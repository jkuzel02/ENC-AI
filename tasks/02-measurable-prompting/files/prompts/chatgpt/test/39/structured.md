# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Strategies for Enhancing Digital Brand Growth
Body: I hope this message finds you well. I am interested in learning about effective digital strategies that can help boost brand growth and engagement for businesses. Could you share some insights or recommendations on this matter? Your input would be greatly appreciated.

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
  "subject": "Strategies for Enhancing Digital Brand Growth",
  "body": "I hope this message finds you well. I am interested in learning about effective digital strategies that can help boost brand growth and engagement for businesses. Could you share some insights or recommendations on this matter? Your input would be greatly appreciated.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
