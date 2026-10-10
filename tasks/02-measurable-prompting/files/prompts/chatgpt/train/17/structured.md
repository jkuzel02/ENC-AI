# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Guidelines for Securing Medical Data on macOS Systems with Symantec Endpoint Protection
Body: Could you provide guidelines on securing medical data on macOS systems using Symantec Endpoint Protection? Thank you for your assistance.

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
  "subject": "Guidelines for Securing Medical Data on macOS Systems with Symantec Endpoint Protection",
  "body": "Could you provide guidelines on securing medical data on macOS systems using Symantec Endpoint Protection? Thank you for your assistance.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
