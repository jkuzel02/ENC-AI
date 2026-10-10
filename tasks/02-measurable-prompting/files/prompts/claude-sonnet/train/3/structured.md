## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Security
Body: Dear Customer Support, I am reaching out to inquire about the security protocols you have in place to protect medical data. As a valued customer, I want to ensure that my sensitive health information is handled with the utmost care and confidentiality. Could you please provide me with information on the measures you take to safeguard medical data? Additionally, I would appreciate it if you could inform me about any certifications or compliances your company adheres to, such as HIPAA. I am also keen to know if you have any specific measures to prevent data breaches and unauthorized access. Thank you for your time and assistance. I look forward to your prompt response.

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


ANSWER: {"subject": "Security", "body": "Dear Customer Support, I am reaching out to inquire about the security protocols you have in place to protect medical data. As a valued customer, I want to ensure that my sensitive health information is handled with the utmost care and confidentiality. Could you please provide me with information on the measures you take to safeguard medical data? Additionally, I would appreciate it if you could inform me about any certifications or compliances your company adheres to, such as HIPAA. I am also keen to know if you have any specific measures to prevent data breaches and unauthorized access. Thank you for your time and assistance. I look forward to your prompt response.", "type": "Request", "queue": "IT Support", "priority": "low", "language": "en"}
