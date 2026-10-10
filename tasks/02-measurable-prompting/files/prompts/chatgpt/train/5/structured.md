# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Problem with Integration
Body: The integration stopped working unexpectedly, causing synchronization errors between our platforms. This might be due to recent modifications to the API. Despite attempting to restart services and examining logs, the problem remains unresolved. I would be grateful for your help in addressing this issue.

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
  "subject": "Problem with Integration",
  "body": "The integration stopped working unexpectedly, causing synchronization errors between our platforms. This might be due to recent modifications to the API. Despite attempting to restart services and examining logs, the problem remains unresolved. I would be grateful for your help in addressing this issue.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
