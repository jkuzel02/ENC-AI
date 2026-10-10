# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Slowness observed in the data analytics platform
Body: There has been a noticeable slowdown in the data analytics platform. It might be due to inadequate server resources. Despite restarting the servers and verifying the configurations, the problem continues.

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
  "subject": "Slowness observed in the data analytics platform",
  "body": "There has been a noticeable slowdown in the data analytics platform. It might be due to inadequate server resources. Despite restarting the servers and verifying the configurations, the problem continues.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
