## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Enhancing Security for Medical Data Transmission Systems
Body: Hello Customer Support, I am writing to inquire about enhancing security for the transmission and storage of medical data. Given the sensitive nature of medical information, it is crucial that it is protected with the highest level of security to safeguard patient details. Could you please share the current encryption methods used by your organization and the steps taken to ensure the secure handling of medical data? Additionally, are there plans to introduce further security enhancements, such as multi-factor authentication and encryption key management? Your insights on this matter would be greatly appreciated. Thank you for your time and cooperation. I eagerly await your response.

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


ANSWER: {"subject": "Enhancing Security for Medical Data Transmission Systems", "body": "Hello Customer Support, I am writing to inquire about enhancing security for the transmission and storage of medical data. Given the sensitive nature of medical information, it is crucial that it is protected with the highest level of security to safeguard patient details. Could you please share the current encryption methods used by your organization and the steps taken to ensure the secure handling of medical data? Additionally, are there plans to introduce further security enhancements, such as multi-factor authentication and encryption key management? Your insights on this matter would be greatly appreciated. Thank you for your time and cooperation. I eagerly await your response.", "type": "Request", "queue": "IT Support", "priority": "low", "language": "en"}
