# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Request for Assistance with Data Integration
Body: We are encountering data integration problems while optimizing investments using analytics tools. These issues might be due to unexpected software compatibility problems between various applications. Despite updating the software and checking for configuration errors, the problem continues. We would greatly appreciate your guidance in resolving this matter to ensure a smooth data flow and accurate analysis. Please inform us of the next steps to address this issue.

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
  "subject": "Request for Assistance with Data Integration",
  "body": "We are encountering data integration problems while optimizing investments using analytics tools. These issues might be due to unexpected software compatibility problems between various applications. Despite updating the software and checking for configuration errors, the problem continues. We would greatly appreciate your guidance in resolving this matter to ensure a smooth data flow and accurate analysis. Please inform us of the next steps to address this issue.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
