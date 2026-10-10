# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Best Practices for Securing Medical Data with Snagit and KNIME
Body: I am contacting you to seek advice on the secure management of medical data when utilizing Snagit and KNIME. Given the sensitive nature of the data, I am keen to adhere to all necessary security protocols. Could you offer guidance on the secure storage and transmission of medical images and data through these tools? Additionally, I would be grateful for any suggestions on encryption, access control, and compliance with applicable regulations. I appreciate your consideration and anticipation of your prompt response. I am eager to hear from you soon.

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
  "subject": "Best Practices for Securing Medical Data with Snagit and KNIME",
  "body": "I am contacting you to seek advice on the secure management of medical data when utilizing Snagit and KNIME. Given the sensitive nature of the data, I am keen to adhere to all necessary security protocols. Could you offer guidance on the secure storage and transmission of medical images and data through these tools? Additionally, I would be grateful for any suggestions on encryption, access control, and compliance with applicable regulations. I appreciate your consideration and anticipation of your prompt response. I am eager to hear from you soon.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
