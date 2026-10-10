# Measurable Prompting

**Task**

From the files in `files/raw_tickets_texts` create three sets of prompts:

- **Train / development** – first 20 cases (1‑20)
- **Validation** – next 10 cases (21‑30)
- **Test** – last 10 cases (31‑40)

At least 8 edge cases (20 % of 40) must contain real complications such as missing information, ambiguous proposals, mismatched details, etc.

Create a total of **40 prompt bundles** and store them under `files/prompts`.

---

## Expected Directory Structure

```
files/prompts/
├── gpt-oss
│   ├── train
│   │   ├── 1
│   │   │   ├── basic.md
│   │   │   ├── structured.md
│   │   │   └── optimized.md
│   │   ├── 2
│   │   │   ├── basic.md
│   │   │   ├── structured.md
│   │   │   └── optimized.md
│   │   …
│   │   └── 20
│   │       ├── basic.md
│   │       ├── structured.md
│   │       └── optimized.md
│   ├── validate
│   │   ├── 21
│   │   │   ├── basic.md
│   │   │   ├── structured.md
│   │   │   └── optimized.md
│   │   …
│   │   └── 30
│   │       ├── basic.md
│   │       ├── structured.md
│   │       └── optimized.md
│   └── test
│       ├── 31
│       │   ├── basic.md
│       │   ├── structured.md
│       │   └── optimized.md
│       …
│       └── 40
│           ├── basic.md
│           ├── structured.md
│           └── optimized.md
├── gemini
│   └── … (other model families)
├── claude-sonnet
│   └── …
└── grok
    └── …
```

> **Note**: The folder `files/raw_tickets_texts` (not `files/raw_tickets/texts`) holds the original ticket files.

---

## Prompt Types

### Basic Prompt
A quick, unprepared prompt consisting of a single sentence followed by the ticket context:
```
Extract data from the given ticket to a JSON format.

Subject: <subject>
Body: <body>
```
No extra wording is added.

### Structured Prompt
A fully‑specified prompt using six architecture components:
1. **Persona/Role** – e.g., *You are a data extraction assistant.*
2. **Context/State** – the ticket subject and body.
3. **Instructions/Tasks** – extract the information into the required JSON.
4. **Constraints** – preserve wording, no fabrication, valid JSON.
5. **Few‑shot Examples** – one minimal example showing input and correct JSON output.
6. **Expected Format of Output** – the JSON schema:
```json
{
  "subject": "string | null",
  "body": "string",
  "type": "'Request' | 'Change' | 'Problem' | 'Incident'",
  "queue": "'Customer Service' | 'Technical Support' | 'IT Support' | 'Billing and Payments'",
  "priority": "'low' | 'medium' | 'high'",
  "language": "'en'"
}
```

### Optimized Prompt
Placeholder files for now; they will be refined after the basic and structured answers are reviewed.

---

## General Rules
- Work directly in the workspace files; do not delete original tickets.
- Keep the `ANSWER:` marker exactly as specified.
- Do **not** answer `optimized.md` files until Phase 2 (review) is complete.
- Follow the workflow described in `antigravity_prompt.md` for answering, reviewing, and evaluating prompts.

---

*This file now matches the actual repository layout and corrects the raw‑ticket path.*
