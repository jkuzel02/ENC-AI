# Local Kubernetes Cluster Development

This guide covers local development of the Kubernetes cluster using
[kind](https://kind.sigs.k8s.io/) (**K**ubernetes **in** **D**ocker) on both
**macOS** and **Ubuntu inside WSL2**.

The cluster runs Flux CD for GitOps reconciliation, Traefik Gateway for routing
`*.localhost` subdomains over HTTPS, Prometheus and Grafana for monitoring, and
Kagent (multi-agent AI for Kubernetes) with Grafana MCP integration.

Follow the setup section for your operating system:
- [macOS Setup](#macos-setup)
- [WSL2 (Ubuntu) Setup](#wsl2-ubuntu-setup)

Then proceed to the common steps:
- [Prepare the API Key](#prepare-the-api-key)
- [Bootstrap](#bootstrap)
- [Access Web Services & Applications](#access-web-services--applications)
- [Verify Readiness](#verify-readiness)
- [Suspending and Resuming (Save Resources)](#suspending-and-resuming-save-resources)
- [Clean Up](#clean-up)

---

## macOS Setup

### Requirements

On macOS, install the required development tools via [Homebrew](https://brew.sh/)
and use [Docker Desktop for Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
(or [OrbStack](https://orbstack.dev/)).

1. **Install tools via Homebrew:**

   ```bash
   brew install kind kubectl helm
   ```

2. **Start Docker Desktop:**
   Launch Docker Desktop from `/Applications` or via the terminal:

   ```bash
   open -a Docker
   ```

3. **Verify the tools and Docker daemon:**

   ```bash
   docker --version
   kind version
   kubectl version --client
   helm version --short
   ```

   Before bootstrapping, the Docker daemon must be running and responsive without
   elevated privileges:

   ```bash
   docker info
   ```

### macOS Networking & Port Availability

- The kind cluster binds host ports `80` and `443` on `127.0.0.1`. Ensure no
  other local web server (e.g. Apache, Nginx, Caddy) is currently listening on
  these ports:
  ```bash
  lsof -iTCP:80,443 -sTCP:LISTEN
  ```
- Domains ending in `*.localhost` (such as `kagent.localhost` and `grafana.localhost`)
  resolve automatically to `127.0.0.1` on macOS according to RFC 6761 without
  modifying `/etc/hosts`.

---

## WSL2 (Ubuntu) Setup

This section covers local development in **Ubuntu inside WSL2**.
Run the commands in a WSL Bash terminal, including when using VS Code connected
to WSL. The manual Docker steps below assume Docker Engine runs inside that WSL
distribution; they do not describe Docker Desktop integration or production use.

### Requirements

Install these tools inside WSL:

- [Docker Engine](https://docs.docker.com/engine/install/ubuntu/)
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- [Helm](https://helm.sh/docs/intro/install/)

The bootstrap needs network access to download container images, Helm charts,
and the Git source.

### Make user-installed tools available in Bash

If the tool binaries are installed into `~/.local/bin`, add this block to
`~/.bashrc`:

```bash
# User-installed development tools
case ":$PATH:" in
    *":$HOME/.local/bin:"*) ;;
    *) export PATH="$HOME/.local/bin:$PATH" ;;
esac
```

Load the change and verify the tools:

```bash
source ~/.bashrc
docker --version
kind version
kubectl version --client
helm version --short
```

`docker --version` checks only the client. Before bootstrapping, this must also
succeed **without sudo**:

```bash
docker info
```

### Start Docker Inside WSL

#### Docker installed as a systemd service

If your installation provides `docker.service` and WSL has systemd enabled:

```bash
sudo systemctl start docker
sudo systemctl status docker
```

See Microsoft's [WSL systemd guide](https://learn.microsoft.com/en-us/windows/wsl/systemd)
if systemd is unavailable. Enabling systemd does not install Docker's service.

#### Standalone binaries without docker.service

`Unit docker.service not found` means the service is missing. This can happen
when Docker was installed as standalone binaries in `~/.local/bin`.
`systemctl daemon-reload` does not create a missing service;
`systemctl daemon-reload docker` is invalid because `daemon-reload` takes no
service name.

For this local development setup, run the daemon directly. Ensure the Docker
archive's companion binaries (including `containerd`, `runc`, `docker-proxy`,
and `docker-init`) are also available in `~/.local/bin`.
See Docker's [binary installation guide](https://docs.docker.com/engine/install/binaries/).

If startup fails with `failed to create NAT chain DOCKER: iptables not found`,
install the missing dependency in Ubuntu:

```bash
sudo apt-get update
sudo apt-get install -y iptables
```

In **terminal 1**, start Docker:

```bash
sudo env PATH="$HOME/.local/bin:$PATH" "$HOME/.local/bin/dockerd"
```

Passing `PATH` explicitly lets the root daemon find the companion binaries.
Enter the sudo password in your own WSL terminal; typed characters are not
shown. When an assistant cannot accept interactive input, run this command in
your own terminal rather than sending a password through chat.

Wait for `API listen on /var/run/docker.sock`. Keep terminal 1 open and the
command running. Open **terminal 2** (the `+` button in VS Code's Terminal panel)
for the following commands. Pressing Ctrl+C in terminal 1 stops Docker; closing
the terminal can also stop it. A WSL shutdown stops the daemon and cluster.
Restart Docker before using the cluster again.

#### Docker socket permissions

If `docker info` reports `permission denied` for `/var/run/docker.sock`, the
daemon is running but your user lacks access. For the manually started daemon
in this local WSL setup, run in terminal 2:

```bash
sudo chgrp "$(id -gn)" /var/run/docker.sock
sudo chmod g+rw /var/run/docker.sock
docker info
```

This grants Docker access to your primary group. Docker socket access grants
root-level control inside the WSL distribution; use a group containing only
trusted users. The socket permissions may need to be set again after restarting
the daemon. For a service-based installation, follow Docker's
[Linux post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/)
for persistent group access.

If the socket is missing (`No such file or directory` or `cannot dereference`),
first check terminal 1: the daemon may have stopped or failed to start. Start it
and wait for the API message before changing socket permissions. Do not create
the socket manually.

---

## Prepare the API Key

From the repository root, create the private environment file only if it does
not already exist:

```bash
cd proj/k8s
(umask 077; cp -n .env.example .env)
chmod 600 .env
```

Edit `.env` locally and replace the example value with your actual API key:

```dotenv
API_KEY=your-api-key
```

The bootstrap requires a readable regular file owned by your user, with no
permissions for other users and no symlink. It accepts exactly one nonempty,
unquoted `API_KEY=value` entry, without whitespace in the value; comments and
blank lines are allowed. Do not use `export`, quotes, or shell expansion.
The bootstrap reads the file as data and creates the `llm-ai-einfra` Secret
in the `kagent` namespace.

The filename must be exactly `.env`. An editor-created file named `.env `
(with a trailing space) or `.env copy.example` will not be found. Check names
without printing the key:

```bash
ls -lb .env*
```

If you accidentally created `.env ` and `.env` does not exist, rename it:

```bash
mv -n -- '.env ' .env
chmod 600 .env
```

A missing or invalid `.env` stops the script before cluster creation or Helm
installation. `.env` is ignored by Git; never commit keys, copies of secret
files, or kubeconfig files.

---

## Bootstrap

From the repository root:

```bash
bash proj/k8s/bootstrap.sh
```

Or, if already in `proj/k8s`, run `bash bootstrap.sh`. The script resolves paths
relative to itself.

The script creates the kind cluster `local` using `kind/local.yaml`, or reuses
it if it already exists. It installs Flux Operator and Flux controllers,
applies the Git source and root reconciliation, waits for the `kagent`
namespace, and creates or updates the API key Secret. It targets the
`kind-local` context explicitly.

Creating a cluster directly with `kind create cluster --config kind/local.yaml`
(from `proj/k8s`) creates only Kubernetes; it does not replace the bootstrap.
If you already did that, run the bootstrap to finish the setup.

Flux reconciles the `main` branch of `https://github.com/jkuzel02/ENC-AI`.
Local manifest edits are not automatically deployed. A successful bootstrap
does not mean every application is ready: Flux continues installing applications
in dependency order afterward.

---

## Access Web Services & Applications

Traefik Gateway exposes services through TLS on port 443 with automatic redirection
from HTTP port 80. Certificates are issued by cert-manager using a local cluster
CA for `*.localhost`.

| Service | URL | Notes & Credentials |
| --- | --- | --- |
| **Kagent UI** | `https://kagent.localhost` | Web UI for the Kagent multi-agent AI system |
| **Grafana** | `https://grafana.localhost` | Cluster metrics & dashboards. User: `admin` |
| **Flux Dashboard** | `https://flux.localhost` | GitOps reconciliation status and controls |
| **Demo Apps** | `https://foo.localhost`<br>`https://bar.localhost` | Sample applications routing to demo deployments |

### Retrieve Grafana Admin Password

To retrieve the generated password for user `admin` in Grafana:

```bash
kubectl --context kind-local -n monitoring get secret monitoring-grafana -o jsonpath="{.data.admin-password}" | base64 --decode && echo ""
```

### Self-Signed Certificate Warning

Because certificates are issued by an in-cluster self-signed issuer, browsers
(Chrome, Safari, Edge) will show an `Untrusted Certificate` or `Not Secure` warning
on the first visit. Click **Advanced** and select **Proceed to localhost (unsafe)**
to open the web interface.

---

## Verify Readiness

```bash
kubectl --context kind-local get nodes
kubectl --context kind-local get pods -A
kubectl --context kind-local -n flux-system get gitrepositories,kustomizations,helmreleases
kubectl --context kind-local -n kagent get pods
```

The node should become `Ready`. During initial installation, pods can be
`ContainerCreating` and Flux resources can report dependencies that are not yet
ready. Repeat the checks as reconciliation progresses. For a resource that
remains unready, inspect its conditions and events, for example:

```bash
kubectl --context kind-local -n flux-system describe kustomization foundation
```

After fixing a prerequisite, rerun `bash proj/k8s/bootstrap.sh` from the
repository root; it reuses the existing cluster.

---

## Suspending and Resuming (Save Resources)

When not actively developing, you can put the cluster to sleep without losing any
state, downloaded container images, or certificates:

1. **Pause / Stop the cluster container:**
   ```bash
   docker stop local-control-plane
   ```
2. **Quit Docker Desktop:**
   This frees up all RAM and CPU allocated to Docker on your machine.

3. **Resume later:**
   Start Docker Desktop and run:
   ```bash
   docker start local-control-plane
   ```
   All pods and web interfaces will be back up and running within 15–30 seconds.

---

## Clean Up

With Docker still running, permanently remove the local cluster:

```bash
kind delete cluster --name local
```

For the manually started Docker daemon in WSL, stop it with Ctrl+C in terminal 1
when you no longer need it.
