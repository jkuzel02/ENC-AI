# 15 — Backend OOM causes a frontend outage

## Layout and reference answer

- `app/` applies the healthy configuration in `app/base/`, containing individual Kubernetes resources and application source mounted through ConfigMap/code.
- `app/fault/` overlays only the intended fault; apply it with `-k`, not by applying its patch files directly.
- `rca.json` contains `context` and the evaluator-only `root-cause`. This per-directory path replaces the illustrative flat filenames retained in the first 42 lines of `../../examples.md`.

The fixture is **not a captured incident**. `context.resources` is the rendered faulty configuration (Secret values are redacted); `time_window` is null and events/logs/metrics/checks are empty because no cluster run was performed. Empty evidence arrays mean **not collected**, not zero measurements. Before benchmarking, replace static configuration with the relevant live objects and add timestamped observations and a UTC time window. The reference `supporting_evidence` lists expected evidence criteria, not observed facts. Give the LLM only the populated `context`, never this README, the fault overlay path, or `root-cause`.

## Root cause

Deployment/backend limits its web container to 64Mi although the backend retains a bounded 128 MiB allocation plus interpreter overhead.

The backend exceeds its cgroup memory limit and is OOM-killed; backend downtime causes frontend dependency errors and user-visible HTTP 502 responses.

## Prerequisites

Use the project's local `kind-local` cluster with spare capacity, registry access, and permission to manage namespace `rca-15`. Run one case at a time. These resources are outside the existing Flux demo reconciliation scope. Manifests use `python:3.12.8-slim`; record the resolved image digest and Kubernetes/CNI versions for a frozen benchmark. Baseline/fault application is manual and the commands below are not executed automatically.

No extra cluster extension is required. Validate the healthy baseline before injecting the fault.

## Establish a healthy baseline

Run from this case directory (from `proj/`, first run `cd example-cases/15`).

```sh
kubectl --context kind-local apply -k app/
kubectl --context kind-local -n rca-15 rollout status deployment/api --timeout=180s
kubectl --context kind-local -n rca-15 rollout status deployment/backend --timeout=180s
kubectl --context kind-local -n rca-15 rollout status deployment/load --timeout=180s
```

Verify successful requests through the Service before proceeding; readiness alone does not prove the scenario is healthy.

## Inject the fault

```sh
kubectl --context kind-local apply -k app/fault/
```

Allow the symptoms to stabilize and record the start/end of a fixed incident window. Do not require a successful rollout for a scenario designed to prevent readiness, scheduling, image retrieval, or startup.

## Capture and distinguish evidence

Expected evidence to obtain:

- Backend termination history shows OOMKilled, the limit is 64Mi, and allocation is configured to retain 128 MiB.
- Correlate backend OOM/restart timestamps and endpoint readiness changes with frontend dependency errors and load-generator HTTP 502 responses.
- The frontend remains healthy without local restarts or resource exhaustion; node conditions exclude node memory pressure.

Allow at least 30 seconds after readiness for the gradual 128 MiB allocation to finish in the healthy baseline. Capture previous backend/worker logs before they are overwritten by further restarts. Memory scraping can miss short-lived peaks. Exit code 137 alone is not proof of OOM.

Useful read-only capture commands:

```sh
kubectl --context kind-local -n rca-15 get pods -o yaml
kubectl --context kind-local -n rca-15 get deployment,service,endpointslice,configmap -o yaml
kubectl --context kind-local -n rca-15 get events --sort-by=.metadata.creationTimestamp -o yaml
kubectl --context kind-local -n rca-15 logs deployment/api --timestamps --tail=200
kubectl --context kind-local -n rca-15 logs deployment/backend --previous --timestamps --tail=200
kubectl --context kind-local -n rca-15 logs deployment/load --timestamps --tail=500
```

Commands for logs may fail intentionally when the container has never started or has no previous instance; record that absence rather than inserting guessed logs. Use the Pod name and container name for exact restart attribution, especially during rollouts. Redact sensitive values before adding observations to `context`. Capture node conditions and relevant Prometheus metrics separately when the expected evidence calls for them.

For HTTP cases, use a separate healthy in-cluster client (or the existing load/control workload) when api cannot be exec'd. Port-forwarding a Deployment reaches a Pod directly and does not validate Service routing.

## Recover and verify

```sh
kubectl --context kind-local apply -k app/
kubectl --context kind-local -n rca-15 rollout status deployment/api --timeout=180s
kubectl --context kind-local -n rca-15 rollout status deployment/backend --timeout=180s
kubectl --context kind-local -n rca-15 rollout status deployment/load --timeout=180s
```

The backend completes its allocation without new OOM terminations and frontend requests succeed at the original offered load. Keep recovery observations outside the LLM incident context.

## Compare the LLM answer

Compare the predicted `cause`, `causal_chain`, cited `supporting_evidence`, `remediation`, and `recovery_check` with `rca.json["root-cause"]` semantically. Require the affected object/configuration field and the specific fault, not just a Pod status. Reward only evidence present in the captured context. If required observations are missing, an appropriately qualified diagnosis is preferable to fabricated certainty. All three AI approaches must receive the identical captured context.

## Cleanup and validation status

Only this disposable case namespace is removed by:

```sh
kubectl --context kind-local delete namespace rca-15 --wait=true --timeout=120s
```

Both Kustomize variants were rendered locally, JSON was parsed and cross-checked against the faulty rendered resources, and Python source was syntax-checked. No cluster deployment, runtime fault injection, or recovery test has been performed.
