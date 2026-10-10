# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Support for QuickBooks
Body: I am seeking information on billing options and the integration of the QuickBooks Online SaaS platform. Could you provide details on the available plans and pricing? I would appreciate it if you could explain the benefits of each plan and how they cater to different business needs. Additionally, I would like to know if there are any discounts available for long-term commitments and if a free trial period is offered. Please let me know the necessary information to assist with my inquiry.

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
  "subject": "Support for QuickBooks",
  "body": "I am seeking information on billing options and the integration of the QuickBooks Online SaaS platform. Could you provide details on the available plans and pricing? I would appreciate it if you could explain the benefits of each plan and how they cater to different business needs. Additionally, I would like to know if there are any discounts available for long-term commitments and if a free trial period is offered. Please let me know the necessary information to assist with my inquiry.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
