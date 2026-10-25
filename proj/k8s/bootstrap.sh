#!/usr/bin/env bash
set -euo pipefail
# Disable command tracing and core dumps to avoid exposing Secret data
set +x
ulimit -c 0

# Resolve paths from this script, regardless of the caller's working directory
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

# Require a private, regular .env file owned by the current user
if [[ ! -f .env || -L .env || ! -O .env || ! -r .env ]]; then
  printf 'Create a readable .env owned by your user from .env.example (no symlinks).\n' >&2
  exit 1
fi

# Support Linux and macOS stat; reject access by other users
if env_mode="$(stat -c '%a' .env 2>/dev/null)"; then
  :
else
  env_mode="$(stat -f '%Lp' .env)"
fi
if (( (8#$env_mode & 077) != 0 )); then
  printf '.env must be private. Run: chmod 600 .env\n' >&2
  exit 1
fi

# Validate one nonempty API_KEY entry without executing or printing its contents
# Comments and blank lines are allowed; quotes and shell expansion are not used
if ! awk '
  { sub(/\r$/, "") }
  /^[[:space:]]*(#|$)/ { next }
  /^API_KEY=[^[:space:]]+$/ {
    value = substr($0, 9)
    if (value ~ /^["\047]/) exit 1
    count++
    next
  }
  { exit 1 }
  END { if (count != 1) exit 1 }
' .env; then
  printf '.env must contain exactly one unquoted, nonempty API_KEY=value entry.\n' >&2
  exit 1
fi

# Target the local cluster explicitly for all Helm and kubectl operations
context="kind-local"

# Reuse the local kind cluster if it exists; otherwise create it
clusters="$(kind get clusters)"
if grep -Fxq 'local' <<< "$clusters"; then
  printf 'Reusing existing kind cluster local.\n'
else
  kind create cluster --config kind/local.yaml
fi

# Install Flux Operator
helm upgrade --install flux-operator \
  oci://ghcr.io/controlplaneio-fluxcd/charts/flux-operator \
  --kube-context "$context" \
  --version 0.61.0 \
  --namespace flux-system \
  --create-namespace \
  --wait

# Install Flux instance
helm upgrade --install flux-instance \
  oci://ghcr.io/controlplaneio-fluxcd/charts/flux-instance \
  --kube-context "$context" \
  --version 0.61.0 \
  --namespace flux-system \
  --set instance.cluster.size=small \
  --wait

# Wait for the operator to finish installing the Flux controllers
kubectl --context "$context" -n flux-system wait \
  --for=condition=Ready fluxinstance/flux \
  --timeout=3m

# Apply the Git source and root reconciliation for Flux CD
kubectl --context "$context" apply -f flux/

# Wait for Flux to create the namespace before creating the Secret
printf 'Waiting for namespace kagent in context %s...\n' "$context"
kubectl --context "$context" wait \
  --for=create namespace/kagent \
  --timeout=3m

# Let kubectl read .env as data, without sourcing it or exporting the key
# Pipe the Secret directly to the API without creating temporary credential files
# Server-side apply avoids storing another copy in a last-applied annotation
kubectl --context "$context" -n kagent create secret generic llm-ai-einfra \
  --from-env-file=.env \
  --dry-run=client -o yaml |
  kubectl --context "$context" -n kagent apply \
    --server-side --field-manager=kagent-secret-bootstrap -f -
