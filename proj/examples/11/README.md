# 11 — NetworkPolicy omits a required dependency

## Layout and reference answer

- `app/` applies the healthy configuration in `app/base/`, containing individual Kubernetes resources and application source mounted through ConfigMap/code.
- `app/fault/` overlays only the intended fault; apply it with `-k`, not by applying its patch files directly.
- `rca.json` contains `context` and the evaluator-only `root-cause`. This per-directory path replaces the illustrative flat filenames retained in the first 42 lines of `../../examples.md`.

The fixture is **not a captured incident**. `context.resources` is the rendered faulty configuration (Secret values are redacted); `time_window` is null and events/logs/metrics/checks are empty because no cluster run was performed. Empty evidence arrays mean **not collected**, not zero measurements. Before benchmarking, replace static configuration with the relevant live objects and add timestamped observations and a UTC time window. The reference `supporting_evidence` lists expected evidence criteria, not observed facts. Give the LLM only the populated `context`, never this README, the fault overlay path, or `root-cause`.

## Root cause

NetworkPolicy/frontend-egress isolates app=api Pods but permits only DNS, omitting required backend egress on TCP 8080.

With an enforcing CNI and no additive allow rule, backend traffic from selected frontend Pods is denied while DNS and unrelated clients still work.

## Prerequisites

Use the project's local `kind-local` cluster with spare capacity, registry access, and permission to manage namespace `rca-11`. Run one case at a time. These resources are outside the existing Flux demo reconciliation scope. Manifests use `python:3.12.8-slim`; record the resolved image digest and Kubernetes/CNI versions for a frozen benchmark. Baseline/fault application is manual and the commands below are not executed automatically.

This case requires a CNI that enforces NetworkPolicy. Default kind networking may not enforce it. Verify enforcement using a disposable deny/allow connectivity check before this experiment; otherwise mark the run unsupported. This policy allows TCP/UDP DNS to any destination so it also works with node-local DNS. Ensure no other policy allows frontend backend traffic.

## Establish a healthy baseline

Run from this case directory (from `proj/`, first run `cd example-cases/11`).

```sh
kubectl --context kind-local apply -k app/
kubectl --context kind-local -n rca-11 rollout status deployment/api --timeout=180s
kubectl --context kind-local -n rca-11 rollout status deployment/backend --timeout=180s
kubectl --context kind-local -n rca-11 rollout status deployment/control --timeout=180s
```

Verify successful requests through the Service before proceeding; readiness alone does not prove the scenario is healthy.

## Inject the fault

```sh
kubectl --context kind-local apply -k app/fault/
```

Allow the symptoms to stabilize and record the start/end of a fixed incident window. Do not require a successful rollout for a scenario designed to prevent readiness, scheduling, image retrieval, or startup.

## Capture and distinguish evidence

Expected evidence to obtain:

- The enforcing policy selects app=api and its egress rules allow only TCP/UDP 53.
- Service/backend endpoints and backend readiness are healthy, and frontend DNS lookup succeeds.
- A frontend TCP check to backend:8080 fails while the equivalent check from the unselected control client succeeds; review every additive policy.

Both app=api and app=backend stay Ready because their probes are local. Compare DNS plus TCP backend:8080 from api and the unselected control Deployment. Inspect all policies, namespace labels and optional policy-engine drop logs before attributing a timeout to policy denial.

Useful read-only capture commands:

```sh
kubectl --context kind-local -n rca-11 get pods -o yaml
kubectl --context kind-local -n rca-11 get deployment,service,endpointslice,configmap -o yaml
kubectl --context kind-local -n rca-11 get events --sort-by=.metadata.creationTimestamp -o yaml
kubectl --context kind-local -n rca-11 logs deployment/api --timestamps --tail=200
kubectl --context kind-local -n rca-11 get networkpolicy -o yaml
kubectl --context kind-local -n rca-11 exec deployment/api -- python -c 'import socket; print(socket.getaddrinfo("backend", 8080)); print(socket.create_connection(("backend", 8080), timeout=3))'
kubectl --context kind-local -n rca-11 exec deployment/control -- python -c 'import socket; print(socket.getaddrinfo("backend", 8080)); print(socket.create_connection(("backend", 8080), timeout=3))'
```

Commands for logs may fail intentionally when the container has never started or has no previous instance; record that absence rather than inserting guessed logs. Use the Pod name and container name for exact restart attribution, especially during rollouts. Redact sensitive values before adding observations to `context`. Capture node conditions and relevant Prometheus metrics separately when the expected evidence calls for them.

For HTTP cases, use a separate healthy in-cluster client (or the existing load/control workload) when api cannot be exec'd. Port-forwarding a Deployment reaches a Pod directly and does not validate Service routing.

## Recover and verify

```sh
kubectl --context kind-local apply -k app/
kubectl --context kind-local -n rca-11 rollout status deployment/api --timeout=180s
kubectl --context kind-local -n rca-11 rollout status deployment/backend --timeout=180s
kubectl --context kind-local -n rca-11 rollout status deployment/control --timeout=180s
```

Frontend-to-backend requests succeed with the policy still selecting the frontend and DNS continuing to work. Keep recovery observations outside the LLM incident context.

## Compare the LLM answer

Compare the predicted `cause`, `causal_chain`, cited `supporting_evidence`, `remediation`, and `recovery_check` with `rca.json["root-cause"]` semantically. Require the affected object/configuration field and the specific fault, not just a Pod status. Reward only evidence present in the captured context. If required observations are missing, an appropriately qualified diagnosis is preferable to fabricated certainty. All three AI approaches must receive the identical captured context.

## Cleanup and validation status

Only this disposable case namespace is removed by:

```sh
kubectl --context kind-local delete namespace rca-11 --wait=true --timeout=120s
```

Both Kustomize variants were rendered locally, JSON was parsed and cross-checked against the faulty rendered resources, and Python source was syntax-checked. No cluster deployment, runtime fault injection, or recovery test has been performed.
