# Kubernetes RCA example cases

These 15 proposed cases support the experiment in `proposal.md`: compare a single agent with a basic prompt, a single agent with an optimized prompt, and a multi-agent system using the same incident evidence. They are scenario specifications, not results collected from a running cluster.

## Table of contents

- [01 — Memory limit below a legitimate working set](examples/01/)
- [02 — CPU throttling under steady load](examples/02/)
- [03 — Invalid application configuration](examples/03/)
- [04 — Nonexistent container image tag](examples/04/)
- [05 — Missing key in a referenced Secret](examples/05/)
- [06 — Liveness probe kills a healthy but slow-starting application](examples/06/)
- [07 — Readiness probe uses the wrong HTTP path](examples/07/)
- [08 — Service selector matches no Pods](examples/08/)
- [09 — Service forwards to the wrong target port](examples/09/)
- [10 — Incorrect dependency DNS name](examples/10/)
- [11 — NetworkPolicy omits a required dependency](examples/11/)
- [12 — CPU request exceeds schedulable node capacity](examples/12/)
- [13 — PVC references a nonexistent StorageClass](examples/13/)
- [14 — ServiceAccount lacks a required API permission](examples/14/)
- [15 — Backend OOM causes a frontend outage](examples/15/)

## Dataset format

The dataset location is `examples/`, with one numbered directory per case containing a `README.md`, an `app/` directory, and an `rca.json` file. Each JSON file has exactly two top-level keys:

```json
{
  "context": {
    "incident": "User-visible problem and affected workload",
    "time_window": "UTC start and end of the captured observation window",
    "resources": [],
    "events": [],
    "logs": [],
    "metrics": [],
    "checks": []
  },
  "root-cause": {
    "cause": "Specific fault and affected resource or configuration field",
    "causal_chain": "How the fault produces the observed problem",
    "supporting_evidence": [],
    "remediation": "Recommended correction",
    "recovery_check": "Observable condition confirming recovery"
  }
}
```

Give agents only `context`. Keep `root-cause` private to the evaluator. Use neutral directory names such as `01/`, so paths do not reveal diagnoses. The descriptive titles above are authoring notes, not agent input.

Populate `context` with actual observations when implementing the cases. The evidence described below is expected evidence to capture, not fabricated telemetry to present as a real run. Preserve timestamps, namespaces, resource names, container names, units, and relevant configuration. Record unavailable evidence explicitly; an empty metrics list must not imply measured zero usage. Redact secret values while retaining key names and error categories.

## Execution and evaluation conditions

- Establish a healthy baseline, inject the specified fault, capture a fixed evidence window, then restore the baseline. Run one case at a time in an isolated test namespace.
- The current demo contains HTTP echo applications. Cases requiring configuration validation, authentication, memory allocation, startup delays, or dependency calls have dedicated test workloads under `examples/`.
- Flux manages the existing demo. Use dedicated test resources outside its reconciliation scope, or an explicit GitOps-controlled fault mechanism, so reconciliation does not silently undo a fault during capture.
- Preserve the same evidence bundle and task prompt across all three approaches. Keep the injection instructions and expected answer outside agent input. Compare diagnosis accuracy, evidence correctness, output structure, analysis time, and total token usage across all agents and tool calls.
- Score the specific underlying fault, not just a status such as `CrashLoopBackOff`. Require cited evidence and a causal explanation. Report unsupported claims separately. If essential evidence is missing, accept an appropriately qualified diagnosis rather than rewarding invented certainty.
- Verify recovery after the correction, but keep recovery observations out of the incident input. The cases below have not been executed or validated against this cluster.
