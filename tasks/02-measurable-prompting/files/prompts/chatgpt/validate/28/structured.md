# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Tech Support Inquiry
Body: I am contacting you to ask about the integration possibilities for ClickUp within my existing technology infrastructure. Could you send me a detailed list of tools that are compatible with ClickUp and a short explanation of their integration features? Additionally, I would be grateful for any instructions on setting up these integrations and any supplementary materials you can provide.

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
  "subject": "Tech Support Inquiry",
  "body": "I am contacting you to ask about the integration possibilities for ClickUp within my existing technology infrastructure. Could you send me a detailed list of tools that are compatible with ClickUp and a short explanation of their integration features? Additionally, I would be grateful for any instructions on setting up these integrations and any supplementary materials you can provide.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
