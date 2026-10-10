import json
from pathlib import Path
from datasets import load_dataset


# https://huggingface.co/datasets/mihalachecostindaniel/ticket-triage-data
# Load only the first 40 rows
dataset = load_dataset(
    "mihalachecostindaniel/ticket-triage-data",
    split="train[:40]"
)


# Export the first 20 tickets for training, the next 10 for validation,
# and the last 10 for testing. Preserve the original ticket numbers.
json_output_dir = Path("ticket_triage_json")
text_output_dir = Path("raw_tickets_texts")
json_fields = ("subject", "body", "type", "queue", "priority", "language")
splits = (("train", 0, 20), ("validate", 20, 30), ("test", 30, 40))

for split_name, start, end in splits:
    json_dir = json_output_dir / split_name
    text_dir = text_output_dir / split_name
    json_dir.mkdir(parents=True, exist_ok=True)
    text_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    for index in range(start, min(end, len(dataset))):
        row = dataset[index]
        ticket_number = index + 1
        ticket = {field: row.get(field) for field in json_fields}

        file_path = json_dir / f"ticket_{ticket_number:03d}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(ticket, f, indent=4, ensure_ascii=False)

        subject = row.get("subject") or ""
        body = row.get("body") or ""
        raw_ticket = f"Subject: {subject}\nBody: {body}"

        file_path = text_dir / f"raw_ticket_{ticket_number:03d}.txt"
        file_path.write_text(raw_ticket, encoding="utf-8")
        count += 1

    print(f"Saved {count} JSON files to {json_dir}")
    print(f"Saved {count} raw tickets to {text_dir}")
