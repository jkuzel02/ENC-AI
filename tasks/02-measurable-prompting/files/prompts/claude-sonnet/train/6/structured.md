## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Issue with Data Analytics Platform - Insufficient RAM Allocation
Body: I am reaching out to report an issue with our data analytics platform. The platform has crashed, and we believe it might be due to inadequate RAM allocation. We have already tried restarting the server and reviewing the logs, but the problem still exists. We kindly request your assistance in investigating this matter and providing a resolution at your earliest convenience. Please inform us if any additional information from our side is necessary to address this issue. The platform is currently unavailable, and we urgently need it to be operational. Thank you for your consideration and support.

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


ANSWER: {"subject": "Issue with Data Analytics Platform - Insufficient RAM Allocation", "body": "I am reaching out to report an issue with our data analytics platform. The platform has crashed, and we believe it might be due to inadequate RAM allocation. We have already tried restarting the server and reviewing the logs, but the problem still exists. We kindly request your assistance in investigating this matter and providing a resolution at your earliest convenience. Please inform us if any additional information from our side is necessary to address this issue. The platform is currently unavailable, and we urgently need it to be operational. Thank you for your consideration and support.", "type": "Incident", "queue": "Technical Support", "priority": "high", "language": "en"}
