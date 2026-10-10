# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Problem with SQL Server Downtime
Body: Faced an SQL Server outage that disrupted data analytics processing, impacting investment optimization. The outage might be due to high query loads on the server. Restarted the SQL Service and reviewed the server logs for any errors.

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
  "subject": "Problem with SQL Server Downtime",
  "body": "Faced an SQL Server outage that disrupted data analytics processing, impacting investment optimization. The outage might be due to high query loads on the server. Restarted the SQL Service and reviewed the server logs for any errors.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
