# Codex Master Prompt — Implement Kubernetes Multi-Agent Root Cause Analysis

You are responsible for implementing the complete **Multi-Agent AI for Kubernetes Root Cause Analysis** project described in the repository's `AGENTS.md`.

Your objective is to deliver a fully functional, reproducible, well-tested research prototype that can be deployed, executed, evaluated, and demonstrated on a local development machine.

**Do not stop after scaffolding, creating documentation, or implementing a proof of concept. Complete the implementation and verify it to the greatest extent supported by the available execution environment.**

## 1. Source of truth

Before doing anything:

1. Read `AGENTS.md` in its entirety.
2. Inspect the existing repository, including its source code, tests, configuration, and documentation.
3. Extract all functional requirements, non-functional requirements, research objectives, assumptions, and deliverables.
4. Create a traceable implementation plan connecting each requirement to its implementation and corresponding tests.

Treat `AGENTS.md` as the primary project specification.

This prompt defines additional engineering, testing, documentation, and execution requirements. If a conflict exists, preserve the research objectives from `AGENTS.md` while following the stricter testing and safety requirements.

Do not silently omit requirements.

## 2. Mandatory multi-agent development approach

Use a multi-agent software development workflow.

If the Codex environment supports spawning specialized sub-agents, delegate work to them and coordinate their results. If parallel sub-agents are unavailable, execute the same specialized roles sequentially with explicit reviews and independent verification.

Use these roles:

### Agent A — Architect and Research Lead

Responsibilities:

- Analyze `AGENTS.md`.
- Design the complete system architecture.
- Define interfaces between modules.
- Specify experiment methodology and fairness requirements.
- Define JSON schemas for incident snapshots, agent observations, diagnoses, and evaluation results.
- Identify implementation risks and architectural inconsistencies.
- Review completed components against research objectives.

Deliverable: `docs/ARCHITECTURE.md`.

### Agent B — Kubernetes and Observability Engineer

Responsibilities:

- Implement local Kubernetes infrastructure using kind.
- Provide Helm-based installation of Prometheus and Grafana using `kube-prometheus-stack`.
- Implement Kubernetes manifests for demo applications.
- Implement reproducible failure scenarios.
- Configure monitoring and required metrics.
- Provide reliable cluster setup and cleanup scripts.
- Verify resource collection and Kubernetes API connectivity.

Deliverable: working local infrastructure with automated validation.

### Agent C — Python Backend and Data Engineer

Responsibilities:

- Implement Kubernetes data collection.
- Implement Prometheus HTTP API integration.
- Implement immutable incident evidence snapshots.
- Implement input validation, error handling, redaction, and deterministic data processing.
- Provide testable interfaces suitable for mocked and real infrastructure.

Deliverable: evidence collection subsystem with unit and integration tests.

### Agent D — AI and Multi-Agent Systems Engineer

Responsibilities:

- Implement the AI inference provider abstraction.
- Support an OpenAI-compatible inference endpoint when available.
- Investigate compatibility with `chat.ai.e-infra.cz` through user-provided API configuration or available documentation.
- Implement the three experimental diagnostic approaches.
- Implement agent orchestration and structured outputs.
- Design prompts that require evidence-based diagnosis.
- Handle model errors, malformed output, retries, and timeouts.

Deliverable: functioning AI diagnosis subsystem.

### Agent E — Testing and Evaluation Engineer

Responsibilities:

- Establish the test strategy before implementation.
- Implement automated unit, integration, and end-to-end tests.
- Build the experiment runner.
- Implement evaluation metrics and statistical summaries.
- Validate experiment reproducibility.
- Check that baseline comparisons are fair.
- Verify that results are not fabricated or hardcoded.

Deliverable: automated testing and experimental evaluation framework.

### Agent F — Documentation and Quality Reviewer

Responsibilities:

- Review code quality, maintainability, and security.
- Validate the setup instructions against actual commands.
- Create beginner-friendly local deployment documentation.
- Document configuration, experiments, troubleshooting, and cleanup.
- Review project completeness against `AGENTS.md`.
- Identify missing tests and unsupported claims.

Deliverable: complete, verified documentation.

### Coordination requirements

- The lead agent owns architectural consistency and final integration.
- Agree on schemas and module interfaces before parallel implementation.
- Use clearly separated files or modules to minimize conflicting edits.
- Require independent review of security-sensitive code, AI evaluation logic, and experiment methodology.
- Integrate contributions incrementally.
- Do not mark a component complete until its relevant tests pass.
- Record important architectural decisions in `docs/DECISIONS.md`.
- Do not claim that sub-agents were used if the environment does not actually support them.

## 3. Mandatory development methodology: tests first

Follow strict test-driven development.

**For every functional component, write the tests before implementing its production logic.**

Use the following cycle:

1. Identify expected behavior.
2. Define public interfaces.
3. Write tests that describe the behavior.
4. Run the tests and confirm that they fail for the expected reason.
5. Implement the minimum production code necessary.
6. Run the tests again.
7. Refactor without changing behavior.
8. Run regression tests.
9. Continue to the next requirement.

Tests must assert meaningful behavior, not just successful imports or object creation.

Do not write tests that merely reproduce existing implementation details.

Do not use hardcoded expected answers in AI implementations.

Do not modify tests simply to hide implementation defects.

If a test expectation is genuinely incorrect, document the reason for changing it.

### Required testing layers

**Unit tests**

- Kubernetes resource parsing.
- Prometheus response parsing.
- Incident snapshot generation.
- Snapshot validation.
- Sensitive-data redaction.
- Prompt construction.
- Agent orchestration.
- Structured-output parsing.
- Root-cause classification.
- Evaluation metrics.
- Cost and token accounting.
- Configuration validation.

**Integration tests**

- Kubernetes client against a disposable test cluster when available.
- Prometheus querying against a running instance.
- Evidence collection using realistic fixtures.
- AI inference using mocked provider responses.
- Agent pipeline execution using recorded incident snapshots.

**End-to-end tests**

- Deploy a test workload.
- Trigger a controlled failure.
- Collect relevant evidence.
- Execute the diagnosis pipeline.
- Validate the diagnosis schema.
- Record and score the result.

Real infrastructure tests should use explicit markers so that ordinary unit tests can run without Docker, Kubernetes, or paid API access.

### Testing requirements

Use:

- `pytest`
- `pytest-cov`
- `pytest-mock` or equivalent mocking utilities
- `ruff`
- Python type checking with `mypy` or `pyright`

Target at least 85% coverage of core Python logic, while prioritizing meaningful test quality over a coverage number.

All tests must be independently repeatable.

Randomized behavior must use explicit seeds when applicable.

## 4. Technology stack

Prefer the following technologies unless `AGENTS.md` specifies otherwise:

| Component | Technology |
|---|---|
| Programming language | Python 3.12 |
| Local Kubernetes | kind |
| Containers | Docker |
| Kubernetes deployment | Helm |
| Monitoring | Prometheus |
| Dashboards | Grafana |
| Monitoring stack | kube-prometheus-stack |
| Kubernetes integration | Official Kubernetes Python client |
| Metrics integration | Prometheus HTTP API |
| LLM inference | OpenAI-compatible Python client |
| AI orchestration | Python with explicit agent interfaces |
| Configuration | YAML and environment variables |
| Data models | Pydantic |
| Testing | pytest |
| Linting | Ruff |
| Type checking | mypy or pyright |
| Automation | Makefile and Bash |

Avoid adding unnecessary infrastructure or frameworks.

In particular, do not introduce MCP, vector databases, Kubernetes Operators, or distributed messaging unless a concrete requirement makes them necessary.

Prefer standard Python orchestration over LangGraph unless LangGraph materially simplifies the implementation.

## 5. Implement the local Kubernetes environment

Provide a reproducible local Kubernetes setup.

Required components:

- kind cluster.
- A dedicated namespace for demo applications.
- Prometheus.
- Grafana.
- kube-state-metrics.
- Metrics needed for container CPU, memory, restarts, and health.
- Test applications capable of generating controlled failures.

Use Helm configuration appropriate for a laptop or desktop computer.

Document recommended CPU, RAM, and disk requirements.

### Required deployment scripts

Implement commands equivalent to:

```bash
make setup
make deploy-monitoring
make deploy-demo
make verify-infrastructure
make destroy
```

Commands must be documented, idempotent where practical, and safe to rerun.

The destroy command must clearly identify which project-specific resources it will remove. Never delete an unrelated Kubernetes cluster.

### Monitoring requirements

Grafana must include useful dashboards covering:

- CPU usage.
- Memory usage.
- Pod restarts.
- Pod/container health.
- Incident-related metrics.
- Monitoring of test workloads.

Provision dashboards automatically when practical.

Validate that the Prometheus queries used by the evidence collector are available in the deployed monitoring configuration.

Do not assume a metric exists without verifying its exporter and labels.

## 6. Implement reproducible incident scenarios

Implement at least these six scenarios:

1. Container terminated because of OOM.
2. Application experiencing CrashLoopBackOff.
3. Container image retrieval failure.
4. CPU throttling caused by resource limits.
5. Readiness probe failure.
6. Application unable to reach a required database service.

Each scenario must contain:

- Kubernetes manifests.
- A setup or trigger procedure.
- A way to identify the affected resources.
- Expected observable symptoms.
- Known ground-truth root cause.
- Data collection instructions.
- Validation tests.
- Cleanup procedure.

Make each scenario deterministic where practical.

Use dedicated namespaces and uniquely identified resources to prevent interference.

Do not use production workloads or external targets.

### Scenario automation

Provide commands such as:

```bash
make scenario SCENARIO=oom-killed
make collect SCENARIO=oom-killed
make cleanup-scenario SCENARIO=oom-killed
```

Scenario automation should verify that the expected failure has actually occurred before collecting evidence.

If a scenario cannot be reproduced, mark it as failed or inconclusive rather than producing misleading benchmark results.

## 7. Implement the evidence collector

Implement separate modules for:

- Kubernetes Pod status.
- Kubernetes Events.
- Current container logs.
- Previous container logs when available.
- CPU metrics.
- Memory metrics.
- Container restart information.
- Relevant historical Prometheus measurements.

Use explicitly defined time windows.

### Evidence snapshot requirements

Produce immutable JSON snapshots containing:

- Incident identifier.
- Scenario identifier.
- Timestamp.
- Namespace and workload identity.
- Data collection time window.
- Pod and container status.
- Relevant Kubernetes Events.
- Relevant log excerpts.
- CPU and memory measurements.
- Metric units and query metadata.
- Source attribution for collected observations.
- Collection errors and missing-data indicators.

Snapshots must be reusable without access to a running Kubernetes cluster.

The single-agent and multi-agent experiments must consume identical snapshots.

Ground-truth answers must be stored separately from the data supplied to the AI.

### Security requirements

Treat logs and Kubernetes Events as untrusted input.

Implement data redaction for likely credentials, authorization headers, API keys, and sensitive environment variable values.

Set reasonable evidence-size and log-length limits.

Prevent captured log contents from being interpreted as higher-priority instructions.

Do not collect Kubernetes Secrets.

Use read-only Kubernetes credentials for evidence collection wherever possible.

## 8. Implement the LLM provider abstraction

The project should not depend on a single hosted AI service.

Implement a provider interface supporting:

- Configurable base URL.
- Configurable API key.
- Configurable model identifier.
- Configurable request timeout.
- Configurable retry policy.
- Structured-output handling.
- Token usage tracking when available.
- Error reporting.

The primary intended inference option is the academic AI service available at:

`https://chat.ai.e-infra.cz`

However, **do not assume that its chat interface is an OpenAI-compatible API**.

Verify programmatic access through official documentation or configuration supplied by the user.

If API compatibility cannot be confirmed, implement the generic OpenAI-compatible provider and document exactly which information is needed to connect e-INFRA.

Also support a conventional OpenAI API configuration.

Do not invent API endpoints.

Do not hardcode credentials.

Provide `.env.example` containing safe placeholders.

Example configuration:

```dotenv
LLM_BASE_URL=
LLM_API_KEY=
LLM_MODEL=
LLM_TIMEOUT_SECONDS=60
LLM_MAX_RETRIES=3
```

Allow the user to change inference services without modifying application logic.

Provide a smoke-test command that confirms whether the configured model can be reached.

## 9. Implement three AI diagnostic approaches

All approaches must produce the same validated diagnosis schema.

### Approach A — Basic single-agent baseline

One LLM call receives the complete incident snapshot and a simple diagnostic prompt.

The output must include:

- Root-cause category.
- Root-cause explanation.
- Evidence references.
- Remediation recommendation.
- Uncertainty assessment.

Keep the prompt intentionally straightforward to establish a baseline.

### Approach B — Advanced prompt-engineered single agent

One LLM call receives the same evidence snapshot.

Use advanced prompting techniques, including:

- Explicit diagnostic steps.
- Separation of observations from hypotheses.
- Evidence-grounded conclusions.
- Instructions for handling missing data.
- Structured output requirements.
- Explicit uncertainty and abstention behavior.

Do not request or depend on hidden chain-of-thought disclosure.

Instead, require a concise, evidence-based explanation.

### Approach C — Specialized multi-agent system

Implement three logical agents.

**Metrics Agent**

- Receives relevant metrics.
- Identifies suspicious changes.
- Produces structured observations.
- Clearly distinguishes observation from inference.

**Logs and Events Agent**

- Receives logs, Events, and Kubernetes state.
- Identifies diagnostic patterns.
- Produces structured observations.
- References evidence supporting its conclusions.

**Diagnosis Agent**

- Receives the outputs of the specialist agents.
- Combines their findings.
- Identifies the most likely root cause.
- Resolves conflicting observations where possible.
- Produces the same diagnosis schema as the single-agent systems.
- Explicitly acknowledges uncertainty where evidence is insufficient.

Implement real orchestration with separate model calls and typed message passing.

Do not implement the multi-agent architecture as a single prompt pretending that multiple agents exist.

Allow independent execution of specialist agents where supported.

Handle individual agent failure gracefully.

### Experiment fairness

For all three approaches:

- Use the same model family and model version when possible.
- Use exactly the same source incident snapshots.
- Keep the output schema identical.
- Keep temperature and model parameters consistent where supported.
- Record prompt versions.
- Record token consumption and latency.
- Do not expose ground-truth labels to the AI.
- Separate development/tuning scenarios from held-out evaluation scenarios.
- Record the number of LLM calls and effective context volume per approach.

Document that the multi-agent approach naturally uses more LLM calls and potentially more tokens.

Do not artificially force identical token counts if that would fundamentally change the architectures; instead, measure and report their resource differences.

## 10. Implement an automated evaluation framework

The experiment framework must allow us to compare the three diagnostic approaches objectively.

### Required metrics

Implement:

- Exact-match root-cause category accuracy.
- Per-scenario accuracy.
- Macro-averaged precision, recall, and F1 when applicable.
- Evidence-reference validity.
- Unsupported-claim detection where objectively possible.
- Response latency.
- Token consumption.
- Estimated inference cost when pricing data is configured.
- Failure and abstention rates.

Do not claim that automated scoring can perfectly determine semantic correctness or hallucinations.

Use manual review or clearly identified heuristic/LLM-assisted scoring for subjective criteria.

For LLM-based evaluation, keep the evaluator independent of the system being evaluated and document its limitations.

### Repeated experiments

Support running multiple trials per incident and architecture.

Example:

```bash
make benchmark RUNS=5
```

Store each result independently.

Record:

- Model identifier.
- Prompt version.
- Incident snapshot version.
- Timestamp.
- Diagnostic approach.
- Trial identifier.
- Raw model output.
- Parsed diagnosis.
- Token usage.
- Latency.
- Error status.

Provide aggregated results as JSON and CSV.

### Visualizations

Generate at least:

- Accuracy comparison chart.
- Latency comparison chart.
- Token usage comparison chart.
- Per-scenario comparison chart.

Use Python and Matplotlib.

Generate a Markdown evaluation report summarizing the experimental findings.

**Never fabricate benchmark results.**

If no real experiments have been executed, generate clearly labeled sample fixtures for testing only, not research conclusions.

## 11. CLI and developer experience

Provide a clear command-line interface supporting operations equivalent to:

```bash
python -m k8s_ai_rca collect --scenario oom-killed

python -m k8s_ai_rca diagnose \
  --incident datasets/incidents/example.json \
  --approach single-basic

python -m k8s_ai_rca diagnose \
  --incident datasets/incidents/example.json \
  --approach single-advanced

python -m k8s_ai_rca diagnose \
  --incident datasets/incidents/example.json \
  --approach multi-agent

python -m k8s_ai_rca benchmark \
  --dataset datasets/incidents \
  --runs 5
```

The exact CLI design may differ, but these operations must be supported and documented.

Provide helpful validation errors for missing configuration, unavailable clusters, unsupported model options, and malformed incident files.

## 12. Local machine documentation

Create comprehensive documentation for someone who has never run this repository before.

Required files:

**`README.md`**

- Project description.
- Research objectives.
- Architecture overview.
- Features.
- Technology stack.
- Quick start.
- Expected output.
- Links to detailed documentation.

**`docs/LOCAL_SETUP.md`**

- Hardware recommendations.
- Supported operating systems.
- Docker installation prerequisites.
- kind installation.
- kubectl installation.
- Helm installation.
- Python environment setup.
- Cluster creation.
- Prometheus installation.
- Grafana installation.
- Dashboard access and port-forwarding.
- AI provider configuration.
- Demo application deployment.
- Evidence collection.
- Running AI diagnosis.
- Running experiments.
- Viewing results.
- Infrastructure cleanup.

**`docs/ARCHITECTURE.md`**

- Component architecture.
- Data flow.
- Agent responsibilities.
- API interfaces.
- Evidence schema.
- Deployment topology.
- Security boundaries.

**`docs/EXPERIMENTS.md`**

- Research questions.
- Hypotheses.
- Experimental variables.
- Baseline designs.
- Dataset construction.
- Ground-truth methodology.
- Evaluation metrics.
- Repeated-trial methodology.
- Known limitations.
- Instructions for reproducing results.

**`docs/SCENARIOS.md`**

- All incident scenarios.
- Setup and trigger procedure.
- Expected failure.
- Expected evidence.
- Ground truth.
- Cleanup.

**`docs/TROUBLESHOOTING.md`**

Include common problems:

- Docker unavailable.
- kind cluster creation failure.
- Insufficient RAM.
- Prometheus not ready.
- Prometheus query returns no data.
- Grafana inaccessible.
- Missing Kubernetes metrics.
- AI API authentication failure.
- e-INFRA compatibility issues.
- Malformed model responses.
- Scenario does not reproduce.
- Benchmark interrupted.
- Environment cleanup failure.

**`docs/DECISIONS.md`**

Record architectural decisions and their rationale.

**`docs/TESTING.md`**

- Test layout.
- Running unit tests.
- Running integration tests.
- Running end-to-end tests.
- Coverage.
- Mocked provider behavior.
- CI checks.

Documentation must use commands that actually exist in the repository.

Do not document imaginary features.

## 13. Automation and CI

Implement a Makefile with discoverable commands.

At minimum:

```bash
make help
make install
make test
make test-unit
make test-integration
make lint
make typecheck
make setup
make deploy-monitoring
make deploy-demo
make verify-infrastructure
make scenario SCENARIO=oom-killed
make collect SCENARIO=oom-killed
make diagnose
make benchmark
make clean
make destroy
```

Add GitHub Actions workflows for:

- Python unit tests.
- Ruff linting.
- Type checking.
- Test coverage.

Do not require paid API access or a running Kubernetes cluster for the default CI workflow.

Use mocked providers and recorded fixtures for CI tests.

Real API and Kubernetes tests must be separately selectable.

## 14. Security and operational safety

This project will intentionally create failing workloads.

Therefore:

- Clearly distinguish the disposable test cluster from production environments.
- Refuse destructive scenario operations unless the target cluster matches the project-owned configuration.
- Never automatically remediate production resources.
- Never execute arbitrary shell commands generated by an LLM.
- Use minimum Kubernetes RBAC permissions.
- Do not send secrets to hosted AI providers.
- Keep credentials out of Git.
- Ensure `.env` is ignored by Git.
- Document any telemetry or external API calls.
- Add timeouts to potentially blocking operations.
- Keep infrastructure resource consumption reasonable.
- Do not expose Grafana or Prometheus publicly by default.

## 15. Implementation phases

Execute the work in this order.

### Phase 0 — Analysis and planning

- Read `AGENTS.md`.
- Inspect the repository.
- Identify requirements.
- Define architecture.
- Define schemas.
- Write implementation plan.
- Assign specialized agents.

### Phase 1 — Test foundation

- Set up Python packaging.
- Configure pytest.
- Configure Ruff and type checking.
- Implement test fixtures and interfaces.
- Write initial failing tests.

### Phase 2 — Infrastructure

- Implement kind setup.
- Deploy monitoring.
- Deploy demo applications.
- Validate observability.
- Write and execute infrastructure tests.

### Phase 3 — Incident scenarios

- Implement reproducible failure injection.
- Validate failure conditions.
- Implement ground-truth manifests.
- Write scenario tests.

### Phase 4 — Evidence collection

- Write collector tests first.
- Implement Kubernetes collector.
- Implement Prometheus collector.
- Implement immutable snapshots.
- Implement redaction.
- Validate against real and mocked data.

### Phase 5 — AI systems

- Write provider and orchestration tests first.
- Implement configurable model provider.
- Implement basic single agent.
- Implement advanced single agent.
- Implement specialized multi-agent architecture.
- Verify consistent output schemas.

### Phase 6 — Benchmarking

- Write scoring tests first.
- Implement experiment runner.
- Implement repeated trials.
- Implement evaluation metrics.
- Implement result export.
- Implement comparison visualizations.

### Phase 7 — Integration and validation

- Run all unit tests.
- Run static checks.
- Run integration tests where infrastructure is available.
- Run end-to-end scenarios.
- Verify the benchmark.
- Fix defects.
- Review research validity.

### Phase 8 — Documentation and final review

- Complete all documentation.
- Verify command examples.
- Review security.
- Review code maintainability.
- Update requirement traceability.
- Produce a final implementation summary.

## 16. Completion criteria

The project is complete only when:

- All required components from `AGENTS.md` have been implemented or explicitly documented as blocked.
- The local Kubernetes environment can be created using the provided instructions.
- Prometheus collects the metrics used by the application.
- Grafana can visualize the deployed workloads.
- At least six incident scenarios can be triggered and validated.
- Evidence snapshots can be collected and replayed offline.
- All three AI diagnostic approaches execute using the same snapshot schema.
- The multi-agent approach makes separate, real agent calls.
- Evaluation metrics can be computed automatically.
- Benchmarks can be repeated.
- Results can be exported and visualized.
- Unit tests and static checks pass.
- Real integration tests have been executed wherever the environment permits.
- The project contains sufficient documentation for a new developer to run it.

If external access, API credentials, system resources, or permissions prevent validation, document the limitation precisely and provide the commands required to finish that validation.

Do not report blocked tests as passed.

## 17. Working rules

- Begin by inspecting the repository and writing the implementation plan.
- Use specialized sub-agents where available.
- Apply test-driven development for every functional module.
- Commit logical milestones when Git access and permissions permit.
- Maintain a task checklist and update it as work progresses.
- Avoid large speculative abstractions.
- Prefer clear, typed, maintainable Python.
- Use realistic fixtures.
- Do not fabricate experimental outcomes.
- Do not assume e-INFRA exposes an API without verification.
- Do not ask for credentials to be pasted into source code.
- Do not stop at a partial implementation if further work is possible.
- Do not silently skip failed checks.
- Correct integration defects rather than bypassing them.

Make reasonable technical decisions independently.

Ask questions only when a decision genuinely requires unavailable user information or authorization.

## 18. Final report

After implementation, provide a concise report containing:

1. Implemented components.
2. Architecture overview.
3. How the multi-agent development workflow was used.
4. Tests executed and their results.
5. Infrastructure and end-to-end verification status.
6. AI inference providers supported.
7. Exact commands required to run the project locally.
8. Known limitations and unverified behavior.
9. Remaining work, if any.
10. Recommended next steps for the academic evaluation.

The final output must distinguish implemented and tested functionality from functionality that requires further verification.

**Start now by reading `AGENTS.md`, inspecting the repository, defining the architecture and tests, and then implementing the project phase by phase.**

