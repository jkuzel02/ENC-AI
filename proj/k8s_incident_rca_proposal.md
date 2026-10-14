# Evaluating Single-Agent and Multi-Agent LLM Systems for Kubernetes Incident Diagnosis

## Project summary

The project investigates whether a **multi-agent large language model (LLM) system** can diagnose Kubernetes incidents more accurately and reliably than a **single-agent LLM**. We will build a reproducible Kubernetes test environment, inject known failures, collect relevant observability data, and compare different AI approaches on the same incident snapshots.

Rather than building a production-ready Kubernetes assistant, the primary objective is an **experimental comparison of AI architectures and prompting strategies**.

## Research question

> Does separating Kubernetes incident analysis into specialized LLM agents improve root-cause identification, evidence quality, or reliability compared with a well-prompted single-agent LLM, and at what cost in latency and model usage?

### Hypotheses

- **H1:** A multi-agent pipeline may improve diagnostic accuracy on incidents that require combining metrics, events, and logs.
- **H2:** A carefully prompted single agent may perform similarly on straightforward incidents, with lower latency and model usage.
- **H3:** Requiring evidence citations and a structured diagnosis may reduce unsupported conclusions across both architectures.

These are hypotheses to test, **not expected conclusions**.

## Proposed approaches

All approaches receive the **same frozen incident evidence snapshot**, use the same base model where possible, and produce a common structured output.

1. **Baseline A — Single agent, basic prompt:** One LLM call analyzes the evidence and reports the likely root cause.
2. **Baseline B — Single agent, engineered prompt:** One LLM call with explicit evidence requirements, uncertainty guidance, and a structured diagnosis schema.
3. **Experimental C — Multi-agent pipeline:**
   - **Metrics agent:** Examines CPU, memory, restarts, and time-series signals.
   - **Logs/events agent:** Examines application logs, Kubernetes events, and workload states.
   - **Diagnosis agent:** Consolidates the two analyses into a diagnosis, supporting evidence, uncertainties, and next steps.

A simple Python orchestrator is sufficient; a complex agent framework is optional.

## Technical architecture

```text
                  Local Kubernetes test cluster (kind / minikube)
                 ┌─────────────────────────────────────────────┐
                 │ Demo apps + controlled failure scenarios    │
                 │ Kubernetes API: pods, conditions, events    │
                 │ Prometheus: CPU, RAM, throttling, restarts  │
                 │ Grafana: incident dashboards                │
                 └────────────────────┬────────────────────────┘
                                      │
                            Python evidence collector
                                      │
                          Versioned JSON incident snapshots
                                      │
                      ┌───────────────┼────────────────────┐
                      │               │                    │
                 Basic single    Engineered single     Multi-agent
                    agent            agent              pipeline
                      │               │                    │
                      └───────────────┼────────────────────┘
                                      │
                        Standardized JSON diagnoses
                                      │
                           Benchmark & evaluation
                     accuracy / evidence / time / cost
```

### Infrastructure to deploy

| Component | Proposed technology | Role |
|---|---|---|
| Kubernetes | `kind` or `minikube` | Isolated cluster for reproducible incidents |
| Monitoring | Prometheus, deployed via `kube-prometheus-stack` Helm chart | Historical cluster and workload metrics |
| Metrics exporters | kube-state-metrics, kubelet/cAdvisor | Workload states, resource usage, throttling |
| Visualization | Grafana (from the monitoring stack) | Visual inspection and presentation of incidents |
| Workloads | Small demo API, nginx, optionally a database | Realistic failure scenarios |
| AI application | Python | Data collection, LLM orchestration, evaluation |
| LLM provider | e-INFRA AI service, subject to available API/model access | Model inference for all experimental variants |

**Scope choice:** Run the Python experimentation tool outside Kubernetes initially. The infrastructure runs the workloads and monitoring; the AI code can remain a local CLI application.

## Using chat.ai.e-infra.cz

We have access to **https://chat.ai.e-infra.cz/**, which may be useful for model inference and interactive prototyping.

Before implementation, confirm:

- Whether the service provides **programmatic API access**, rather than only a chat interface.
- Which models are available and whether a stable model can be selected for repeatable experiments.
- Authentication mechanism, quotas/rate limits, context-window limits, and usage reporting.
- Whether its terms and data-handling rules permit submitting sanitized synthetic Kubernetes logs and incident snapshots.

**Important:** Access to the chat website alone does **not** guarantee a compatible API. Do not assume OpenAI-compatible endpoints or specific models until verified.

If a usable API is unavailable, alternatives include a permitted institution-provided inference endpoint, an OpenAI API account, or a local model. The same model should be used for all compared approaches; if models differ, that limitation must be documented.

## Failure scenarios and dataset

Start with **three** scenarios for the minimum viable project; expand to **six** if time permits.

| Incident | Ground-truth cause | Useful signals |
|---|---|---|
| OOMKilled | Container exceeds memory limit | Termination reason, memory usage, restarts |
| CrashLoopBackOff | Application crashes at startup | Previous logs, container exit code, Pod state |
| ImagePullBackOff | Invalid/inaccessible container image | Image-pull events, Pod state |
| CPU throttling | CPU limit constrains a busy workload | CPU usage and throttling counters |
| Readiness failure | Probe fails despite running container | Probe events, readiness condition, application logs |
| Database unreachable | App cannot connect to required service | Connection errors, Service/endpoint status |

For each scenario:

1. Deploy a known configuration and inject one controlled failure.
2. Record the **ground truth** (cause, trigger, expected diagnostic evidence).
3. Collect a bounded observation window of Kubernetes events/statuses, logs, and Prometheus metrics.
4. Save an immutable, sanitized JSON snapshot with a scenario ID and timestamp range.
5. Re-run each diagnostic approach against that **same** snapshot.

Avoid answer leakage in evidence metadata (for example, do not provide a field named `root_cause` as input to the model). Keep ground-truth labels in a separate evaluation file.

## Core components to implement

### 1. Scenario runner

YAML manifests and lightweight scripts that deploy, trigger, and reset test incidents. Provide deterministic steps, timeouts, and cleanup.

### 2. Evidence collector

A Python program using the Kubernetes client and Prometheus HTTP API to capture:

- Pod status, conditions, restarts, exit codes.
- Recent warning events and container logs.
- CPU and memory time series; throttling and restart metrics where available.
- Context such as namespace, workload name, and collection window.

Use bounded query windows and preserve metric units. Normalize everything to a documented JSON schema.

### 3. LLM approaches

Implement all three approaches with shared model configuration and a common output structure:

```json
{
  "incident_id": "INC-001",
  "root_cause_category": "oom_killed",
  "explanation": "...",
  "supporting_evidence": ["..."],
  "uncertainties": ["..."],
  "recommended_checks": ["..."]
}
```

Agent prompts should cite evidence present in the input, distinguish observations from hypotheses, and avoid unsupported certainty.

### 4. Evaluation runner

Run all approaches over the same incidents, saving model responses, errors, timings, and token usage **when available**.

## Evaluation methodology

| Measure | Method |
|---|---|
| Root-cause accuracy | Compare predicted root-cause category with labeled ground truth |
| Evidence support | Manually or systematically check whether referenced evidence exists in the snapshot |
| Unsupported claims | Count important claims that are not supported by the snapshot |
| Latency | Measure end-to-end response time |
| Token usage | Record input/output tokens if exposed by the provider |
| Cost | Estimate from published pricing only when applicable; otherwise report model calls/tokens |

Use consistent incident evidence, base model, temperature/configuration (where controllable), and output schema. Prefer multiple runs per scenario and variants of each failure to avoid drawing conclusions from a handful of examples. Report uncertainty and failures, not only successful demo cases.

An additional analysis can compare **basic vs. engineered prompts** to determine whether multi-agent orchestration offers benefits beyond prompt engineering alone.

## Minimum viable deliverable (MVP)

- [ ] Working local Kubernetes test cluster.
- [ ] Prometheus capturing relevant resource/workload metrics.
- [ ] Grafana dashboard for demonstrating incidents.
- [ ] At least three repeatable incident scenarios with ground truth.
- [ ] Evidence snapshots collected and sanitized automatically.
- [ ] Two single-agent baselines implemented.
- [ ] Three-role multi-agent pipeline implemented.
- [ ] Benchmark results comparing accuracy, evidence support, latency, and usage.
- [ ] Reproducible setup guide, limitations, and short demonstration.

## Optional extensions (not required)

- Expand from three to six or more incident scenarios.
- Add application traces or Loki-based historical log collection.
- Add tool calling, so agents request more evidence on demand, and compare it with fixed-snapshot analysis.
- Add a simple results dashboard or Grafana annotations for detected incidents.
- Test a second model for robustness, while keeping model comparisons separate from architecture comparisons.

**Explicitly out of scope:** autonomous remediation, production cluster access, a custom-trained LLM, a full MCP server, complex RAG infrastructure, or a production-grade frontend.

## Suggested implementation phases

| Phase | Work | Deliverable |
|---|---|---|
| 1. Infrastructure | kind/minikube, Helm monitoring, demo app | Healthy cluster + Grafana dashboard |
| 2. Reproducible incidents | Three failure scenarios + ground truth | Scenario scripts and labels |
| 3. Evidence collection | Kubernetes and Prometheus API integration | Frozen incident JSON snapshots |
| 4. AI baselines | Basic and engineered single-agent prompts | Comparable structured diagnoses |
| 5. Multi-agent system | Specialized agents and coordinator | Multi-agent diagnoses |
| 6. Experiments | Repeat trials, score outputs, analyze results | Tables, figures, discussion |
| 7. Delivery | Tests, README, report, demo | Reproducible project repository |

The sequence matters more than rigid week estimates. Build a working single-agent baseline before adding orchestration complexity.

## Risks and mitigations

- **Too much infrastructure work:** Use `kube-prometheus-stack` and keep the AI system as a local Python CLI.
- **Limited hardware:** Start with lightweight workloads and retention settings; don't require a local LLM.
- **LLM API unavailable:** Verify e-INFRA programmatic access early and define a fallback provider.
- **Small or trivial dataset:** Add incident variants and ambiguous evidence to distinguish the approaches.
- **Unfair evaluation:** Freeze input snapshots and keep model/configuration as similar as possible across approaches.
- **Sensitive data:** Use a disposable test cluster; redact tokens, secrets, usernames, and unnecessary identifying details before transmission. Never commit API credentials.
- **Multi-agent overhead:** Report latency and usage, including cases where the single agent is better.

## Expected outcome

A reproducible experiment and open-source codebase showing **when (if ever) specialized LLM agents help with Kubernetes root-cause diagnosis**. The result may favor the multi-agent approach, a well-engineered single agent, or different methods for different classes of incident. All are valid outcomes when supported by transparent evaluation.

## Short proposal abstract

> This project evaluates the effectiveness of single-agent and multi-agent large language model architectures for diagnosing incidents in Kubernetes environments. A controlled Kubernetes cluster will be monitored using Prometheus and Grafana, while reproducible failure scenarios will provide labeled diagnostic cases. An evidence collector will combine Kubernetes events, logs, workload status, and metrics into standardized incident snapshots. We will implement a basic single-agent baseline, an enhanced prompt-engineered single agent, and a multi-agent system with specialized metrics, logs, and diagnosis roles. All approaches will be evaluated on identical evidence using root-cause accuracy, quality of supporting evidence, response latency, and model usage. The project aims to determine whether multi-agent decomposition provides measurable benefits over simpler prompting strategies, rather than assuming that increased architectural complexity automatically improves results.
