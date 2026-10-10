# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Enhancing Security for Medical Data Transmission Systems
Body: Hello Customer Support, I am writing to inquire about enhancing security for the transmission and storage of medical data. Given the sensitive nature of medical information, it is crucial that it is protected with the highest level of security to safeguard patient details. Could you please share the current encryption methods used by your organization and the steps taken to ensure the secure handling of medical data? Additionally, are there plans to introduce further security enhancements, such as multi-factor authentication and encryption key management? Your insights on this matter would be greatly appreciated. Thank you for your time and cooperation. I eagerly await your response.

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
  "subject": "Enhancing Security for Medical Data Transmission Systems",
  "body": "Hello Customer Support, I am writing to inquire about enhancing security for the transmission and storage of medical data. Given the sensitive nature of medical information, it is crucial that it is protected with the highest level of security to safeguard patient details. Could you please share the current encryption methods used by your organization and the steps taken to ensure the secure handling of medical data? Additionally, are there plans to introduce further security enhancements, such as multi-factor authentication and encryption key management? Your insights on this matter would be greatly appreciated. Thank you for your time and cooperation. I eagerly await your response.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
