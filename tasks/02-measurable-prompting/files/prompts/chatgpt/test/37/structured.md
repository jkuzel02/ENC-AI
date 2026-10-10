# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Technical Help
Body: The scanner is not functioning correctly because of old drivers and recent macOS updates. Despite efforts to restart, update software, and reinstall drivers, the problem remains unresolved.

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
  "subject": "Technical Help",
  "body": "The scanner is not functioning correctly because of old drivers and recent macOS updates. Despite efforts to restart, update software, and reinstall drivers, the problem remains unresolved.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
