# Measurable Prompting

Measurable prompting means adding quantifiable metrics, clear acceptance criteria, or score-based evaluation steps to your AI prompts so you can track accuracy and performance.

Instead of guessing whether an AI output looks "good", measurable prompting forces the model or a testing framework to grade the output against concrete numbers or targets.

## Example Comparison

* **Vague Prompt:** "Write a summary of this report and make sure it is good."
* **Measurable Prompt:** "Summarize this report in 3 bullet points* Each bullet point must be under 20 words, cite a specific statistic from the text, and maintain a neutral tone. At the end, output a self-evaluation score (1-5) on how strictly you followed these constraints."

## How to Work with the Files

The dataset can be divided into 3 parts: train (first 20), validation (next 10), test (last 10)

1. Train set gets run with basic, then structured and with optimalized prompt, which improved based on flaws from basic + structure ones.
2. For the validation, we just test the candidates with an optimalized prompt. From those we choose the best one.
3. The test set is then run with all 3 prompts and we compare the results: "On the 10 unknown tickets the basic prompt showed 40% of success, the structured prompt showed 70% and optimized showed 90%"
