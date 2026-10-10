# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Problem with Data Analytics Software Frequent Crashes
Body: The data analytics software used by the financial firm is experiencing frequent crashes, likely due to RAM limitations and software conflicts.

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
  "subject": "Problem with Data Analytics Software Frequent Crashes",
  "body": "The data analytics software used by the financial firm is experiencing frequent crashes, likely due to RAM limitations and software conflicts.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
