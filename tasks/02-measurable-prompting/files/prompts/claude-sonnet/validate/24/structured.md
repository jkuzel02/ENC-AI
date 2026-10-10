## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Enquiries on Shopware Integrations with Google Cloud and Microsoft Azure
Body: Hello Customer Support, I am writing to inquire about the integrations that are currently available for Shopware with Google Cloud Platform and Microsoft Azure services. I am currently using Shopware as my e-commerce platform and I am keen to explore the integration opportunities with Google Cloud Platform and Microsoft Azure services. Would you be able to provide me with a detailed list of the available integrations and their descriptions? Furthermore, I would be grateful for any assistance in understanding how to set up and configure these integrations. Specifically, I am interested in knowing more about the integration with Google Cloud Storage, Google Cloud Functions, and Microsoft Azure Storage. Could you also inform me about any future plans for new integrations? Lastly, I would appreciate any insights into the limitations or restrictions on the use of these integrations. I look forward to your response and hope to receive detailed guidance on this matter. Thank you for your time and support. Kind regards, [Your Name]

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


ANSWER: {"subject": "Enquiries on Shopware Integrations with Google Cloud and Microsoft Azure", "body": "Hello Customer Support, I am writing to inquire about the integrations that are currently available for Shopware with Google Cloud Platform and Microsoft Azure services. I am currently using Shopware as my e-commerce platform and I am keen to explore the integration opportunities with Google Cloud Platform and Microsoft Azure services. Would you be able to provide me with a detailed list of the available integrations and their descriptions? Furthermore, I would be grateful for any assistance in understanding how to set up and configure these integrations. Specifically, I am interested in knowing more about the integration with Google Cloud Storage, Google Cloud Functions, and Microsoft Azure Storage. Could you also inform me about any future plans for new integrations? Lastly, I would appreciate any insights into the limitations or restrictions on the use of these integrations. I look forward to your response and hope to receive detailed guidance on this matter. Thank you for your time and support. Kind regards, [Your Name]", "type": "Request", "queue": "Technical Support", "priority": "low", "language": "en"}
