# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Issue with Website Analytics Dashboard
Body: Dear Customer Support, I am encountering a problem with my website analytics dashboard that is not updating. I believe there might be an issue with the API connection. I have already restarted the dashboard and verified my credentials, yet the problem still exists. Could you please investigate and offer a solution at your earliest convenience? If you require any additional information from me, please let me know. Thank you for your assistance, and I look forward to your response.

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
  "subject": "Issue with Website Analytics Dashboard",
  "body": "Dear Customer Support, I am encountering a problem with my website analytics dashboard that is not updating. I believe there might be an issue with the API connection. I have already restarted the dashboard and verified my credentials, yet the problem still exists. Could you please investigate and offer a solution at your earliest convenience? If you require any additional information from me, please let me know. Thank you for your assistance, and I look forward to your response.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
