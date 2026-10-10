# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Support for Data Analytics Platform Crash
Body: The data analytics platform encountered issues while processing client investment reports due to high server load and software conflicts, despite restarting applications and checking for updates. The problem continues and requires your assistance.

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
  "subject": "Support for Data Analytics Platform Crash",
  "body": "The data analytics platform encountered issues while processing client investment reports due to high server load and software conflicts, despite restarting applications and checking for updates. The problem continues and requires your assistance.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
