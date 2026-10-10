# Evaluation Metrics: Multi-Model Benchmark

## Metric Definitions and Measurement Scales

This evaluation benchmarks 4 AI systems (`Gemini 3.8 Flash`, `ChatGPT OSS 120B`, `Grok 4.5`, and `Claude Sonnet 4.6`) across 3 prompt conditions (`basic`, `structured`, `optimized`) and 40 IT ticket cases (total 480 runs).

- **Correct JSON format (0/1)**: `1` if the output is a single valid JSON object strictly complying with the schema without Markdown code fences (```` ```json ````) or external text; otherwise `0`.
- **Accuracy & completeness (0.0 to 1.0)**: Macro-averaged fraction of the six core keys (`subject`, `body`, `type`, `queue`, `priority`, `language`) that exactly match the ground-truth reference values.
- **Scale of hallucinations (0 to 3)**:
  - `0`: No unsupported information. Extracted text is verbatim and classifications adhere to ticket evidence.
  - `1`: Minor unsupported detail, extra keys, or superficial embellishment.
  - `2`: Substantial unsupported information (e.g., synthesizing a subject title when the ticket header is blank).
  - `3`: Pervasive fabrication, arbitrary outputs, or complete schema divergence.
- **Scale of appropriate refusal (0/1 or N/A)**:
  - `1`: The model appropriately refused to invent unsupported facts or assigned `null` when ticket information was missing/empty (Cases 15 and 32).
  - `0`: The model failed the negative constraint by fabricating content or copying label headers.
  - `N/A`: The ticket had unambiguous, complete information where negative refusal/null handling was not required.

---

## Detailed Evaluation Table (480 Runs)

| Model | Split | Case | Prompt type | Correct JSON format | Accuracy & completeness | Scale of hallucinations | Scale of appropriate refusal | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gemini-flash | train | 1 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Customer Service); Type: None (exp Request) |
| gemini-flash | train | 2 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Customer Service); Type: None (exp Request) |
| gemini-flash | train | 3 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Customer Service); Type: None (exp Request) |
| gemini-flash | train | 4 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Request) |
| gemini-flash | train | 5 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp IT Support); Type: None (exp Problem) |
| gemini-flash | train | 6 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Problem) |
| gemini-flash | train | 7 | basic | 0 | 0.33 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Incident) |
| gemini-flash | train | 8 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Request) |
| gemini-flash | train | 9 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Incident) |
| gemini-flash | train | 10 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Incident) |
| gemini-flash | train | 11 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Customer Service); Type: None (exp Problem) |
| gemini-flash | train | 12 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Product Support); Type: None (exp Change) |
| gemini-flash | train | 13 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Problem) |
| gemini-flash | train | 14 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Customer Service); Type: None (exp Incident) |
| gemini-flash | train | 15 | basic | 0 | 0.33 | 2 | 0 | Markdown fence used; Missing keys: language,type,queue; Subject mismatch: 'Reported Data Breach / O; Queue: None (exp Product Support); Type: None (exp Incident) |
| gemini-flash | train | 16 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp IT Support); Type: None (exp Change) |
| gemini-flash | train | 17 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Billing and Payments); Type: None (exp Request) |
| gemini-flash | train | 18 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Incident) |
| gemini-flash | train | 19 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Incident) |
| gemini-flash | train | 20 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Customer Service); Type: None (exp Request) |
| gemini-flash | validate | 21 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Product Support); Type: None (exp Request) |
| gemini-flash | validate | 22 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Service Outages and Maintenance); Type: None (exp Request) |
| gemini-flash | validate | 23 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Billing and Payments); Type: None (exp Incident) |
| gemini-flash | validate | 24 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Request) |
| gemini-flash | validate | 25 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Change) |
| gemini-flash | validate | 26 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Customer Service); Type: None (exp Request) |
| gemini-flash | validate | 27 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp IT Support); Type: None (exp Incident) |
| gemini-flash | validate | 28 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp IT Support); Type: None (exp Request) |
| gemini-flash | validate | 29 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Request) |
| gemini-flash | validate | 30 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp IT Support); Type: None (exp Change) |
| gemini-flash | test | 31 | basic | 0 | 0.33 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp IT Support); Type: None (exp Incident) |
| gemini-flash | test | 32 | basic | 0 | 0.33 | 2 | 0 | Markdown fence used; Missing keys: language,type,queue; Subject mismatch: 'Application Performance ; Queue: None (exp IT Support); Type: None (exp Problem) |
| gemini-flash | test | 33 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Billing and Payments); Type: None (exp Problem) |
| gemini-flash | test | 34 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Customer Service); Type: None (exp Incident) |
| gemini-flash | test | 35 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp IT Support); Type: None (exp Change) |
| gemini-flash | test | 36 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Product Support); Type: None (exp Request) |
| gemini-flash | test | 37 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp IT Support); Type: None (exp Incident) |
| gemini-flash | test | 38 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Technical Support); Type: None (exp Incident) |
| gemini-flash | test | 39 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Customer Service); Type: None (exp Request) |
| gemini-flash | test | 40 | basic | 0 | 0.50 | 1 | N/A | Markdown fence used; Missing keys: language,type,queue; Queue: None (exp Billing and Payments); Type: None (exp Request) |
| gemini-flash | train | 1 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 2 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 3 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 4 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 5 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 6 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 7 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 8 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 9 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 10 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 11 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 12 | structured | 1 | 0.83 | 0 | N/A | Queue: Technical Support (exp Product Support) |
| gemini-flash | train | 13 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 14 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 15 | structured | 1 | 0.83 | 0 | 1 | Queue: IT Support (exp Product Support) |
| gemini-flash | train | 16 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 17 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 18 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 19 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 20 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 21 | structured | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Product Support) |
| gemini-flash | validate | 22 | structured | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Service Outages and Maintenance) |
| gemini-flash | validate | 23 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 24 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 25 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 26 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 27 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 28 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 29 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 30 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 31 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 32 | structured | 1 | 1.00 | 0 | 1 | Perfect match |
| gemini-flash | test | 33 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 34 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 35 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 36 | structured | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Product Support) |
| gemini-flash | test | 37 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 38 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 39 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 40 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 1 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 2 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 3 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 4 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 5 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 6 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 7 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 8 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 9 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 10 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 11 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 12 | optimized | 1 | 0.83 | 0 | N/A | Queue: Technical Support (exp Product Support) |
| gemini-flash | train | 13 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 14 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 15 | optimized | 1 | 0.83 | 0 | 1 | Queue: IT Support (exp Product Support) |
| gemini-flash | train | 16 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 17 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 18 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 19 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | train | 20 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 21 | optimized | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Product Support) |
| gemini-flash | validate | 22 | optimized | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Service Outages and Maintenance) |
| gemini-flash | validate | 23 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 24 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 25 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 26 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 27 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 28 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 29 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | validate | 30 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 31 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 32 | optimized | 1 | 1.00 | 0 | 1 | Perfect match |
| gemini-flash | test | 33 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 34 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 35 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 36 | optimized | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Product Support) |
| gemini-flash | test | 37 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 38 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 39 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gemini-flash | test | 40 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gpt-oss | train | 1 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| gpt-oss | train | 2 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| gpt-oss | train | 3 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| gpt-oss | train | 4 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp medium) |
| gpt-oss | train | 5 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Problem); Priority: low (exp high) |
| gpt-oss | train | 6 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Problem); Priority: low (exp high) |
| gpt-oss | train | 7 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Incident); Priority: low (exp high) |
| gpt-oss | train | 8 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp medium) |
| gpt-oss | train | 9 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Incident) |
| gpt-oss | train | 10 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Incident); Priority: low (exp high) |
| gpt-oss | train | 11 | basic | 1 | 0.83 | 0 | N/A | Type: Request (exp Problem) |
| gpt-oss | train | 12 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Product Support); Type: Request (exp Change) |
| gpt-oss | train | 13 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Problem); Priority: low (exp high) |
| gpt-oss | train | 14 | basic | 1 | 0.67 | 0 | N/A | Type: Request (exp Incident); Priority: low (exp high) |
| gpt-oss | train | 15 | basic | 1 | 0.33 | 2 | 0 | Subject mismatch: 'Subject:'; Queue: Customer Service (exp Product Support); Type: Request (exp Incident); Priority: low (exp high) |
| gpt-oss | train | 16 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Change); Priority: low (exp medium) |
| gpt-oss | train | 17 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Billing and Payments); Priority: low (exp medium) |
| gpt-oss | train | 18 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Incident); Priority: low (exp medium) |
| gpt-oss | train | 19 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Incident); Priority: low (exp medium) |
| gpt-oss | train | 20 | basic | 1 | 1.00 | 0 | N/A | Perfect match |
| gpt-oss | validate | 21 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Product Support); Priority: low (exp high) |
| gpt-oss | validate | 22 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Service Outages and Maintenance); Priority: low (exp high) |
| gpt-oss | validate | 23 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Billing and Payments); Type: Request (exp Incident) |
| gpt-oss | validate | 24 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp high) |
| gpt-oss | validate | 25 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Change); Priority: low (exp high) |
| gpt-oss | validate | 26 | basic | 1 | 1.00 | 0 | N/A | Perfect match |
| gpt-oss | validate | 27 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Incident); Priority: low (exp medium) |
| gpt-oss | validate | 28 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp IT Support); Priority: low (exp medium) |
| gpt-oss | validate | 29 | basic | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Technical Support) |
| gpt-oss | validate | 30 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Change); Priority: low (exp medium) |
| gpt-oss | test | 31 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Incident) |
| gpt-oss | test | 32 | basic | 1 | 0.33 | 2 | 0 | Subject mismatch: 'Subject:'; Queue: Customer Service (exp IT Support); Type: Request (exp Problem); Priority: low (exp high) |
| gpt-oss | test | 33 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Billing and Payments); Type: Request (exp Problem); Priority: low (exp high) |
| gpt-oss | test | 34 | basic | 1 | 0.83 | 0 | N/A | Type: Request (exp Incident) |
| gpt-oss | test | 35 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Change); Priority: low (exp medium) |
| gpt-oss | test | 36 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Product Support); Priority: low (exp high) |
| gpt-oss | test | 37 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Incident); Priority: low (exp medium) |
| gpt-oss | test | 38 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Incident); Priority: low (exp medium) |
| gpt-oss | test | 39 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| gpt-oss | test | 40 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Billing and Payments); Priority: low (exp high) |
| gpt-oss | train | 1 | structured | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| gpt-oss | train | 2 | structured | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| gpt-oss | train | 3 | structured | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Customer Service); Type: Incident (exp Request); Priority: high (exp medium) |
| gpt-oss | train | 4 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp medium) |
| gpt-oss | train | 5 | structured | 1 | 0.83 | 0 | N/A | Type: Incident (exp Problem) |
| gpt-oss | train | 6 | structured | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Problem); Priority: low (exp high) |
| gpt-oss | train | 7 | structured | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Incident); Priority: low (exp high) |
| gpt-oss | train | 8 | structured | 1 | 0.83 | 0 | N/A | Type: Problem (exp Request) |
| gpt-oss | train | 9 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Incident) |
| gpt-oss | train | 10 | structured | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Technical Support) |
| gpt-oss | train | 11 | structured | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Customer Service); Type: Incident (exp Problem); Priority: high (exp low) |
| gpt-oss | train | 12 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Product Support); Type: Request (exp Change) |
| gpt-oss | train | 13 | structured | 1 | 0.83 | 0 | N/A | Priority: medium (exp high) |
| gpt-oss | train | 14 | structured | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| gpt-oss | train | 15 | structured | 1 | 0.67 | 2 | 0 | Subject mismatch: 'Subject:'; Queue: IT Support (exp Product Support) |
| gpt-oss | train | 16 | structured | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Change); Priority: low (exp medium) |
| gpt-oss | train | 17 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Billing and Payments); Type: Problem (exp Request) |
| gpt-oss | train | 18 | structured | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| gpt-oss | train | 19 | structured | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| gpt-oss | train | 20 | structured | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Customer Service); Type: Incident (exp Request); Priority: high (exp low) |
| gpt-oss | validate | 21 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Product Support); Priority: low (exp high) |
| gpt-oss | validate | 22 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Service Outages and Maintenance); Priority: low (exp high) |
| gpt-oss | validate | 23 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Priority: high (exp low) |
| gpt-oss | validate | 24 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp high) |
| gpt-oss | validate | 25 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Incident (exp Change) |
| gpt-oss | validate | 26 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| gpt-oss | validate | 27 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident) |
| gpt-oss | validate | 28 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Request) |
| gpt-oss | validate | 29 | structured | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Technical Support) |
| gpt-oss | validate | 30 | structured | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Change); Priority: low (exp medium) |
| gpt-oss | test | 31 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Incident) |
| gpt-oss | test | 32 | structured | 1 | 0.50 | 2 | 0 | Subject mismatch: 'Subject:'; Queue: Technical Support (exp IT Support); Priority: medium (exp high) |
| gpt-oss | test | 33 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Type: Incident (exp Problem) |
| gpt-oss | test | 34 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: high (exp low) |
| gpt-oss | test | 35 | structured | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Change); Priority: low (exp medium) |
| gpt-oss | test | 36 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Product Support); Type: Incident (exp Request) |
| gpt-oss | test | 37 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident) |
| gpt-oss | test | 38 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Priority: high (exp medium) |
| gpt-oss | test | 39 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Type: Problem (exp Request) |
| gpt-oss | test | 40 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Billing and Payments); Priority: low (exp high) |
| gpt-oss | train | 1 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| gpt-oss | train | 2 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| gpt-oss | train | 3 | optimized | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Customer Service); Type: Incident (exp Request); Priority: high (exp medium) |
| gpt-oss | train | 4 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp medium) |
| gpt-oss | train | 5 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Incident (exp Problem) |
| gpt-oss | train | 6 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Incident (exp Problem) |
| gpt-oss | train | 7 | optimized | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Incident); Priority: low (exp high) |
| gpt-oss | train | 8 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Problem (exp Request) |
| gpt-oss | train | 9 | optimized | 1 | 0.83 | 0 | N/A | Type: Request (exp Incident) |
| gpt-oss | train | 10 | optimized | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Technical Support) |
| gpt-oss | train | 11 | optimized | 1 | 0.50 | 0 | N/A | Queue: Technical Support (exp Customer Service); Type: Incident (exp Problem); Priority: high (exp low) |
| gpt-oss | train | 12 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Product Support); Type: Request (exp Change) |
| gpt-oss | train | 13 | optimized | 1 | 0.83 | 0 | N/A | Priority: medium (exp high) |
| gpt-oss | train | 14 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gpt-oss | train | 15 | optimized | 1 | 0.67 | 2 | 0 | Subject mismatch: 'Subject:'; Queue: IT Support (exp Product Support) |
| gpt-oss | train | 16 | optimized | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Incident (exp Change); Priority: high (exp medium) |
| gpt-oss | train | 17 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Billing and Payments); Type: Problem (exp Request) |
| gpt-oss | train | 18 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Problem (exp Incident) |
| gpt-oss | train | 19 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Problem (exp Incident) |
| gpt-oss | train | 20 | optimized | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Customer Service); Type: Incident (exp Request); Priority: high (exp low) |
| gpt-oss | validate | 21 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Product Support); Priority: low (exp high) |
| gpt-oss | validate | 22 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Service Outages and Maintenance); Priority: low (exp high) |
| gpt-oss | validate | 23 | optimized | 1 | 0.83 | 0 | N/A | Priority: high (exp low) |
| gpt-oss | validate | 24 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp high) |
| gpt-oss | validate | 25 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Incident (exp Change) |
| gpt-oss | validate | 26 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| gpt-oss | validate | 27 | optimized | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: high (exp medium) |
| gpt-oss | validate | 28 | optimized | 1 | 0.83 | 0 | N/A | Type: Problem (exp Request) |
| gpt-oss | validate | 29 | optimized | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Technical Support) |
| gpt-oss | validate | 30 | optimized | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Change); Priority: low (exp medium) |
| gpt-oss | test | 31 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Incident) |
| gpt-oss | test | 32 | optimized | 1 | 0.67 | 2 | 0 | Subject mismatch: 'Subject:'; Priority: medium (exp high) |
| gpt-oss | test | 33 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Type: Incident (exp Problem) |
| gpt-oss | test | 34 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: high (exp low) |
| gpt-oss | test | 35 | optimized | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Change); Priority: low (exp medium) |
| gpt-oss | test | 36 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Product Support); Type: Incident (exp Request) |
| gpt-oss | test | 37 | optimized | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp IT Support); Type: Request (exp Incident); Priority: low (exp medium) |
| gpt-oss | test | 38 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Priority: high (exp medium) |
| gpt-oss | test | 39 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| gpt-oss | test | 40 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp high) |
| grok | train | 1 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| grok | train | 2 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: low (exp medium) |
| grok | train | 3 | basic | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Customer Service); Type: Incident (exp Request); Priority: high (exp medium) |
| grok | train | 4 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Change (exp Request) |
| grok | train | 5 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: medium (exp high) |
| grok | train | 6 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Incident (exp Problem) |
| grok | train | 7 | basic | 1 | 1.00 | 0 | N/A | Perfect match |
| grok | train | 8 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp medium) |
| grok | train | 9 | basic | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| grok | train | 10 | basic | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Technical Support) |
| grok | train | 11 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: medium (exp low) |
| grok | train | 12 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: medium (exp low) |
| grok | train | 13 | basic | 1 | 0.83 | 0 | N/A | Priority: medium (exp high) |
| grok | train | 14 | basic | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| grok | train | 15 | basic | 1 | 0.67 | 2 | 0 | Subject mismatch: 'Body: To Whom It May Con; Queue: IT Support (exp Product Support) |
| grok | train | 16 | basic | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp IT Support) |
| grok | train | 17 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Billing and Payments); Priority: low (exp medium) |
| grok | train | 18 | basic | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| grok | train | 19 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Problem (exp Incident) |
| grok | train | 20 | basic | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| grok | validate | 21 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: low (exp high) |
| grok | validate | 22 | basic | 1 | 0.50 | 0 | N/A | Queue: Technical Support (exp Service Outages and Maintenance); Type: Problem (exp Request); Priority: medium (exp high) |
| grok | validate | 23 | basic | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| grok | validate | 24 | basic | 1 | 0.67 | 0 | N/A | Type: Change (exp Request); Priority: medium (exp high) |
| grok | validate | 25 | basic | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Change); Priority: low (exp high) |
| grok | validate | 26 | basic | 1 | 0.83 | 0 | N/A | Queue: Billing and Payments (exp Customer Service) |
| grok | validate | 27 | basic | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| grok | validate | 28 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| grok | validate | 29 | basic | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Technical Support) |
| grok | validate | 30 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Change) |
| grok | test | 31 | basic | 1 | 0.50 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident); Priority: medium (exp low) |
| grok | test | 32 | basic | 1 | 0.67 | 2 | 0 | Subject mismatch: 'Body: During the last de; Priority: medium (exp high) |
| grok | test | 33 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Type: Incident (exp Problem) |
| grok | test | 34 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: high (exp low) |
| grok | test | 35 | basic | 1 | 0.83 | 0 | N/A | Queue: Technical Support (exp IT Support) |
| grok | test | 36 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Product Support); Priority: low (exp high) |
| grok | test | 37 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident) |
| grok | test | 38 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Priority: high (exp medium) |
| grok | test | 39 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| grok | test | 40 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp high) |
| grok | train | 1 | structured | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| grok | train | 2 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: low (exp medium) |
| grok | train | 3 | structured | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Customer Service); Type: Incident (exp Request); Priority: high (exp medium) |
| grok | train | 4 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Change (exp Request) |
| grok | train | 5 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: medium (exp high) |
| grok | train | 6 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Incident (exp Problem) |
| grok | train | 7 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| grok | train | 8 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp medium) |
| grok | train | 9 | structured | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| grok | train | 10 | structured | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Technical Support) |
| grok | train | 11 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: medium (exp low) |
| grok | train | 12 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: medium (exp low) |
| grok | train | 13 | structured | 1 | 0.83 | 0 | N/A | Priority: medium (exp high) |
| grok | train | 14 | structured | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| grok | train | 15 | structured | 1 | 0.67 | 2 | 0 | Subject mismatch: 'Body: To Whom It May Con; Queue: IT Support (exp Product Support) |
| grok | train | 16 | structured | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp IT Support) |
| grok | train | 17 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Billing and Payments); Priority: low (exp medium) |
| grok | train | 18 | structured | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| grok | train | 19 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Problem (exp Incident) |
| grok | train | 20 | structured | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| grok | validate | 21 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: low (exp high) |
| grok | validate | 22 | structured | 1 | 0.50 | 0 | N/A | Queue: Technical Support (exp Service Outages and Maintenance); Type: Problem (exp Request); Priority: medium (exp high) |
| grok | validate | 23 | structured | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| grok | validate | 24 | structured | 1 | 0.67 | 0 | N/A | Type: Change (exp Request); Priority: medium (exp high) |
| grok | validate | 25 | structured | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Change); Priority: low (exp high) |
| grok | validate | 26 | structured | 1 | 0.83 | 0 | N/A | Queue: Billing and Payments (exp Customer Service) |
| grok | validate | 27 | structured | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| grok | validate | 28 | structured | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| grok | validate | 29 | structured | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Technical Support) |
| grok | validate | 30 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Change) |
| grok | test | 31 | structured | 1 | 0.50 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident); Priority: medium (exp low) |
| grok | test | 32 | structured | 1 | 0.67 | 2 | 0 | Subject mismatch: 'Body: During the last de; Priority: medium (exp high) |
| grok | test | 33 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Type: Incident (exp Problem) |
| grok | test | 34 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: high (exp low) |
| grok | test | 35 | structured | 1 | 0.83 | 0 | N/A | Queue: Technical Support (exp IT Support) |
| grok | test | 36 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Product Support); Priority: low (exp high) |
| grok | test | 37 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident) |
| grok | test | 38 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Priority: high (exp medium) |
| grok | test | 39 | structured | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| grok | test | 40 | structured | 1 | 0.83 | 0 | N/A | Priority: low (exp high) |
| grok | train | 1 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| grok | train | 2 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: low (exp medium) |
| grok | train | 3 | optimized | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Customer Service); Type: Incident (exp Request); Priority: high (exp medium) |
| grok | train | 4 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Change (exp Request) |
| grok | train | 5 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: medium (exp high) |
| grok | train | 6 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Incident (exp Problem) |
| grok | train | 7 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| grok | train | 8 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp medium) |
| grok | train | 9 | optimized | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| grok | train | 10 | optimized | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Technical Support) |
| grok | train | 11 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: medium (exp low) |
| grok | train | 12 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: medium (exp low) |
| grok | train | 13 | optimized | 1 | 0.83 | 0 | N/A | Priority: medium (exp high) |
| grok | train | 14 | optimized | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| grok | train | 15 | optimized | 1 | 0.67 | 2 | 0 | Subject mismatch: 'Body: To Whom It May Con; Queue: IT Support (exp Product Support) |
| grok | train | 16 | optimized | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp IT Support) |
| grok | train | 17 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Billing and Payments); Priority: low (exp medium) |
| grok | train | 18 | optimized | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| grok | train | 19 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Problem (exp Incident) |
| grok | train | 20 | optimized | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| grok | validate | 21 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: low (exp high) |
| grok | validate | 22 | optimized | 1 | 0.50 | 0 | N/A | Queue: Technical Support (exp Service Outages and Maintenance); Type: Problem (exp Request); Priority: medium (exp high) |
| grok | validate | 23 | optimized | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| grok | validate | 24 | optimized | 1 | 0.67 | 0 | N/A | Type: Change (exp Request); Priority: medium (exp high) |
| grok | validate | 25 | optimized | 1 | 0.50 | 0 | N/A | Queue: Customer Service (exp Technical Support); Type: Request (exp Change); Priority: low (exp high) |
| grok | validate | 26 | optimized | 1 | 0.83 | 0 | N/A | Queue: Billing and Payments (exp Customer Service) |
| grok | validate | 27 | optimized | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| grok | validate | 28 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| grok | validate | 29 | optimized | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Technical Support) |
| grok | validate | 30 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Change) |
| grok | test | 31 | optimized | 1 | 0.50 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident); Priority: medium (exp low) |
| grok | test | 32 | optimized | 1 | 0.67 | 2 | 0 | Subject mismatch: 'Body: During the last de; Priority: medium (exp high) |
| grok | test | 33 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Type: Incident (exp Problem) |
| grok | test | 34 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: high (exp low) |
| grok | test | 35 | optimized | 1 | 0.83 | 0 | N/A | Queue: Technical Support (exp IT Support) |
| grok | test | 36 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Product Support); Priority: low (exp high) |
| grok | test | 37 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident) |
| grok | test | 38 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Priority: high (exp medium) |
| grok | test | 39 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| grok | test | 40 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp high) |
| claude-sonnet | train | 1 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| claude-sonnet | train | 2 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: low (exp medium) |
| claude-sonnet | train | 3 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: low (exp medium) |
| claude-sonnet | train | 4 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Priority: low (exp medium) |
| claude-sonnet | train | 5 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Incident (exp Problem) |
| claude-sonnet | train | 6 | basic | 1 | 0.83 | 0 | N/A | Type: Incident (exp Problem) |
| claude-sonnet | train | 7 | basic | 1 | 1.00 | 0 | N/A | Perfect match |
| claude-sonnet | train | 8 | basic | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp medium) |
| claude-sonnet | train | 9 | basic | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| claude-sonnet | train | 10 | basic | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Technical Support) |
| claude-sonnet | train | 11 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: medium (exp low) |
| claude-sonnet | train | 12 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: medium (exp low) |
| claude-sonnet | train | 13 | basic | 1 | 1.00 | 0 | N/A | Perfect match |
| claude-sonnet | train | 14 | basic | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| claude-sonnet | train | 15 | basic | 1 | 0.83 | 0 | 1 | Queue: IT Support (exp Product Support) |
| claude-sonnet | train | 16 | basic | 1 | 0.83 | 0 | N/A | Priority: high (exp medium) |
| claude-sonnet | train | 17 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Priority: low (exp medium) |
| claude-sonnet | train | 18 | basic | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: high (exp medium) |
| claude-sonnet | train | 19 | basic | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| claude-sonnet | train | 20 | basic | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| claude-sonnet | validate | 21 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: low (exp high) |
| claude-sonnet | validate | 22 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Service Outages and Maintenance); Priority: low (exp high) |
| claude-sonnet | validate | 23 | basic | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| claude-sonnet | validate | 24 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp high) |
| claude-sonnet | validate | 25 | basic | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Request (exp Change); Priority: low (exp high) |
| claude-sonnet | validate | 26 | basic | 1 | 1.00 | 0 | N/A | Perfect match |
| claude-sonnet | validate | 27 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: high (exp medium) |
| claude-sonnet | validate | 28 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: low (exp medium) |
| claude-sonnet | validate | 29 | basic | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Technical Support) |
| claude-sonnet | validate | 30 | basic | 1 | 0.83 | 0 | N/A | Queue: Technical Support (exp IT Support) |
| claude-sonnet | test | 31 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: medium (exp low) |
| claude-sonnet | test | 32 | basic | 1 | 0.67 | 0 | 1 | Queue: Technical Support (exp IT Support); Type: Incident (exp Problem) |
| claude-sonnet | test | 33 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Type: Incident (exp Problem) |
| claude-sonnet | test | 34 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: high (exp low) |
| claude-sonnet | test | 35 | basic | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp IT Support) |
| claude-sonnet | test | 36 | basic | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Product Support); Priority: low (exp high) |
| claude-sonnet | test | 37 | basic | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident) |
| claude-sonnet | test | 38 | basic | 1 | 0.83 | 0 | N/A | Priority: high (exp medium) |
| claude-sonnet | test | 39 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| claude-sonnet | test | 40 | basic | 1 | 0.83 | 0 | N/A | Priority: low (exp high) |
| claude-sonnet | train | 1 | structured | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| claude-sonnet | train | 2 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: low (exp medium) |
| claude-sonnet | train | 3 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: low (exp medium) |
| claude-sonnet | train | 4 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Priority: low (exp medium) |
| claude-sonnet | train | 5 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Incident (exp Problem) |
| claude-sonnet | train | 6 | structured | 1 | 0.83 | 0 | N/A | Type: Incident (exp Problem) |
| claude-sonnet | train | 7 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| claude-sonnet | train | 8 | structured | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp medium) |
| claude-sonnet | train | 9 | structured | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| claude-sonnet | train | 10 | structured | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Technical Support) |
| claude-sonnet | train | 11 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: medium (exp low) |
| claude-sonnet | train | 12 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: medium (exp low) |
| claude-sonnet | train | 13 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| claude-sonnet | train | 14 | structured | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| claude-sonnet | train | 15 | structured | 1 | 0.83 | 0 | 1 | Queue: IT Support (exp Product Support) |
| claude-sonnet | train | 16 | structured | 1 | 0.83 | 0 | N/A | Priority: high (exp medium) |
| claude-sonnet | train | 17 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Priority: low (exp medium) |
| claude-sonnet | train | 18 | structured | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: high (exp medium) |
| claude-sonnet | train | 19 | structured | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| claude-sonnet | train | 20 | structured | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| claude-sonnet | validate | 21 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: low (exp high) |
| claude-sonnet | validate | 22 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Service Outages and Maintenance); Priority: low (exp high) |
| claude-sonnet | validate | 23 | structured | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| claude-sonnet | validate | 24 | structured | 1 | 0.83 | 0 | N/A | Priority: low (exp high) |
| claude-sonnet | validate | 25 | structured | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Request (exp Change); Priority: low (exp high) |
| claude-sonnet | validate | 26 | structured | 1 | 1.00 | 0 | N/A | Perfect match |
| claude-sonnet | validate | 27 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: high (exp medium) |
| claude-sonnet | validate | 28 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: low (exp medium) |
| claude-sonnet | validate | 29 | structured | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Technical Support) |
| claude-sonnet | validate | 30 | structured | 1 | 0.83 | 0 | N/A | Queue: Technical Support (exp IT Support) |
| claude-sonnet | test | 31 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: medium (exp low) |
| claude-sonnet | test | 32 | structured | 1 | 0.67 | 0 | 1 | Queue: Technical Support (exp IT Support); Type: Incident (exp Problem) |
| claude-sonnet | test | 33 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Type: Incident (exp Problem) |
| claude-sonnet | test | 34 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: high (exp low) |
| claude-sonnet | test | 35 | structured | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp IT Support) |
| claude-sonnet | test | 36 | structured | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Product Support); Priority: low (exp high) |
| claude-sonnet | test | 37 | structured | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident) |
| claude-sonnet | test | 38 | structured | 1 | 0.83 | 0 | N/A | Priority: high (exp medium) |
| claude-sonnet | test | 39 | structured | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| claude-sonnet | test | 40 | structured | 1 | 0.83 | 0 | N/A | Priority: low (exp high) |
| claude-sonnet | train | 1 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| claude-sonnet | train | 2 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: low (exp medium) |
| claude-sonnet | train | 3 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: low (exp medium) |
| claude-sonnet | train | 4 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Technical Support); Priority: low (exp medium) |
| claude-sonnet | train | 5 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Incident (exp Problem) |
| claude-sonnet | train | 6 | optimized | 1 | 0.83 | 0 | N/A | Type: Incident (exp Problem) |
| claude-sonnet | train | 7 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| claude-sonnet | train | 8 | optimized | 1 | 0.67 | 0 | N/A | Queue: Customer Service (exp Technical Support); Priority: low (exp medium) |
| claude-sonnet | train | 9 | optimized | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| claude-sonnet | train | 10 | optimized | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Technical Support) |
| claude-sonnet | train | 11 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Customer Service); Priority: medium (exp low) |
| claude-sonnet | train | 12 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: medium (exp low) |
| claude-sonnet | train | 13 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| claude-sonnet | train | 14 | optimized | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| claude-sonnet | train | 15 | optimized | 1 | 0.83 | 0 | 1 | Queue: IT Support (exp Product Support) |
| claude-sonnet | train | 16 | optimized | 1 | 0.83 | 0 | N/A | Priority: high (exp medium) |
| claude-sonnet | train | 17 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Priority: low (exp medium) |
| claude-sonnet | train | 18 | optimized | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: high (exp medium) |
| claude-sonnet | train | 19 | optimized | 1 | 0.83 | 0 | N/A | Type: Problem (exp Incident) |
| claude-sonnet | train | 20 | optimized | 1 | 0.83 | 0 | N/A | Queue: IT Support (exp Customer Service) |
| claude-sonnet | validate | 21 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Product Support); Priority: low (exp high) |
| claude-sonnet | validate | 22 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp Service Outages and Maintenance); Priority: low (exp high) |
| claude-sonnet | validate | 23 | optimized | 1 | 0.67 | 0 | N/A | Type: Problem (exp Incident); Priority: medium (exp low) |
| claude-sonnet | validate | 24 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp high) |
| claude-sonnet | validate | 25 | optimized | 1 | 0.50 | 0 | N/A | Queue: IT Support (exp Technical Support); Type: Request (exp Change); Priority: low (exp high) |
| claude-sonnet | validate | 26 | optimized | 1 | 1.00 | 0 | N/A | Perfect match |
| claude-sonnet | validate | 27 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: high (exp medium) |
| claude-sonnet | validate | 28 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: low (exp medium) |
| claude-sonnet | validate | 29 | optimized | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp Technical Support) |
| claude-sonnet | validate | 30 | optimized | 1 | 0.83 | 0 | N/A | Queue: Technical Support (exp IT Support) |
| claude-sonnet | test | 31 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Priority: medium (exp low) |
| claude-sonnet | test | 32 | optimized | 1 | 0.67 | 0 | 1 | Queue: Technical Support (exp IT Support); Type: Incident (exp Problem) |
| claude-sonnet | test | 33 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Billing and Payments); Type: Incident (exp Problem) |
| claude-sonnet | test | 34 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Customer Service); Priority: high (exp low) |
| claude-sonnet | test | 35 | optimized | 1 | 0.83 | 0 | N/A | Queue: Customer Service (exp IT Support) |
| claude-sonnet | test | 36 | optimized | 1 | 0.67 | 0 | N/A | Queue: IT Support (exp Product Support); Priority: low (exp high) |
| claude-sonnet | test | 37 | optimized | 1 | 0.67 | 0 | N/A | Queue: Technical Support (exp IT Support); Type: Problem (exp Incident) |
| claude-sonnet | test | 38 | optimized | 1 | 0.83 | 0 | N/A | Priority: high (exp medium) |
| claude-sonnet | test | 39 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp medium) |
| claude-sonnet | test | 40 | optimized | 1 | 0.83 | 0 | N/A | Priority: low (exp high) |

---

## Summary by Model and Prompt Type

| Model | Prompt Type | Evaluated Runs | Correct JSON Format Rate | Mean Accuracy & Completeness | Mean Hallucination Score | Appropriate Refusal Rate |
| --- | --- | --- | --- | --- | --- | --- |
| gemini-flash | basic | 40 | 0.0% (0/40) | 48.3% | 1.05 | 0.0% (0/2) |
| gemini-flash | structured | 40 | 100.0% (40/40) | 97.9% | 0.00 | 100.0% (2/2) |
| gemini-flash | optimized | 40 | 100.0% (40/40) | 97.9% | 0.00 | 100.0% (2/2) |
| gpt-oss | basic | 40 | 100.0% (40/40) | 63.3% | 0.10 | 0.0% (0/2) |
| gpt-oss | structured | 40 | 100.0% (40/40) | 67.9% | 0.10 | 0.0% (0/2) |
| gpt-oss | optimized | 40 | 100.0% (40/40) | 69.2% | 0.10 | 0.0% (0/2) |
| grok | basic | 40 | 100.0% (40/40) | 71.7% | 0.10 | 0.0% (0/2) |
| grok | structured | 40 | 100.0% (40/40) | 71.7% | 0.10 | 0.0% (0/2) |
| grok | optimized | 40 | 100.0% (40/40) | 71.7% | 0.10 | 0.0% (0/2) |
| claude-sonnet | basic | 40 | 100.0% (40/40) | 75.0% | 0.00 | 100.0% (2/2) |
| claude-sonnet | structured | 40 | 100.0% (40/40) | 75.0% | 0.00 | 100.0% (2/2) |
| claude-sonnet | optimized | 40 | 100.0% (40/40) | 75.0% | 0.00 | 100.0% (2/2) |
