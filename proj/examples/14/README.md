# 14 — ServiceAccount lacks a required API permission

## Layout and reference answer

- `app/` applies the healthy configuration in `app/base/`, containing individual Kubernetes resources and application source mounted through ConfigMap/code.
- `app/fault/` overlays only the intended fault; apply it with `-k`, not by applying its patch files directly.
- `rca.json` contains `context` and the evaluator-only `root-cause`. This per-directory path replaces the illustrative flat filenames retained in the first 42 lines of `../../examples.md`.

The fixture is **not a captured incident**. `context.resources` is the rendered faulty configuration (Secret values are redacted); `time_window` is null and events/logs/metrics/checks are empty because no cluster run was performed. Empty evidence arrays mean **not collected**, not zero measurements. Before benchmarking, replace static configuration with the relevant live objects and add timestamped observations and a UTC time window. The reference `supporting_evidence` lists expected evidence criteria, not observed facts. Give the LLM only the populated `context`, never this README, the fault overlay path, or `root-cause`.

## Root cause

Role/config-reader permits get but omits list on ConfigMaps for ServiceAccount/controller.

The API server authenticates the ServiceAccount, but RBAC denies its list request with HTTP 403, preventing reconciliation.

## Prerequisites

Use the project's local `kind-local` cluster with spare capacity, registry access, and permission to manage namespace `rca-14`. Run one case at a time. These resources are outside the existing Flux demo reconciliation scope. Manifests use `python:3.12.8-slim`; record the resolved image digest and Kubernetes/CNI versions for a frozen benchmark. Baseline/fault application is manual and the commands below are not executed automatically.

The cluster must use normal RBAC enforcement. Ensure no other RoleBinding or ClusterRoleBinding grants this test ServiceAccount list permission. API connectivity and the mounted ServiceAccount token must work in the healthy baseline.

## Establish a healthy baseline

Run from this case directory (from `proj/`, first run `cd example-cases/14`).

```sh
kubectl --context kind-local apply -k app/
kubectl --context kind-local -n rca-14 rollout status deployment/api --timeout=180s
```

Check controller logs for successful get and list requests.

## Inject the fault

```sh
kubectl --context kind-local apply -k app/fault/
```

Allow the symptoms to stabilize and record the start/end of a fixed incident window. Do not require a successful rollout for a scenario designed to prevent readiness, scheduling, image retrieval, or startup.

## Capture and distinguish evidence

Expected evidence to obtain:

- Deployment/api uses ServiceAccount/controller and RoleBinding/config-reader binds it to Role/config-reader.
- The Role verbs include get but not list for core ConfigMaps.
- Controller logs show get=200 and list=403 Forbidden identifying the ServiceAccount; authorization checks agree.

Controller logs issue both get settings and list configmaps every five seconds. Verify get=200 continues while list=403. Use authorization checks for system:serviceaccount:rca-14:controller; the admin running those checks needs impersonation permission. Never copy mounted bearer tokens into the dataset.

Useful read-only capture commands:

```sh
kubectl --context kind-local -n rca-14 get pods -o yaml
kubectl --context kind-local -n rca-14 get deployment,service,endpointslice,configmap -o yaml
kubectl --context kind-local -n rca-14 get events --sort-by=.metadata.creationTimestamp -o yaml
kubectl --context kind-local -n rca-14 logs deployment/api --timestamps --tail=200
kubectl --context kind-local -n rca-14 get role,rolebinding,serviceaccount -o yaml
kubectl --context kind-local -n rca-14 auth can-i get configmaps --as=system:serviceaccount:rca-14:controller
kubectl --context kind-local -n rca-14 auth can-i list configmaps --as=system:serviceaccount:rca-14:controller
```

Commands for logs may fail intentionally when the container has never started or has no previous instance; record that absence rather than inserting guessed logs. Use the Pod name and container name for exact restart attribution, especially during rollouts. Redact sensitive values before adding observations to `context`. Capture node conditions and relevant Prometheus metrics separately when the expected evidence calls for them.

Authorization checks require the invoking administrator to have impersonation permission; a denied impersonation request is not evidence about the controller ServiceAccount.

## Recover and verify

```sh
kubectl --context kind-local apply -k app/
kubectl --context kind-local -n rca-14 rollout status deployment/api --timeout=180s
```

The same ServiceAccount can list ConfigMaps and controller logs show successful reconciliation without granting cluster-admin. Keep recovery observations outside the LLM incident context.

## Compare the LLM answer

Compare the predicted `cause`, `causal_chain`, cited `supporting_evidence`, `remediation`, and `recovery_check` with `rca.json["root-cause"]` semantically. Require the affected object/configuration field and the specific fault, not just a Pod status. Reward only evidence present in the captured context. If required observations are missing, an appropriately qualified diagnosis is preferable to fabricated certainty. All three AI approaches must receive the identical captured context.

## Cleanup and validation status

Only this disposable case namespace is removed by:

```sh
kubectl --context kind-local delete namespace rca-14 --wait=true --timeout=120s
```

Both Kustomize variants were rendered locally, JSON was parsed and cross-checked against the faulty rendered resources, and Python source was syntax-checked. No cluster deployment, runtime fault injection, or recovery test has been performed.
