## Role
You are a precise data extraction and classification assistant for IT and customer support tickets.

## Context
You have received a support ticket. Your task is to extract its fields verbatim and classify the ticket into the correct type, queue, and priority.

Subject: Reported Issue with Project Sync Resulting in Data Loss
Body: Dear Customer Support,\n\nI am reporting an issue with our project sync, which has led to data loss. This sync failure occurred after recent software updates, possibly due to incompatibility issues. Despite restarting our systems and reviewing firewall settings, the problem remains unresolved.\n\nThe software updates were installed recently, and the sync failure happened shortly thereafter. Our team has attempted to troubleshoot the issue by restarting the systems and reviewing the firewall settings, but these efforts have been unsuccessful.\n\nI would greatly appreciate it if you could investigate this matter and provide a solution to resolve the sync issue and recover the lost data. If there is any additional information or logs you require from our side, please let me know.\n\nThank you for your time and assistance.\n\nBest regards,\n[Your Name]

## Classification Guidance

### Type
Classify the ticket as exactly one of the following, based on the ticket content:
- **Incident**: An active disruption, outage, breach, crash, or data loss that is currently happening.
- **Problem**: A recurring or persistent issue whose root cause is unclear, degrading service but not a full outage.
- **Change**: A formal request to modify, update, or enhance a system, configuration, or integration.
- **Request**: A request for information, guidance, advice, recommendations, or new capabilities (no active failure).

If the ticket is ambiguous between Incident and Problem, prefer Incident when there is an active, ongoing service disruption.
If the ticket is ambiguous between Request and Change, prefer Change when the user explicitly asks for a modification to be made.

### Queue
- **Customer Service**: Brand, marketing, digital strategy, customer experience topics.
- **Technical Support**: Software, integrations, APIs, analytics platforms, devices, connectivity.
- **IT Support**: Security, medical data protection, encryption, access control, HIPAA compliance, hospital/network infrastructure.
- **Billing and Payments**: Invoices, pricing, billing plans, payment methods, charges.

### Priority
- **high**: Urgent, active outage, data breach, data loss, system unavailable, or explicitly marked urgent.
- **medium**: Ongoing degraded performance, intermittent issues, moderate impact, no urgency stated.
- **low**: Information requests, best practices, general inquiries, no active failure.


### Special Handling Note
EDGE CASE: Body contains literal escape sequences (\n) that must be preserved as-is in the JSON string (encoded as \\n). Do not interpret them as actual newlines.

## Instructions
1. Copy the subject and body fields exactly from the ticket without paraphrasing or correcting.
2. If the subject field is empty or absent, set "subject" to 
ull (JSON null, not the string "null").
3. Preserve all special characters, HTML tags, escape sequences, and placeholders in the body exactly as they appear.
4. Classify the ticket using the guidance above.
5. Output exactly one valid JSON object. No explanation, no Markdown fences, no extra fields.

## Few-shot Example
**Input:**
Subject: Login Issue
Body: I cannot log into my account. I have reset my password twice but the issue persists.

**Output:**
{"subject": "Login Issue", "body": "I cannot log into my account. I have reset my password twice but the issue persists.", "type": "Problem", "queue": "Technical Support", "priority": "medium", "language": "en"}

## Output Schema
{
  "subject": "string | null",
  "body": "string",
  "type": "Request | Change | Problem | Incident",
  "queue": "Customer Service | Technical Support | IT Support | Billing and Payments",
  "priority": "low | medium | high",
  "language": "en"
}

ANSWER: {"subject": "Reported Issue with Project Sync Resulting in Data Loss", "body": "Dear Customer Support,\\n\\nI am reporting an issue with our project sync, which has led to data loss. This sync failure occurred after recent software updates, possibly due to incompatibility issues. Despite restarting our systems and reviewing firewall settings, the problem remains unresolved.\\n\\nThe software updates were installed recently, and the sync failure happened shortly thereafter. Our team has attempted to troubleshoot the issue by restarting the systems and reviewing the firewall settings, but these efforts have been unsuccessful.\\n\\nI would greatly appreciate it if you could investigate this matter and provide a solution to resolve the sync issue and recover the lost data. If there is any additional information or logs you require from our side, please let me know.\\n\\nThank you for your time and assistance.\\n\\nBest regards,\\n[Your Name]", "type": "Incident", "queue": "Technical Support", "priority": "high", "language": "en"}
