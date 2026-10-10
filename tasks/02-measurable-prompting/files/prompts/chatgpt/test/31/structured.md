# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Digital Campaign Synchronization Problem Noted
Body: Hello Customer Support, <br>A digital campaign synchronization issue has been observed by me and I am reporting it here. <br>The issue surfaced after the recent software updates and configuration alterations. <br>Steps taken to troubleshoot include restarting the devices and verifying internet connectivity, but unfortunately, the issue still exists. <br>I kindly request you to examine the situation and offer a resolution at the earliest. <br>Please inform me if you need any further details from me for the resolution. <br>I am eagerly awaiting your response. <br>Thanks a lot for your attention and help. <br>Best regards, [Your Name]

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
  "subject": "Digital Campaign Synchronization Problem Noted",
  "body": "Hello Customer Support, <br>A digital campaign synchronization issue has been observed by me and I am reporting it here. <br>The issue surfaced after the recent software updates and configuration alterations. <br>Steps taken to troubleshoot include restarting the devices and verifying internet connectivity, but unfortunately, the issue still exists. <br>I kindly request you to examine the situation and offer a resolution at the earliest. <br>Please inform me if you need any further details from me for the resolution. <br>I am eagerly awaiting your response. <br>Thanks a lot for your attention and help. <br>Best regards, [Your Name]",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
