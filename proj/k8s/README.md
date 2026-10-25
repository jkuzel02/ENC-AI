# Local Kubernetes Cluster

Create a locally running Kubernetes cluster with [kind]((https://kind.sigs.k8s.io)) (**K**ubernetes **in** **D**ocker).

## Requirements

We want to have installed the following set of tools, to be able to work with local Kubernetes cluster:

- [docker](https://docs.docker.com/engine/install/) (on Windows use docker inside [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install))
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- [helm](https://helm.sh/docs/intro/install/)

## Deploy the Example Cluster

Create the example cluster with kind:

```bash
kind create cluster --config kind/kind.yaml
```

After creating a cluster, new context is going to be insterted into KUBECONFIG `~/.kube/config`.

We need to install few other resources as well.

### Install Flux CD

To be able to work with [GitOps](https://about.gitlab.com/topics/gitops/) approach for Continuous Delivery, we'll use [Flux CD](https://fluxcd.io/).

The most k8s-native (and actually the most easy-2-manage) is to use Flux Operator:

```bash
helm upgrade --install flux-operator \
  oci://ghcr.io/controlplaneio-fluxcd/charts/flux-operator \
  --version 0.61.0 \
  --namespace flux-system \
  --create-namespace \
  --wait
```

Then install Flux CD instance itself:

```bash
helm upgrade --install flux-instance \
  oci://ghcr.io/controlplaneio-fluxcd/charts/flux-instance \
  --version 0.61.0 \
  --namespace flux-system \
  --set instance.cluster.size=medium \
  --wait
```

### Bootstrap the Rest

Now let the Flux do the job for us with applying all that is inside `flux/`.

```bash
kubectl apply -f flux/
```
