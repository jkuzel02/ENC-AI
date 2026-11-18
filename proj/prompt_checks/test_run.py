"""Offline checks of the live prompt runner and its case fixtures."""

import json
from io import BytesIO
from unittest import TestCase
from unittest.mock import patch

from proj.prompt_checks.run import (
    ENDPOINT,
    SPECIALISTS,
    complete,
    evaluate_case,
    load_inputs,
    missing_concepts,
)


REPORTS = {
    "k8s-config-events": {
        "agent": "k8s-config-events",
        "anomalies": [],
        "suspicious_resources": [],
        "significant_events": [],
        "preliminary_assessment": "Configuration observations received.",
    },
    "logs-connectivity": {
        "log_findings": [],
        "agent": "logs-connectivity",
        "connectivity_findings": [],
        "runtime_failure_mode": "unknown",
        "preliminary_assessment": "Further runtime evidence is needed.",
    },
    "metrics-telemetry": {
        "resource_findings": [],
        "throttling_detected": False,
        "saturation_identified": None,
        "preliminary_assessment": "Further telemetry is needed.",
    },
}


class PromptRunnerTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prompts, cls.cases, cls.expectations = load_inputs()

    def test_every_prompt_receives_the_right_inputs_for_every_case(self):
        for case_id, case in self.cases.items():
            with self.subTest(case=case_id):
                context = case["context"]
                expected = case["root-cause"]
                calls = {}

                def send(prompt, payload):
                    self.assertNotIn(prompt, calls)
                    calls[prompt] = payload
                    self.assertNotIn("root-cause", payload)
                    if prompt == "base.md":
                        return expected["cause"], None
                    response = REPORTS.get(prompt.split("/")[-1].removesuffix(".md"), expected)
                    return json.dumps(response), None

                results = evaluate_case(case_id, context, self.expectations[case_id], send)

                failures = {
                    result["prompt"]: result["error"]
                    for result in results
                    if result["status"] != "passed"
                }
                self.assertEqual(failures, {})
                self.assertEqual(calls.keys(), self.prompts.keys())
                self.assertEqual(calls["base.md"], {"context": context})
                self.assertEqual(calls["optimal.md"], {"context": context})
                for specialist, fields in SPECIALISTS.items():
                    payload = calls[f"mas/{specialist}.md"].copy()
                    if specialist == "metrics-telemetry":
                        limits = payload.pop("resource_limits")
                        if case_id == "01":
                            self.assertIn(
                                {
                                    "resource": "Deployment/api",
                                    "namespace": "rca-01",
                                    "container": "web",
                                    "requests": {"cpu": "25m", "memory": "32Mi"},
                                    "limits": {"cpu": "500m", "memory": "64Mi"},
                                },
                                limits,
                            )
                    self.assertEqual(payload, {field: context[field] for field in fields})
                self.assertEqual(
                    calls["mas/coordinator.md"], {"context": context, "agent_reports": REPORTS}
                )
                self.assertEqual(list(calls)[-1], "mas/coordinator.md")

    def test_invalid_specialist_report_blocks_only_coordinator(self):
        case = self.cases["01"]

        def send(prompt, payload):
            responses = {
                "base.md": case["root-cause"]["cause"],
                "optimal.md": "```json\n{}\n```",
                "mas/k8s-config-events.md": "{}",
                "mas/logs-connectivity.md": json.dumps(REPORTS["logs-connectivity"]),
                "mas/metrics-telemetry.md": json.dumps(REPORTS["metrics-telemetry"]),
            }
            return responses[prompt], None

        results = evaluate_case("01", case["context"], self.expectations["01"], send)

        self.assertEqual(
            [result["status"] for result in results],
            ["passed", "failed", "failed", "passed", "passed", "blocked"],
        )
        self.assertIn("Invalid JSON", results[1]["error"])
        self.assertIn("Schema violation", results[2]["error"])

    def test_generic_symptom_is_not_a_diagnosis(self):
        groups = self.expectations["01"]
        self.assertEqual(missing_concepts("CrashLoopBackOff", groups), groups)
        cpu_groups = self.expectations["02"]
        self.assertEqual(missing_concepts("CPU limit is 150m", cpu_groups), cpu_groups[1:])

    def test_specialists_cannot_report_missing_observations_as_measured(self):
        case = self.cases["01"]
        reports = {
            **REPORTS,
            "logs-connectivity": {
                **REPORTS["logs-connectivity"],
                "log_findings": [
                    {"source": "web", "level": "error", "summary": "Out of memory."}
                ],
            },
            "metrics-telemetry": {**REPORTS["metrics-telemetry"], "throttling_detected": True},
        }

        def send(prompt, payload):
            agent = prompt.removeprefix("mas/").removesuffix(".md")
            diagnosis = case["root-cause"]
            if prompt == "base.md":
                return diagnosis["cause"], None
            return json.dumps(reports.get(agent, diagnosis)), None

        results = evaluate_case("01", case["context"], self.expectations["01"], send)

        self.assertIn("no logs in the input", results[3]["error"])
        self.assertIn("no metrics in the input", results[4]["error"])
        self.assertEqual(results[-1]["status"], "blocked")

    @patch("proj.prompt_checks.run.urlopen")
    def test_chat_completion_request_and_usage(self, urlopen):
        response = {
            "choices": [{"message": {"content": "RCA result"}, "finish_reason": "stop"}],
            "usage": {"total_tokens": 42},
        }
        urlopen.return_value = BytesIO(json.dumps(response).encode("utf-8"))

        self.assertEqual(
            complete("test-model", "fake-key", "Prompt", {"context": {}}),
            ("RCA result", {"total_tokens": 42}),
        )
        request = urlopen.call_args.args[0]
        self.assertEqual(request.full_url, ENDPOINT)
        self.assertEqual(request.get_method(), "POST")
        self.assertEqual(request.get_header("Authorization"), "Bearer fake-key")
        body = json.loads(request.data)
        self.assertEqual(body["model"], "test-model")
        self.assertEqual(body["messages"][0], {"role": "system", "content": "Prompt"})
        self.assertEqual(json.loads(body["messages"][1]["content"]), {"context": {}})
