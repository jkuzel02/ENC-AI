## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Reported Issue with Project Sync Resulting in Data Loss
Body: Dear Customer Support,\n\nI am reporting an issue with our project sync, which has led to data loss. This sync failure occurred after recent software updates, possibly due to incompatibility issues. Despite restarting our systems and reviewing firewall settings, the problem remains unresolved.\n\nThe software updates were installed recently, and the sync failure happened shortly thereafter. Our team has attempted to troubleshoot the issue by restarting the systems and reviewing the firewall settings, but these efforts have been unsuccessful.\n\nI would greatly appreciate it if you could investigate this matter and provide a solution to resolve the sync issue and recover the lost data. If there is any additional information or logs you require from our side, please let me know.\n\nThank you for your time and assistance.\n\nBest regards,\n[Your Name]

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


ANSWER: {"subject": "Reported Issue with Project Sync Resulting in Data Loss", "body": "Dear Customer Support,\\n\\nI am reporting an issue with our project sync, which has led to data loss. This sync failure occurred after recent software updates, possibly due to incompatibility issues. Despite restarting our systems and reviewing firewall settings, the problem remains unresolved.\\n\\nThe software updates were installed recently, and the sync failure happened shortly thereafter. Our team has attempted to troubleshoot the issue by restarting the systems and reviewing the firewall settings, but these efforts have been unsuccessful.\\n\\nI would greatly appreciate it if you could investigate this matter and provide a solution to resolve the sync issue and recover the lost data. If there is any additional information or logs you require from our side, please let me know.\\n\\nThank you for your time and assistance.\\n\\nBest regards,\\n[Your Name]", "type": "Incident", "queue": "Technical Support", "priority": "high", "language": "en"}
