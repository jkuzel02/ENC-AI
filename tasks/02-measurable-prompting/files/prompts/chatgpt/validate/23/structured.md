# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Problem with Invoice
Body: I am encountering a problem with my invoice. The amount shown online is not accurate. I have attempted to resolve this by refreshing the page and signing out then back in, but the issue still exists. I believe it might be a technical error or a data synchronization issue. Can you please investigate this for me and give me a corrected invoice total?

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
  "subject": "Problem with Invoice",
  "body": "I am encountering a problem with my invoice. The amount shown online is not accurate. I have attempted to resolve this by refreshing the page and signing out then back in, but the issue still exists. I believe it might be a technical error or a data synchronization issue. Can you please investigate this for me and give me a corrected invoice total?",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
