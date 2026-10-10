# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Concerns About Securing Medical Data on 2-in-1 Convertible Laptop with Norton 360
Body: Inquiring about best practices for securing medical data on a 2-in-1 Convertible Laptop. Currently have Norton 360 installed and need guidance on how to properly configure it to protect sensitive medical information. Would greatly appreciate any tips or recommendations you can offer.

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
  "subject": "Concerns About Securing Medical Data on 2-in-1 Convertible Laptop with Norton 360",
  "body": "Inquiring about best practices for securing medical data on a 2-in-1 Convertible Laptop. Currently have Norton 360 installed and need guidance on how to properly configure it to protect sensitive medical information. Would greatly appreciate any tips or recommendations you can offer.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
