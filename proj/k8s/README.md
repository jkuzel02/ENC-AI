# Local Kubernetes Cluster

Create a locally running Kubernetes cluster with [kind]((https://kind.sigs.k8s.io)) (**K**ubernetes **in** **D**ocker).

## Requirements

We want to have installed the following set of tools, to be able to work with local Kubernetes cluster:

- [docker](https://docs.docker.com/engine/install/) (on Windows use docker inside [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install))
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- [helm](https://helm.sh/docs/intro/install/)

## Bootstrap

Run the bootstrap with the following command:

```bash
bash bootstrap.sh
```

## Clean Up

Remove the cluster with the following command:

```bash
kind delete cluster --name local
```
