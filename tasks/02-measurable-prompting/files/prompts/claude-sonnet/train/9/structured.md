## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Issue with Website Analytics Dashboard
Body: Dear Customer Support, I am encountering a problem with my website analytics dashboard that is not updating. I believe there might be an issue with the API connection. I have already restarted the dashboard and verified my credentials, yet the problem still exists. Could you please investigate and offer a solution at your earliest convenience? If you require any additional information from me, please let me know. Thank you for your assistance, and I look forward to your response.

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


ANSWER: {"subject": "Issue with Website Analytics Dashboard", "body": "Dear Customer Support, I am encountering a problem with my website analytics dashboard that is not updating. I believe there might be an issue with the API connection. I have already restarted the dashboard and verified my credentials, yet the problem still exists. Could you please investigate and offer a solution at your earliest convenience? If you require any additional information from me, please let me know. Thank you for your assistance, and I look forward to your response.", "type": "Problem", "queue": "Technical Support", "priority": "medium", "language": "en"}
