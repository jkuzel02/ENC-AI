# Prompt sets

Cases 1–20 are train/development, 21–30 validation, and 31–40 test. Case N maps directly to `raw_tickets_texts/raw_ticket_NNN.txt`; the original order is preserved.

The explicit directory layout in AGENTS.md defines 40 numbered case directories, each containing basic.md, structured.md, and optimized.md: 120 Markdown files in total. This follows the detailed layout despite the introductory wording "40 prompt files in total".

Each basic.md contains the required instruction followed directly by its matching original raw ticket, without ticket boundary markers. Each structured.md embeds that same original ticket and uses the six required architecture components, with a consistent extraction schema, rules, and fictional examples across all splits. No reference JSON answers or dataset labels are included. The structured schema extracts ticket evidence and uncertainty rather than predicting unavailable support replies or internal routing labels. Every optimized.md is empty for manual completion.

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
