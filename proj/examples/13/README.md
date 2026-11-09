# 13 — PVC references a nonexistent StorageClass

## Layout and reference answer

- `app/` applies the healthy configuration in `app/base/`, containing individual Kubernetes resources and application source mounted through ConfigMap/code.
- `app/fault/` overlays only the intended fault; apply it with `-k`, not by applying its patch files directly.
- `rca.json` contains `context` and the evaluator-only `root-cause`. This per-directory path replaces the illustrative flat filenames retained in the first 42 lines of `../../examples.md`.

The fixture is **not a captured incident**. `context.resources` is the rendered faulty configuration (Secret values are redacted); `time_window` is null and events/logs/metrics/checks are empty because no cluster run was performed. Empty evidence arrays mean **not collected**, not zero measurements. Before benchmarking, replace static configuration with the relevant live objects and add timestamped observations and a UTC time window. The reference `supporting_evidence` lists expected evidence criteria, not observed facts. Give the LLM only the populated `context`, never this README, the fault overlay path, or `root-cause`.

## Root cause

PersistentVolumeClaim/data explicitly requests nonexistent StorageClass/rca-missing-storage.

No matching static PV or dynamic provisioner can satisfy the requested class, leaving the PVC Pending and blocking workload startup.

## Prerequisites

Use the project's local `kind-local` cluster with spare capacity, registry access, and permission to manage namespace `rca-13`. Run one case at a time. These resources are outside the existing Flux demo reconciliation scope. Manifests use `python:3.12.8-slim`; record the resolved image digest and Kubernetes/CNI versions for a frozen benchmark. Baseline/fault application is manual and the commands below are not executed automatically.

A working dynamic provisioner and StorageClass/standard are required (the usual kind default). Check `kubectl --context kind-local get storageclass standard` first. If your valid class has another name, update app/base/persistentvolumeclaim-data.yaml before the run. Confirm rca-missing-storage does not exist and no static PV can match it. This case deletes and recreates only disposable test storage because storageClassName is immutable.

## Establish a healthy baseline

Run from this case directory (from `proj/`, first run `cd example-cases/13`).

```sh
kubectl --context kind-local apply -k app/
kubectl --context kind-local -n rca-13 rollout status deployment/api --timeout=180s
```

Verify successful requests through the Service before proceeding; readiness alone does not prove the scenario is healthy.

## Inject the fault

```sh
kubectl --context kind-local -n rca-13 delete deployment api --wait=true --timeout=60s
kubectl --context kind-local -n rca-13 delete pvc data --wait=true --timeout=60s
kubectl --context kind-local apply -k app/fault/
```

Allow the symptoms to stabilize and record the start/end of a fixed incident window. Do not require a successful rollout for a scenario designed to prevent readiness, scheduling, image retrieval, or startup.

## Capture and distinguish evidence

Expected evidence to obtain:

- PVC/data requests rca-missing-storage, which is absent from the StorageClass inventory.
- PVC remains Pending; capture provisioning/binding events and dependent Pod scheduling events.
- No static PV matches the claim; this is not normal delayed binding for an existing WaitForFirstConsumer class.

Capture PVC and Pod events plus StorageClass/PV inventories. A Pending claim alone is insufficient: distinguish the missing class from normal WaitForFirstConsumer behavior. There are no application logs until storage is mounted.

Useful read-only capture commands:

```sh
kubectl --context kind-local -n rca-13 get pods -o yaml
kubectl --context kind-local -n rca-13 get deployment,service,endpointslice,configmap -o yaml
kubectl --context kind-local -n rca-13 get events --sort-by=.metadata.creationTimestamp -o yaml
kubectl --context kind-local -n rca-13 logs deployment/api --timestamps --tail=200
kubectl --context kind-local -n rca-13 get pvc -o yaml
kubectl --context kind-local get storageclass,pv -o yaml
```

Commands for logs may fail intentionally when the container has never started or has no previous instance; record that absence rather than inserting guessed logs. Use the Pod name and container name for exact restart attribution, especially during rollouts. Redact sensitive values before adding observations to `context`. Capture node conditions and relevant Prometheus metrics separately when the expected evidence calls for them.

For HTTP cases, use a separate healthy in-cluster client (or the existing load/control workload) when api cannot be exec'd. Port-forwarding a Deployment reaches a Pod directly and does not validate Service routing.

## Recover and verify

```sh
kubectl --context kind-local -n rca-13 delete deployment api --wait=true --timeout=60s
kubectl --context kind-local -n rca-13 delete pvc data --wait=true --timeout=60s
kubectl --context kind-local apply -k app/
kubectl --context kind-local -n rca-13 rollout status deployment/api --timeout=180s
```

The recreated PVC becomes Bound and the api container mounts /data and becomes ready. Keep recovery observations outside the LLM incident context.

## Compare the LLM answer

Compare the predicted `cause`, `causal_chain`, cited `supporting_evidence`, `remediation`, and `recovery_check` with `rca.json["root-cause"]` semantically. Require the affected object/configuration field and the specific fault, not just a Pod status. Reward only evidence present in the captured context. If required observations are missing, an appropriately qualified diagnosis is preferable to fabricated certainty. All three AI approaches must receive the identical captured context.

## Cleanup and validation status

Only this disposable case namespace is removed by:

```sh
kubectl --context kind-local delete namespace rca-13 --wait=true --timeout=120s
```

Both Kustomize variants were rendered locally, JSON was parsed and cross-checked against the faulty rendered resources, and Python source was syntax-checked. No cluster deployment, runtime fault injection, or recovery test has been performed.
