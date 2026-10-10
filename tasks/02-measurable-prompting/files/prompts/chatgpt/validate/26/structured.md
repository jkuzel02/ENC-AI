# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Expansion of Digital Brand
Body: Customer support, reaching out for inquiries about digital strategy services to aid in brand growth. Would appreciate detailed information and pricing for the services offered. Thank you for your assistance, and I look forward to hearing back soon.

# Instructions/Tasks
Extract the ticket information into the required JSON structure.

# Constraints
- Preserve the original wording where possible.
- Do not fabricate information.
- Output must be valid JSON.

# Few-shot Examples
Example Input:
Subject: Example Subject
Body: Example body text.

Example Output:
{
  "subject": "Example Subject",
  "body": "Example body text.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}

# Expected Format of Output
```json
{
    "subject": "string | null",
    "body": "string",
    "type": "'Request' | 'Change' | 'Problem' | 'Incident'",
    "queue": "'Customer Service' | 'Technical Support' | 'IT Support' | 'Billing and Payments'",
    "priority": "'low' | 'medium' | 'high'",
    "language": "'en'",
}
```


ANSWER: {
  "subject": "Expansion of Digital Brand",
  "body": "Customer support, reaching out for inquiries about digital strategy services to aid in brand growth. Would appreciate detailed information and pricing for the services offered. Thank you for your assistance, and I look forward to hearing back soon.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
