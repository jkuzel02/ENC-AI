# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Support for Digital Marketing
Body: Request for enhancements in digital marketing tools integration to optimize software performance. Aim is to enable effective brand growth strategies and improve the overall customer experience. Appreciate if could look into this matter and provide a solution as soon as possible. Thank you for your time and assistance.

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
  "subject": "Support for Digital Marketing",
  "body": "Request for enhancements in digital marketing tools integration to optimize software performance. Aim is to enable effective brand growth strategies and improve the overall customer experience. Appreciate if could look into this matter and provide a solution as soon as possible. Thank you for your time and assistance.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
