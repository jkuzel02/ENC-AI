import json
from pathlib import Path
from datasets import load_dataset


# https://huggingface.co/datasets/mihalachecostindaniel/ticket-triage-data
# Load only the first 40 rows
dataset = load_dataset(
    "mihalachecostindaniel/ticket-triage-data",
    split="train[:40]"
)


# Create output directory
output_dir = Path("ticket_triage_json")
output_dir.mkdir(parents=True, exist_ok=True)


# Save each row as a separate JSON file
for i, row in enumerate(dataset, start=1):
    file_path = output_dir / f"ticket_{i:03d}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(row, f, indent=4, ensure_ascii=False)

print(f"Saved {len(dataset)} JSON files to {output_dir}")


# Create output directory
output_dir = Path("raw_tickets_texts")
output_dir.mkdir(parents=True, exist_ok=True)


# Save each ticket as a separate TXT file
for i, row in enumerate(dataset, start=1):
    subject = row.get("subject") or ""
    body = row.get("body") or ""

    raw_ticket = f"Subject: {subject}\nBody: {body}"

    file_path = output_dir / f"raw_ticket_{i:03d}.txt"

    file_path.write_text(raw_ticket, encoding="utf-8")

print(f"Saved {len(dataset)} raw tickets to {output_dir}")
