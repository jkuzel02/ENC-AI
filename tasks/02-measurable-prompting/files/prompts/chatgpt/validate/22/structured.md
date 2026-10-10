# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Requirements for Wave Integration with Outlook 2021
Body: I am contacting you to seek information regarding the prerequisites for integrating Wave with Outlook 2021. Could you kindly furnish me with the essential details, including the minimum system specifications such as the operating system, processor speed, and memory capacity, to ensure a seamless integration process? Furthermore, are there any specific software or plugin prerequisites that need to be met? Additionally, it would be greatly appreciated if you could share any troubleshooting advice or typical issues that might occur during the integration. I am eagerly looking forward to your response and resolving this matter. Thank you for your time and support.

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
  "subject": "Requirements for Wave Integration with Outlook 2021",
  "body": "I am contacting you to seek information regarding the prerequisites for integrating Wave with Outlook 2021. Could you kindly furnish me with the essential details, including the minimum system specifications such as the operating system, processor speed, and memory capacity, to ensure a seamless integration process? Furthermore, are there any specific software or plugin prerequisites that need to be met? Additionally, it would be greatly appreciated if you could share any troubleshooting advice or typical issues that might occur during the integration. I am eagerly looking forward to your response and resolving this matter. Thank you for your time and support.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
