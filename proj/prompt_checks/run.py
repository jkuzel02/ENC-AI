"""Evaluate the repository's RCA prompts directly against e-INFRA CZ."""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from time import perf_counter
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

from .schemas import CASE, RCA, REPORT_SCHEMAS


PROJECT = Path(__file__).resolve().parents[1]
ENDPOINT = "https://llm.ai.e-infra.cz/v1/chat/completions"
DEFAULT_MODEL = "deepseek-v4.1-flash"
SPECIALISTS = {
    "k8s-config-events": ("resources", "events"),
    "logs-connectivity": ("logs", "checks"),
    "metrics-telemetry": ("metrics", "time_window"),
}
OBSERVATION_FIELDS = {
    "events": "significant_events",
    "logs": "log_findings",
    "checks": "connectivity_findings",
}


def load_inputs():
    prompts = {
        path.relative_to(PROJECT / "prompts").as_posix(): path.read_text(encoding="utf-8")
        for path in (PROJECT / "prompts").rglob("*.md")
        if path.name.lower() != "readme.md"
    }
    expected_prompts = {"base.md", "optimal.md", "mas/coordinator.md"}
    expected_prompts.update(f"mas/{name}.md" for name in SPECIALISTS)
    if prompts.keys() != expected_prompts or any(not text.strip() for text in prompts.values()):
        raise ValueError("Prompt inventory differs from the benchmark or contains an empty prompt.")

    expectations = json.loads(
        Path(__file__).with_name("expectations.json").read_text(encoding="utf-8")
    )
    cases = {
        path.parent.name: json.loads(path.read_text(encoding="utf-8"))
        for path in sorted((PROJECT / "examples").glob("*/rca.json"))
    }
    if not cases or cases.keys() != expectations.keys():
        raise ValueError("Each case must have an entry in expectations.json.")
    fixture_validator = Draft202012Validator(CASE)
    for case_id, case in cases.items():
        try:
            fixture_validator.validate(case)
        except ValidationError as error:
            location = ".".join(map(str, error.absolute_path)) or "root"
            raise ValueError(f"Invalid fixture {case_id} at {location} ({error.validator}).") from None
        if not expectations[case_id]:
            raise ValueError(f"Case {case_id} must define at least one diagnosis check.")
    return prompts, cases, expectations


def complete(model, api_key, prompt, payload):
    request = Request(
        ENDPOINT,
        data=json.dumps(
            {
                "model": model,
                "temperature": 0,
                "stream": False,
                "messages": [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
                ],
            }
        ).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    request.add_unredirected_header("Authorization", f"Bearer {api_key}")
    try:
        with urlopen(request, timeout=60) as response:
            body = json.load(response)
    except HTTPError as error:
        if error.code in {401, 403, 404, 429}:
            raise SystemExit(f"e-INFRA API returned HTTP {error.code}; stopping the run.") from None
        raise ValueError(f"e-INFRA API returned HTTP {error.code}.") from None
    except (URLError, TimeoutError):
        raise ValueError("The e-INFRA request failed or timed out.") from None

    try:
        choice = body["choices"][0]
        content = choice["message"]["content"]
    except (KeyError, IndexError, TypeError):
        raise ValueError("The e-INFRA response has no completion content.") from None
    if choice.get("finish_reason") != "stop":
        raise ValueError("The model did not finish normally.")
    if not isinstance(content, str) or not content.strip():
        raise ValueError("The model returned an empty response.")
    return content, body.get("usage")


def resource_limits(resources):
    limits = []
    for resource in resources:
        spec = resource.get("spec", {})
        pod_spec = spec.get("template", {}).get("spec", spec)
        metadata = resource.get("metadata", {})
        for container in pod_spec.get("containers", []):
            settings = container.get("resources", {})
            if settings:
                limits.append(
                    {
                        "resource": f"{resource['kind']}/{metadata['name']}",
                        "namespace": metadata.get("namespace"),
                        "container": container["name"],
                        "requests": settings.get("requests", {}),
                        "limits": settings.get("limits", {}),
                    }
                )
    return limits


def missing_concepts(text, groups):
    normalized = text.casefold()
    return [
        alternatives
        for alternatives in groups
        if not any(
            re.search(rf"(?<!\w){re.escape(term.casefold())}(?!\w)", normalized)
            for term in alternatives
        )
    ]


def validate_observations(report, payload):
    for source, findings in OBSERVATION_FIELDS.items():
        if findings in report and not payload[source] and report[findings]:
            raise ValueError(f"Reported {findings} with no {source} in the input.")
    if "metrics" in payload and not payload["metrics"]:
        if report["throttling_detected"] or any(
            finding["status"] != "uncollected" for finding in report["resource_findings"]
        ):
            raise ValueError("Reported measured behavior with no metrics in the input.")


def evaluate_case(case_id, context, expectations, send):
    results = []

    def check(prompt, payload, schema=None, score_cause=False):
        result = {"case": case_id, "prompt": prompt, "status": "failed"}
        results.append(result)
        started = perf_counter()
        try:
            content, usage = send(prompt, payload)
            result.update(output=content, usage=usage)
            parsed = content
            if schema is not None:
                parsed = json.loads(content)
                Draft202012Validator(schema).validate(parsed)
                if prompt.removeprefix("mas/").removesuffix(".md") in SPECIALISTS:
                    validate_observations(parsed, payload)
        except json.JSONDecodeError as error:
            result["error"] = f"Invalid JSON (line {error.lineno}, column {error.colno})."
            return None
        except ValidationError as error:
            location = ".".join(map(str, error.absolute_path)) or "root"
            result["error"] = f"Schema violation at {location} ({error.validator})."
            return None
        except ValueError as error:
            result["error"] = str(error)
            return None
        finally:
            result["seconds"] = round(perf_counter() - started, 3)

        if score_cause:
            cause = parsed["cause"] if schema is not None else content
            result["missing_cause_concepts"] = missing_concepts(cause, expectations)
            if result["missing_cause_concepts"]:
                result["error"] = "Expected cause concepts missing."
                return parsed
        result["status"] = "passed"
        return parsed

    check("base.md", {"context": context}, score_cause=True)
    check("optimal.md", {"context": context}, RCA, score_cause=True)
    reports = {}
    for specialist, fields in SPECIALISTS.items():
        payload = {field: context[field] for field in fields}
        if specialist == "metrics-telemetry":
            payload["resource_limits"] = resource_limits(context["resources"])
        report = check(f"mas/{specialist}.md", payload, REPORT_SCHEMAS[specialist])
        if report is not None:
            reports[specialist] = report

    if reports.keys() == SPECIALISTS.keys():
        check(
            "mas/coordinator.md",
            {"context": context, "agent_reports": reports},
            RCA,
            score_cause=True,
        )
    else:
        results.append(
            {
                "case": case_id,
                "prompt": "mas/coordinator.md",
                "status": "blocked",
                "error": "A required specialist report failed.",
            }
        )
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", action="append", help="Case ID to run; repeat to select more.")
    parser.add_argument("--output", type=Path, default=Path("prompt-results.json"))
    args = parser.parse_args()
    api_key = os.environ.get("LLM_AI_EINFRA_API_KEY", "").strip()
    if not api_key:
        parser.error("Set LLM_AI_EINFRA_API_KEY to an e-INFRA API key.")
    model = os.environ.get("LLM_AI_EINFRA_MODEL", "").strip() or DEFAULT_MODEL

    prompts, cases, expectations = load_inputs()
    selected = list(dict.fromkeys(args.case or cases))
    if unknown := sorted(set(selected) - cases.keys()):
        parser.error(f"Unknown case IDs: {', '.join(unknown)}")

    def send(prompt, payload):
        return complete(model, api_key, prompts[prompt], payload)

    results = []
    try:
        for case_id in selected:
            case_results = evaluate_case(case_id, cases[case_id]["context"], expectations[case_id], send)
            results.extend(case_results)
            for result in case_results:
                print(f"{case_id} {result['prompt']}: {result['status']}", flush=True)
    finally:
        args.output.write_text(
            json.dumps({"model": model, "results": results}, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    passed = sum(result["status"] == "passed" for result in results)
    print(f"{passed}/{len(results)} prompt checks passed.")
    return int(passed != len(results))


if __name__ == "__main__":
    sys.exit(main())
