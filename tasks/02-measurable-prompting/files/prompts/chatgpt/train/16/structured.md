# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Urgent: Update Encryption Protocols for JIRA and HubSpot CRM Systems
Body: Hello customer support, I am contacting you to highlight the urgent requirement to enhance encryption protocols on our JIRA and HubSpot CRM systems in order to secure medical data effectively. This update is vital for safeguarding sensitive information and ensuring adherence to regulatory standards. Could you please undertake these updates as soon as possible and notify me upon completion? If you need any more details from me, please let me know.

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
  "subject": "Urgent: Update Encryption Protocols for JIRA and HubSpot CRM Systems",
  "body": "Hello customer support, I am contacting you to highlight the urgent requirement to enhance encryption protocols on our JIRA and HubSpot CRM systems in order to secure medical data effectively. This update is vital for safeguarding sensitive information and ensuring adherence to regulatory standards. Could you please undertake these updates as soon as possible and notify me upon completion? If you need any more details from me, please let me know.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
