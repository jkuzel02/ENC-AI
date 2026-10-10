# Prompt sets

Each of chatgpt, gemini, grok, and perplexity contains train/1–20, validate/21–30, and test/31–40. Case N uses files/raw_tickets_texts/<split>/raw_ticket_NNN.txt in its original order.

The detailed AGENTS.md layout specifies 40 cases per model, with three prompt files per case: 480 Markdown files across four models. This follows the explicit layout despite the introductory wording "40 prompt files in total".

Basic prompts contain the required sentence followed by the original ticket text. Structured prompts use all six architecture components and output only subject, body, type, queue, priority, and language. Their fictional examples and classification rules are identical across models and splits for comparable evaluation. Type, queue, and priority are inferred using those rules; they are not guaranteed to match dataset labels that are unavailable in the raw ticket. Queue uses the four allowed categories specified in AGENTS.md; language is en. No reference JSON answers or dataset labels are embedded. Optimized prompts are empty for manual completion.

## Existing edge cases

These complications are present in the original tickets; no synthetic changes were made. There are 13 documented edge cases (32.5% of 40), spanning all splits.

| Case | Split | Complication |
| --- | --- | --- |
| 5 | Train/development | Unnamed platforms and API; API changes are only a suspected cause. |
| 6 | Train/development | RAM allocation is suspected, with no measurements or platform identity. |
| 7 | Train/development | Reported data loss after updates; incompatibility is uncertain, and body contains literal escape sequences. |
| 10 | Train/development | Extremely sparse breach body; hospital context and urgency appear only in the subject. |
| 13 | Train/development | RAM limitations and software conflicts are tentative; versions and diagnostics are absent. |
| 14 | Train/development | Extremely sparse breach body; patient-record context appears only in the subject. |
| 15 | Train/development | Empty subject, possible breach, and unresolved <ref_num> placeholder. |
| 23 | Validation | Incorrect invoice amount reported without either the displayed or correct total. |
| 30 | Validation | Settings described as optimized while synchronization problems persist; affected tools are unnamed. |
| 31 | Test | HTML line breaks, a name placeholder, and multiple possible preceding changes. |
| 32 | Test | Empty subject; performance issues persist after rollback, so the suggested cause remains uncertain. |
| 33 | Test | Unauthorized access attempts do not prove successful access; outdated protocols are speculative. |
| 34 | Test | A breach is reported but compromise of medical data and its cause remain uncertain. |
