# Testing the LangGraph RCA workflows

From the repository root, use Python 3.12 and run:

```sh
python -m pip install -r proj/tests/requirements.txt
python -m pytest proj/tests -rx
```

The workflow tests use fake completion responses and run without API
credentials, Kubernetes, or LangGraph. They are expected failures while
`proj.rca.workflows` is absent. Once the module exists, the tests run normally
and implementation errors fail the suite. During test-driven development use
`python -m pytest proj/tests --runxfail` to see the initial failing tests.

## Proposed interface

Implement `proj.rca.workflows.build_workflow(variant, *, complete)` to return a
compiled LangGraph with an `invoke({"context": context})` entry point. The
caller passes the `context` object from a case's `rca.json`. Keep the fixture's
`root-cause` with the evaluator.

Supply the model through the synchronous callable `complete(prompt_path,
payload) -> str`. The prompt path is relative to `proj/prompts/` and the
payload is JSON-compatible. Production can implement this callable with the
[e-INFRA CZ Chat Completions API](https://docs.cerit-sc.cz/en/docs/ai-as-a-service/ai-api).
Tests supply deterministic responses and simulate provider failures through the
same callable.

| Variant | Model calls | Result state |
| --- | --- | --- |
| `base` | `base.md` receives `{"context": context}` | `root-cause` contains the diagnosis text. |
| `optimal` | `optimal.md` receives `{"context": context}` | `root-cause` contains the parsed five-field RCA object. |
| `mas` | Three specialists receive their own fields. The coordinator receives the full context and all three parsed reports keyed by specialist name. | `root-cause` contains the parsed five-field RCA object. |

For MAS, send `resources` and `events` to the configuration specialist,
`logs` and `checks` to the logs specialist, and `metrics`, `time_window`,
and `resource_limits` to the metrics specialist. Each resource limit record
names the workload as `Kind/name` and includes its namespace, container,
requests, and limits. Preserve absent observations as empty lists or a null
time window. The coordinator runs after the three valid reports are ready.

Use the JSON contracts in the corresponding prompt files. Invalid structured
responses should raise `ValueError`. Let completion errors such as provider
timeouts propagate to the caller.
