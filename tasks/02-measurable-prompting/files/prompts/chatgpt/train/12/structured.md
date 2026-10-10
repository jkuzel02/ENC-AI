# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Request for Updating Integration Features on Mobile
Body: I am writing to request an update to the integration features in our mobile applications. The current features are outdated and not compatible with recent software versions. I would like to request enhancements to ensure seamless functionality with the latest software versions.

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
  "subject": "Request for Updating Integration Features on Mobile",
  "body": "I am writing to request an update to the integration features in our mobile applications. The current features are outdated and not compatible with recent software versions. I would like to request enhancements to ensure seamless functionality with the latest software versions.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
