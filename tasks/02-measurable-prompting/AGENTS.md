# Measurable Prompting

Task to do:

From the files in `files/raw_tickets/texts` I need you to create specifically these 3 kind of prompts:

* Train/development set (first 20 cases)
* Validation set (next 10 cases)
* Test set (last 10 cases)

There have to be at least 8 edge cases (as 20% from 40), which will contain real complications (e.g. missing informations in the ticket,
uncertain proposal, unmatching details, etc.)

You will create 40 prompt files in total and store them inside `files/prompts`.

## Expected Structure

### Structure of Prompts Directory

The dir `files/prompts` will contain this structure:

```text
files/prompts/
├── 1/
    ├── basic.md
    ├── structured.md
    └── optimized.md
├── 2/
    ├── basic.md
    ├── structured.md
    └── optimized.md
├── 3/
    ├── basic.md
    ├── structured.md
    └── optimized.md
...
├── 40/
    ├── basic.md
    ├── structured.md
    └── optimized.md
```

### Structure of Prompts

#### Basic Prompt

Basic prompt is just a quick try. There is no perparation. It will only contain a sentece: "Extract the data from the given ticket to a JSON format." Followed by the actual context of the ticket. Do not even say it is already the ticket beginning and end.

#### Structured Prompt

Structured prompt has a set clear rules, roles and format. Use 6 architecture components (Persona/Role, Context/State, Instructions/Tasks, Constraints, Few-shot Examples, Expected Format of Output).

#### Optimized Prompts

The optimized prompts will for now stay clean, and will be handled after the Basic + Structured Prompts for each. It will be the part, that will be handled manually.
