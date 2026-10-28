# Local Kubernetes Cluster

Create a locally running Kubernetes cluster with [kind]((https://kind.sigs.k8s.io)) (**K**ubernetes **in** **D**ocker).

## Requirements

We want to have installed the following set of tools, to be able to work with local Kubernetes cluster:

- [docker](https://docs.docker.com/engine/install/) (on Windows use docker inside [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install))
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- [helm](https://helm.sh/docs/intro/install/)

### Make user-installed tools available in Bash

If you install tool binaries into `~/.local/bin` on Linux or WSL, add the
following block to `~/.bashrc` so new Bash terminals can find them:

```bash
# User-installed development tools
case ":$PATH:" in
    *":$HOME/.local/bin:"*) ;;
    *) export PATH="$HOME/.local/bin:$PATH" ;;
esac
```

Load the change in your current terminal:

```bash
source ~/.bashrc
```

Verify that the tools are available:

```bash
docker --version
kind version
kubectl version --client
helm version --short
```

Docker also needs a running daemon accessible to your user. Check it with
`docker info` before running the bootstrap; adding binaries to `PATH` does
not start the daemon.

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
