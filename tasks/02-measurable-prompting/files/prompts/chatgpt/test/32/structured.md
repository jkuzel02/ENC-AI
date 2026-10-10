# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: 
Body: During the last deployment, users encountered notable performance issues with the application. This might be due to unoptimized code introduced in the latest update. We have already restarted the servers and rolled back the update, but the problems continue. The team is currently actively investigating the cause and working on a solution to restore optimal performance.

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
  "subject": null,
  "body": "During the last deployment, users encountered notable performance issues with the application. This might be due to unoptimized code introduced in the latest update. We have already restarted the servers and rolled back the update, but the problems continue. The team is currently actively investigating the cause and working on a solution to restore optimal performance.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
