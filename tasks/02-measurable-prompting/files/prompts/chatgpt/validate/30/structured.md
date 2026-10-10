# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Update Integration Settings for Compatibility
Body: Customer support, requesting an update to the integration settings for various software tools to enhance compatibility with our scalable SaaS platform. The current settings, although optimized, are causing issues with data synchronization. I would greatly appreciate your assistance in updating these settings as soon as possible. Please let me know the necessary information so we can proceed.

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
  "subject": "Update Integration Settings for Compatibility",
  "body": "Customer support, requesting an update to the integration settings for various software tools to enhance compatibility with our scalable SaaS platform. The current settings, although optimized, are causing issues with data synchronization. I would greatly appreciate your assistance in updating these settings as soon as possible. Please let me know the necessary information so we can proceed.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
