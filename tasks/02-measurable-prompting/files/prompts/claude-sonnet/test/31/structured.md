## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Digital Campaign Synchronization Problem Noted
Body: Hello Customer Support, <br>A digital campaign synchronization issue has been observed by me and I am reporting it here. <br>The issue surfaced after the recent software updates and configuration alterations. <br>Steps taken to troubleshoot include restarting the devices and verifying internet connectivity, but unfortunately, the issue still exists. <br>I kindly request you to examine the situation and offer a resolution at the earliest. <br>Please inform me if you need any further details from me for the resolution. <br>I am eagerly awaiting your response. <br>Thanks a lot for your attention and help. <br>Best regards, [Your Name]

## Instructions / Tasks
Read the ticket subject and body carefully. Extract the required fields and classify the ticket according to the schema below. Use only the information present in the ticket. Do not invent or assume details not explicitly stated.

## Constraints
- Preserve the original wording of the subject and body exactly (do not paraphrase or correct).
- If the subject is empty or missing, set "subject" to null.
- Do not add fields beyond those in the schema.
- Output must be valid JSON only -- no Markdown fences, no explanations.
- Do not fabricate information not present in the ticket.
- Language must always be "en" for English tickets.

## Few-shot Example
**Input:**
Subject: Login Issue
Body: I cannot log into my account. I have reset my password twice but the issue persists.

**Output:**
{"subject": "Login Issue", "body": "I cannot log into my account. I have reset my password twice but the issue persists.", "type": "Problem", "queue": "Technical Support", "priority": "medium", "language": "en"}

## Expected Format of Output
Output exactly one valid JSON object with the following schema:

{
  "subject": "string | null",
  "body": "string",
  "type": "'Request' | 'Change' | 'Problem' | 'Incident'",
  "queue": "'Customer Service' | 'Technical Support' | 'IT Support' | 'Billing and Payments'",
  "priority": "'low' | 'medium' | 'high'",
  "language": "'en'"
}


ANSWER: {"subject": "Digital Campaign Synchronization Problem Noted", "body": "Hello Customer Support, <br>A digital campaign synchronization issue has been observed by me and I am reporting it here. <br>The issue surfaced after the recent software updates and configuration alterations. <br>Steps taken to troubleshoot include restarting the devices and verifying internet connectivity, but unfortunately, the issue still exists. <br>I kindly request you to examine the situation and offer a resolution at the earliest. <br>Please inform me if you need any further details from me for the resolution. <br>I am eagerly awaiting your response. <br>Thanks a lot for your attention and help. <br>Best regards, [Your Name]", "type": "Incident", "queue": "Technical Support", "priority": "medium", "language": "en"}
