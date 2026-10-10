# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Support Needed
Body: Customer Support, facing issues with unauthorized access attempts to medical data in my report. The problems might be due to outdated security protocols. Despite efforts to enhance encryption and update system settings, these measures have been unsuccessful. I would greatly appreciate some guidance to resolve the issue and prevent similar occurrences in the future. Please let me know the next steps to take. Thank you for your assistance, and I look forward to hearing from you soon.

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
  "subject": "Support Needed",
  "body": "Customer Support, facing issues with unauthorized access attempts to medical data in my report. The problems might be due to outdated security protocols. Despite efforts to enhance encryption and update system settings, these measures have been unsuccessful. I would greatly appreciate some guidance to resolve the issue and prevent similar occurrences in the future. Please let me know the next steps to take. Thank you for your assistance, and I look forward to hearing from you soon.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
