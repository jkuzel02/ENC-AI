## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Support for QuickBooks
Body: I am seeking information on billing options and the integration of the QuickBooks Online SaaS platform. Could you provide details on the available plans and pricing? I would appreciate it if you could explain the benefits of each plan and how they cater to different business needs. Additionally, I would like to know if there are any discounts available for long-term commitments and if a free trial period is offered. Please let me know the necessary information to assist with my inquiry.

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


ANSWER: {"subject": "Support for QuickBooks", "body": "I am seeking information on billing options and the integration of the QuickBooks Online SaaS platform. Could you provide details on the available plans and pricing? I would appreciate it if you could explain the benefits of each plan and how they cater to different business needs. Additionally, I would like to know if there are any discounts available for long-term commitments and if a free trial period is offered. Please let me know the necessary information to assist with my inquiry.", "type": "Request", "queue": "Billing and Payments", "priority": "low", "language": "en"}
