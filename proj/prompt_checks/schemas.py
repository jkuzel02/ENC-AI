"""Response schemas transcribed from the prompt definitions."""

TEXT = {"type": "string", "pattern": r"\S"}


def array(items, *, minimum=0):
    return {"type": "array", "items": items, "minItems": minimum}


def object_with(**fields):
    return {
        "type": "object",
        "properties": fields,
        "required": list(fields),
        "additionalProperties": False,
    }


RCA = object_with(
    cause=TEXT,
    causal_chain=TEXT,
    supporting_evidence=array(TEXT, minimum=1),
    remediation=TEXT,
    recovery_check=TEXT,
)

CASE = object_with(
    context=object_with(
        incident=TEXT,
        time_window={"type": ["null", "string", "object"]},
        resources=array({"type": "object"}),
        events=array({}),
        logs=array({}),
        metrics=array({}),
        checks=array({}),
    ),
    **{"root-cause": RCA},
)

REPORT_SCHEMAS = {
    "k8s-config-events": object_with(
        agent={"const": "k8s-config-events"},
        anomalies=array(
            object_with(
                resource=TEXT,
                field=TEXT,
                issue=TEXT,
                severity={"enum": ["low", "medium", "high"]},
            )
        ),
        suspicious_resources=array(TEXT),
        significant_events=array(object_with(reason=TEXT, involved_object=TEXT, message=TEXT)),
        preliminary_assessment=TEXT,
    ),
    "logs-connectivity": object_with(
        agent={"const": "logs-connectivity"},
        log_findings=array(
            object_with(
                source=TEXT,
                level={"enum": ["info", "warning", "error"]},
                summary=TEXT,
            )
        ),
        connectivity_findings=array(
            object_with(target=TEXT, status={"enum": ["passed", "failed"]}, details=TEXT)
        ),
        runtime_failure_mode=TEXT,
        preliminary_assessment=TEXT,
    ),
    "metrics-telemetry": object_with(
        resource_findings=array(
            object_with(
                metric_name=TEXT,
                observed_value=TEXT,
                limit_value={"anyOf": [TEXT, {"type": "null"}]},
                status={"enum": ["normal", "elevated", "saturated", "throttled", "uncollected"]},
                analysis=TEXT,
            )
        ),
        throttling_detected={"type": "boolean"},
        saturation_identified={"anyOf": [TEXT, {"type": "null"}]},
        preliminary_assessment=TEXT,
    ),
}
