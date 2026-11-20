# 16 — Misconfigured CNI plugin prevents Pod networking and sandbox creation

## Layout and reference answer

- `app/` applies the healthy configuration in `app/base/`, containing individual Kubernetes resources and application source mounted through `ConfigMap/code`.
- `app/fault/` overlays the faulty CNI configuration manifest (`ConfigMap/cni-config` in `kube-system`); apply it with `-k`, not by applying its files directly.
- `rca.json` contains `context` and the evaluator-only `root-cause`.

The fixture is **not a captured incident**. `context.resources` is the rendered faulty configuration; `time_window` is null and `events`/`logs`/`metrics`/`checks` are empty because no cluster run was performed. Empty evidence arrays mean **not collected**, not zero measurements. Before benchmarking, replace static configuration with the relevant live objects and add timestamped observations and a UTC time window. The reference `supporting_evidence` lists expected evidence criteria, not observed facts. Give the LLM only the populated `context`, never this README, the fault overlay path, or `root-cause`.

## Root cause

The CNI configuration `10-kindnet.conflist` references a nonexistent CNI plugin type (`nonexistent-cni-plugin`), preventing the container runtime from creating Pod network sandboxes.

Without a working CNI plugin, newly scheduled Pods cannot obtain network interfaces or Pod IPs and remain stuck in `ContainerCreating` with `FailedCreatePodSandBox` events.

## Prerequisites

Use a disposable `kind-local` cluster with permission to manage namespace `rca-16`. Run one case at a time.

> **Warning:** Modifying `/etc/cni/net.d/` on a node affects **all** newly scheduled Pods cluster-wide on that node, not only `rca-16`. Always back up the existing CNI conflist first and restore it immediately after capturing evidence.

## Establish a healthy baseline

Run from this case directory (`proj/examples/16/`):

```sh
kubectl --context kind-local apply -k app/
kubectl --context kind-local -n rca-16 rollout status deployment/api --timeout=180s
```

Verify the Pod reaches `Running` and `Ready` with an assigned Pod IP before injecting the fault.

## Inject the fault

1. Apply the fault ConfigMap representation (optional for cluster-side manifest parity):

   ```sh
   kubectl --context kind-local apply -k app/fault/
   ```

2. Back up and break `/etc/cni/net.d/10-kindnet.conflist` on the `local-control-plane` node, then recreate the `api` Pod so kubelet attempts sandbox creation with the broken CNI config:

   ```sh
   docker exec local-control-plane cp /etc/cni/net.d/10-kindnet.conflist /tmp/10-kindnet.conflist.bak
   docker exec -i local-control-plane sh -c 'cat > /etc/cni/net.d/10-kindnet.conflist' <<'EOF'
   {
     "cniVersion": "0.3.1",
     "name": "kindnet",
     "plugins": [
       {
         "type": "nonexistent-cni-plugin",
         "bridge": "cni0",
         "ipam": {
           "type": "host-local",
           "subnet": "10.244.0.0/24"
         }
       }
     ]
   }
   EOF
   kubectl --context kind-local -n rca-16 delete pod -l app=api
   ```

Allow the symptoms to stabilize and record the start/end of a fixed incident window.

## Capture and distinguish evidence

Expected evidence to obtain:

- Node status/conditions (`NetworkUnavailable` or `NetworkPluginNotReady` if kubelet reports CNI readiness failure) and `kindnet` DaemonSet status in `kube-system`.
- Pod status stuck in `ContainerCreating` with no `podIP`.
- Pod events showing `FailedCreatePodSandBox` mentioning the failed CNI plugin (`nonexistent-cni-plugin` not found in CNI path).
- Absence of application container logs because the Pod sandbox and container never start.

Useful read-only capture commands:

```sh
kubectl --context kind-local get nodes -o yaml
kubectl --context kind-local -n kube-system get pods -l app=kindnet -o yaml
kubectl --context kind-local -n rca-16 get pods -o yaml
kubectl --context kind-local -n rca-16 get events --sort-by=.metadata.creationTimestamp -o yaml
kubectl --context kind-local -n rca-16 describe pod -l app=api
```

## Recover and verify

Restore the backed-up CNI configuration on the node, remove the fault ConfigMap, and recreate the Pod:

```sh
docker exec local-control-plane cp /tmp/10-kindnet.conflist.bak /etc/cni/net.d/10-kindnet.conflist
docker exec local-control-plane rm -f /tmp/10-kindnet.conflist.bak
kubectl --context kind-local -n kube-system delete configmap cni-config --ignore-not-found
kubectl --context kind-local -n rca-16 delete pod -l app=api
kubectl --context kind-local -n rca-16 rollout status deployment/api --timeout=180s
```

Keep recovery observations outside the LLM incident context.

## Cleanup

```sh
kubectl --context kind-local delete namespace rca-16 --wait=true --timeout=120s
```
