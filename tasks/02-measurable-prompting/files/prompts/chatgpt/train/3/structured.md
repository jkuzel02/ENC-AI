# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Security
Body: Dear Customer Support, I am reaching out to inquire about the security protocols you have in place to protect medical data. As a valued customer, I want to ensure that my sensitive health information is handled with the utmost care and confidentiality. Could you please provide me with information on the measures you take to safeguard medical data? Additionally, I would appreciate it if you could inform me about any certifications or compliances your company adheres to, such as HIPAA. I am also keen to know if you have any specific measures to prevent data breaches and unauthorized access. Thank you for your time and assistance. I look forward to your prompt response.

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
  "subject": "Security",
  "body": "Dear Customer Support, I am reaching out to inquire about the security protocols you have in place to protect medical data. As a valued customer, I want to ensure that my sensitive health information is handled with the utmost care and confidentiality. Could you please provide me with information on the measures you take to safeguard medical data? Additionally, I would appreciate it if you could inform me about any certifications or compliances your company adheres to, such as HIPAA. I am also keen to know if you have any specific measures to prevent data breaches and unauthorized access. Thank you for your time and assistance. I look forward to your prompt response.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
