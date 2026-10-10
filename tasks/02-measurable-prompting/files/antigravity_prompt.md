# Antigravity evaluation prompt

You are evaluating the ticket-extraction prompts in this workspace. Follow the workflow exactly and write your answers directly into the designated prompt files.

## Workspace and prompt files

The prompt files are located under:

```text
prompts/
```

The prompt families are organized by model and split:

```text
prompts/<model>/<split>/<case-number>/<prompt-type>.md
```

where `<prompt-type>` is `basic`, `structured`, or `optimized`, and `<split>` is `train`, `validate`, or `test`.

Process all available prompt files for the Antigravity model directories. Do not modify prompt files belonging to another model unless they are explicitly assigned to you.

## Phase 1: Answer the basic and structured prompts

1. Find every `basic.md` and `structured.md` file in the assigned Antigravity prompt directories.
2. Read the complete prompt in each file and follow its instructions.
3. Write the answer directly into that same file, after the existing prompt text.
4. The response must contain only this label followed by the actual answer:

```text
ANSWER: <actual answer>
```

For structured prompts, `<actual answer>` must be one valid JSON object complying with the schema and constraints in the prompt. Do not add Markdown fences, explanations, notes, or additional fields after the JSON object.

Do not answer any `optimized.md` file during this phase.

## Phase 2: Review the basic and structured answers

After all basic and structured prompts have been answered, inspect the answers for flaws. For each case, assess issues such as:

- invalid JSON syntax;
- missing, extra, or incorrectly named fields;
- incorrect copying of the subject or body;
- unsupported assumptions or invented information;
- incorrect type, queue, priority, or language classification;
- failure to preserve uncertainty, conflicts, placeholders, HTML, or escape sequences;
- failure to handle missing information correctly;
- explanations or text outside the required answer format.

Use the original ticket and the prompt requirements as the source of truth. Do not silently change the original basic or structured answers while performing this review.

## Phase 3: Complete and answer the optimized prompts

1. Using the flaws found in Phase 2, complete each corresponding `optimized.md` prompt so that it is a clear, robust version of the prompt for that case.
2. Preserve the intended task and required JSON schema. Improve ambiguity handling, output constraints, classification guidance, and protection against hallucination where needed.
3. Write the completed optimized prompt into the corresponding `optimized.md` file.
4. Then answer the optimized prompt in the same file using exactly:

```text
ANSWER: <actual answer>
```

For optimized prompts, `<actual answer>` must also be a single valid JSON object when the prompt requires JSON. Do not include explanations, Markdown fences, or additional commentary.

Only answer optimized prompts after the basic and structured answers have been reviewed.

## Phase 4: Write evaluation metrics

After all three prompt types have been processed, create this new file:

```text
evaluation_metrics.md
```

Evaluate the answers against the original ticket data and the applicable prompt requirements. Include the following metrics for each model, split, case, and prompt type:

- Correct JSON format
- Accuracy & completeness
- Scale of hallucinations
- Scale of appropriate refusal

Use consistent scales and define them at the beginning of the file. Use:

- `Correct JSON format`: `1` if the answer is valid JSON with the required structure, otherwise `0`.
- `Accuracy & completeness`: a score from `0` to `1`, where `1` means all required values are correct and complete and `0` means none are correct.
- `Scale of hallucinations`: a score from `0` to `3`, where `0` means no unsupported information, `1` means minor unsupported detail, `2` means substantial unsupported information, and `3` means pervasive fabrication or failure to use the ticket as the source of truth.
- `Scale of appropriate refusal`: a score from `0` to `1`, where `1` means the model appropriately avoided unsupported action or claims when the ticket was ambiguous or incomplete, and `0` means it failed to do so. If refusal was not applicable, write `N/A` and explain why.

Include a Markdown table with one row per evaluated answer and columns for:

```text
Model | Split | Case | Prompt type | Correct JSON format | Accuracy & completeness | Scale of hallucinations | Scale of appropriate refusal | Notes
```

Add a short summary by model and prompt type after the detailed table. Base every metric and note on evidence from the ticket and the expected output rules. Do not invent results for files that were not processed.

## Phase 5: Evaluate the held-out test set and complete the worksheet

Only after every available basic, structured, and optimized prompt has been run and the detailed metrics have been recorded, perform the final evaluation.

1. Identify the held-out test cases (`test/31` through `test/40`, or the equivalent test-case range present in the assigned directories).
2. Evaluate and report the four metrics for the test set separately from the training and validation results. Do not use test-set results to revise prompts, optimized prompts, or answers.
3. Add a clearly labeled **Held-out test-set results** section to `evaluation_metrics.md` containing aggregate results for each model and prompt type. Include at least the mean Correct JSON format score, mean Accuracy & completeness score, mean Scale of hallucinations, and the proportion of applicable cases with an appropriate refusal.
4. State the number of evaluated cases and identify any missing or excluded answers. Do not treat missing results as correct or assign scores without evidence.
5. Complete `2026-AI-Student-worksheet.md` using the actual results and evidence from this evaluation. Fill in the relevant sections, including:
   - Operational definition;
   - Unit of analysis;
   - Primary metric and why it is valid;
   - Important quality dimensions not captured by the primary metric;
   - Dataset representativeness;
   - Leakage or contamination risks;
   - Prompt-freezing details;
   - Held-out-case protection;
   - Prompt-change log;
   - Evaluation calculations, calibration, and limitations;
   - Human raters, blinding, and response-order randomization, if applicable.
6. Update the worksheet's system, case-count, and prompt descriptions only when the workspace evidence supports the update. Preserve correct existing information.
7. In the worksheet, distinguish clearly between development/validation observations and held-out test-set conclusions. Use the held-out test set for the final claim about whether structured prompting improved performance.
8. Record the primary result, relevant secondary results, limitations, and any alternative explanation in concise, grammatically correct prose. If a field cannot be supported by the available evidence, write `Not evaluated` and explain what is missing rather than inventing a value.

The final deliverable is complete only when `evaluation_metrics.md` contains the evaluated held-out test-set results and `2026-AI-Student-worksheet.md` reflects the evidence-based conclusions.

## General rules

- Work directly in the workspace files.
- Do not delete the original ticket text or prompt instructions.
- Do not alter the ticket data.
- Keep the `ANSWER:` marker exactly as written.
- Do not answer optimized prompts before completing Phase 2.
- Do not write any answer for a prompt that you cannot locate or read; record the issue in `evaluation_metrics.md` instead.
- Do not claim that a prompt or model is better based only on training or validation results.
- Do not modify held-out test answers after beginning the final test-set evaluation.
- Keep all final conclusions traceable to recorded answers, source tickets, and metric calculations.
