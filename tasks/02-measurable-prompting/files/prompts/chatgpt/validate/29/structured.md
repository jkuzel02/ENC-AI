# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Support for Expanding a Brand
Body: Seeking information on digital marketing tactics for brand growth. Please provide specifics on the services you offer.

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
  "subject": "Support for Expanding a Brand",
  "body": "Seeking information on digital marketing tactics for brand growth. Please provide specifics on the services you offer.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
