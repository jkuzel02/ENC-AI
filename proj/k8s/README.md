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

### Install cert-manager & Deploy Itself-managed Resources

We want an automated TLS certificate management layer and [cert-manager](https://cert-manager.io/) can do just that.

Install release:

```bash
helm install cert-manager \
  oci://quay.io/jetstack/charts/cert-manager \
  --version v1.21.3 \
  --namespace cert-manager \
  --create-namespace \
  --set crds.enabled=true \
  --wait
```

Deploy manifests:

```bash
kubectl apply -f cert-manager/
```

### Install GatewayAPI Resources

To obtain [GatewayAPI](https://gateway-api.sigs.k8s.io/) resources run the following command:

```bash
kubectl apply --server-side -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.6.3/standard-install.yaml
```

### Install Traefik

To actually use GatewayAPI for cluster traffic ingress, let's install [Traefik](https://traefik.io/solutions/gateway-api):

```bash
helm upgrade --install traefik traefik \
  --repo https://traefik.github.io/charts \
  --version 42.1.3 \
  --namespace traefik \
  --create-namespace \
  --values traefik/values.yaml \
  --wait
```

And we have to manually set the HTTP to HTTPS redirect as well as to allow the TLS Secret inter-namespace-reference:

```bash
kubectl apply -f traefik/http-2-https.yaml
kubectl apply -f traefik/allow-traefik-tls.yaml
```

### Install Flux CD

To be able to work with [GitOps](https://about.gitlab.com/topics/gitops/) approach for Continuous Delivery, we'll use [Flux CD](https://fluxcd.io/).

The most k8s-native (and actually the most easy-2-manage) is to use Flux Operator:

```bash
helm upgrade --install flux-operator \
  oci://ghcr.io/controlplaneio-fluxcd/charts/flux-operator \
  --version 0.61.0 \
  --namespace flux-system \
  --create-namespace \
  --values flux-operator/values.yaml \
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

### Demo GitRepository & Kustomization

```bash
kubectl apply -f demo/
```
