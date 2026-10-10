## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Strategies for Brand Expansion
Body: Hello Customer Support Team, I am writing to seek advice on digital methods that can aid in expanding my brand. In the current digital era, a robust online footprint is essential for business success. I am keen to learn about the strategies you suggest for boosting brand visibility and attracting more customers. Particularly, I am interested in exploring social media marketing, search engine optimization, and content development. I think applying the appropriate digital strategies could significantly advance my brand. Would you be able to offer some insights on this? I look forward to your response. Thanks for your time and support.

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


ANSWER: {"subject": "Strategies for Brand Expansion", "body": "Hello Customer Support Team, I am writing to seek advice on digital methods that can aid in expanding my brand. In the current digital era, a robust online footprint is essential for business success. I am keen to learn about the strategies you suggest for boosting brand visibility and attracting more customers. Particularly, I am interested in exploring social media marketing, search engine optimization, and content development. I think applying the appropriate digital strategies could significantly advance my brand. Would you be able to offer some insights on this? I look forward to your response. Thanks for your time and support.", "type": "Request", "queue": "Customer Service", "priority": "low", "language": "en"}
