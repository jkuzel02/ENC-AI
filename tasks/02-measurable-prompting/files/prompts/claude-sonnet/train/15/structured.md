## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: (empty)
Body: To Whom It May Concern, I am contacting you to report a possible data breach, which may be related to outdated software. Despite my attempts to update various programs, including Snagit, Ansible, and Firebase, the problem continues. I am worried about the security of my data and would appreciate your help in addressing this issue promptly. Could you advise on the next steps or suggest a solution to prevent future breaches? I value your swift response to this matter and eagerly await your guidance. Please inform me if you require any further information to assist me. I can be reached at your convenience to discuss this further. Thank you for your support in resolving this issue. Please provide any necessary reference number <ref_num> for my records, and I look forward to your prompt follow-up.

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


ANSWER: {"subject": null, "body": "To Whom It May Concern, I am contacting you to report a possible data breach, which may be related to outdated software. Despite my attempts to update various programs, including Snagit, Ansible, and Firebase, the problem continues. I am worried about the security of my data and would appreciate your help in addressing this issue promptly. Could you advise on the next steps or suggest a solution to prevent future breaches? I value your swift response to this matter and eagerly await your guidance. Please inform me if you require any further information to assist me. I can be reached at your convenience to discuss this further. Thank you for your support in resolving this issue. Please provide any necessary reference number <ref_num> for my records, and I look forward to your prompt follow-up.", "type": "Incident", "queue": "IT Support", "priority": "high", "language": "en"}
