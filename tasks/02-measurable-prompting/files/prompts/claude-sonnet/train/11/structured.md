## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Request for Assistance with Data Integration
Body: We are encountering data integration problems while optimizing investments using analytics tools. These issues might be due to unexpected software compatibility problems between various applications. Despite updating the software and checking for configuration errors, the problem continues. We would greatly appreciate your guidance in resolving this matter to ensure a smooth data flow and accurate analysis. Please inform us of the next steps to address this issue.

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


ANSWER: {"subject": "Request for Assistance with Data Integration", "body": "We are encountering data integration problems while optimizing investments using analytics tools. These issues might be due to unexpected software compatibility problems between various applications. Despite updating the software and checking for configuration errors, the problem continues. We would greatly appreciate your guidance in resolving this matter to ensure a smooth data flow and accurate analysis. Please inform us of the next steps to address this issue.", "type": "Problem", "queue": "Technical Support", "priority": "medium", "language": "en"}
