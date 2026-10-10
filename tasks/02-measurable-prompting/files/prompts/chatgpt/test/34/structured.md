# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Support Request for Data Breach Issue
Body: There has been an unexpected data breach that may have compromised sensitive medical data. This is likely due to insufficient security measures and outdated software. Actions taken include securing the system, updating passwords, and monitoring network activity. Assistance is needed to ensure the necessary steps are taken to protect sensitive information and prevent future breaches.

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
  "subject": "Support Request for Data Breach Issue",
  "body": "There has been an unexpected data breach that may have compromised sensitive medical data. This is likely due to insufficient security measures and outdated software. Actions taken include securing the system, updating passwords, and monitoring network activity. Assistance is needed to ensure the necessary steps are taken to protect sensitive information and prevent future breaches.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
