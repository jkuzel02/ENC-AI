"""Executable contracts for the planned LangGraph RCA workflows."""

import json
from importlib import import_module
from unittest.mock import Mock

import pytest


SPECIALIST_REPORTS = {
    "k8s-config-events": {
        "agent": "k8s-config-events",
        "anomalies": [],
        "suspicious_resources": [],
        "significant_events": [],
        "preliminary_assessment": "No configuration or events were collected.",
    },
    "logs-connectivity": {
        "agent": "logs-connectivity",
        "log_findings": [],
        "connectivity_findings": [],
        "runtime_failure_mode": "unknown",
        "preliminary_assessment": "No logs or checks were collected.",
    },
    "metrics-telemetry": {
        "agent": "metrics-telemetry",
        "resource_findings": [],
        "throttling_detected": False,
        "saturation_identified": None,
        "preliminary_assessment": "No metrics were collected.",
    },
}


@pytest.fixture
def build_workflow(request):
    try:
        module = import_module("proj.rca.workflows")
    except ModuleNotFoundError as error:
        if request.config.getoption("runxfail") or error.name not in {
            "proj.rca",
            "proj.rca.workflows",
        }:
            raise
        pytest.xfail("The LangGraph workflows have yet to be implemented.")
    return module.build_workflow


@pytest.fixture
def context():
    return {
        "incident": "The api becomes unavailable during repeated restarts.",
        "time_window": None,
        "resources": [
            {
                "kind": "Deployment",
                "metadata": {"name": "api", "namespace": "rca-test"},
                "spec": {
                    "template": {
                        "spec": {
                            "containers": [
                                {
                                    "name": "web",
                                    "resources": {
                                        "requests": {"memory": "32Mi"},
                                        "limits": {"memory": "64Mi"},
                                    },
                                }
                            ]
                        }
                    }
                },
            }
        ],
        "events": [{"reason": "OOMKilled", "involved_object": "Pod/api"}],
        "logs": [{"container": "web", "message": "retained_mib=56"}],
        "metrics": [],
        "checks": [{"target": "Service/api", "status": "failed"}],
    }


@pytest.fixture
def root_cause():
    return {
        "cause": "The web container exceeds its 64Mi memory limit.",
        "causal_chain": "Memory exhaustion kills the container and interrupts requests.",
        "supporting_evidence": ["64Mi memory limit", "OOMKilled event"],
        "remediation": "Raise the memory limit to fit the legitimate working set.",
        "recovery_check": "Requests succeed without further OOM terminations.",
    }


@pytest.mark.parametrize("variant", ["base", "optimal"])
def test_single_agent_uses_its_prompt_with_the_full_context(
    build_workflow, context, root_cause, variant
):
    response = json.dumps(root_cause) if variant == "optimal" else "The memory limit is too low."
    complete = Mock(return_value=response)
    graph = build_workflow(variant, complete=complete)

    result = graph.invoke({"context": context})

    complete.assert_called_once_with(f"{variant}.md", {"context": context})
    expected = root_cause if variant == "optimal" else response
    assert result["root-cause"] == expected


def test_mas_routes_domain_inputs_then_synthesizes_reports(build_workflow, context, root_cause):
    responses = {f"mas/{agent}.md": report for agent, report in SPECIALIST_REPORTS.items()}
    responses["mas/coordinator.md"] = root_cause
    complete = Mock(side_effect=lambda prompt, payload: json.dumps(responses[prompt]))
    graph = build_workflow("mas", complete=complete)

    result = graph.invoke({"context": context})

    calls = [call.args for call in complete.call_args_list]
    assert len(calls) == 4
    assert dict(calls[:-1]) == {
        "mas/k8s-config-events.md": {
            "resources": context["resources"],
            "events": context["events"],
        },
        "mas/logs-connectivity.md": {
            "logs": context["logs"],
            "checks": context["checks"],
        },
        "mas/metrics-telemetry.md": {
            "metrics": [],
            "time_window": None,
            "resource_limits": [
                {
                    "resource": "Deployment/api",
                    "namespace": "rca-test",
                    "container": "web",
                    "requests": {"memory": "32Mi"},
                    "limits": {"memory": "64Mi"},
                }
            ],
        },
    }
    assert calls[-1] == (
        "mas/coordinator.md",
        {"context": context, "agent_reports": SPECIALIST_REPORTS},
    )
    assert result["root-cause"] == root_cause


@pytest.mark.parametrize("variant", ["optimal", "mas"])
@pytest.mark.parametrize("bad_output", ["not JSON", '{"cause": "incomplete"}'])
def test_structured_final_response_must_match_the_rca_schema(
    build_workflow, context, variant, bad_output
):
    def complete(prompt, payload):
        agent = prompt.removeprefix("mas/").removesuffix(".md")
        if agent in SPECIALIST_REPORTS:
            return json.dumps(SPECIALIST_REPORTS[agent])
        return bad_output

    with pytest.raises(ValueError):
        build_workflow(variant, complete=complete).invoke({"context": context})


def test_invalid_specialist_report_never_reaches_coordinator(build_workflow, context):
    reports = {**SPECIALIST_REPORTS, "metrics-telemetry": {"agent": "metrics-telemetry"}}

    def respond(prompt, payload):
        agent = prompt.removeprefix("mas/").removesuffix(".md")
        return json.dumps(reports[agent])

    complete = Mock(side_effect=respond)
    with pytest.raises(ValueError):
        build_workflow("mas", complete=complete).invoke({"context": context})

    assert "mas/coordinator.md" not in [call.args[0] for call in complete.call_args_list]


@pytest.mark.parametrize("variant", ["base", "optimal", "mas"])
def test_provider_errors_propagate(build_workflow, context, variant):
    unavailable = TimeoutError("provider unavailable")
    graph = build_workflow(variant, complete=Mock(side_effect=unavailable))

    with pytest.raises(TimeoutError) as error:
        graph.invoke({"context": context})

    assert error.value is unavailable
