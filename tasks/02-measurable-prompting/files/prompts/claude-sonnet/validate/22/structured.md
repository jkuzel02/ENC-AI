## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Requirements for Wave Integration with Outlook 2021
Body: I am contacting you to seek information regarding the prerequisites for integrating Wave with Outlook 2021. Could you kindly furnish me with the essential details, including the minimum system specifications such as the operating system, processor speed, and memory capacity, to ensure a seamless integration process? Furthermore, are there any specific software or plugin prerequisites that need to be met? Additionally, it would be greatly appreciated if you could share any troubleshooting advice or typical issues that might occur during the integration. I am eagerly looking forward to your response and resolving this matter. Thank you for your time and support.

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


ANSWER: {"subject": "Requirements for Wave Integration with Outlook 2021", "body": "I am contacting you to seek information regarding the prerequisites for integrating Wave with Outlook 2021. Could you kindly furnish me with the essential details, including the minimum system specifications such as the operating system, processor speed, and memory capacity, to ensure a seamless integration process? Furthermore, are there any specific software or plugin prerequisites that need to be met? Additionally, it would be greatly appreciated if you could share any troubleshooting advice or typical issues that might occur during the integration. I am eagerly looking forward to your response and resolving this matter. Thank you for your time and support.", "type": "Request", "queue": "Technical Support", "priority": "low", "language": "en"}
