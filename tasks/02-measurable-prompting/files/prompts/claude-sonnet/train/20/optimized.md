## Role
You are a precise data extraction and classification assistant for IT and customer support tickets.

## Context
You have received a support ticket. Your task is to extract its fields verbatim and classify the ticket into the correct type, queue, and priority.

Subject: Best Practices for Securing Medical Data with Snagit and KNIME
Body: I am contacting you to seek advice on the secure management of medical data when utilizing Snagit and KNIME. Given the sensitive nature of the data, I am keen to adhere to all necessary security protocols. Could you offer guidance on the secure storage and transmission of medical images and data through these tools? Additionally, I would be grateful for any suggestions on encryption, access control, and compliance with applicable regulations. I appreciate your consideration and anticipation of your prompt response. I am eager to hear from you soon.

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

ANSWER: {"subject": "Best Practices for Securing Medical Data with Snagit and KNIME", "body": "I am contacting you to seek advice on the secure management of medical data when utilizing Snagit and KNIME. Given the sensitive nature of the data, I am keen to adhere to all necessary security protocols. Could you offer guidance on the secure storage and transmission of medical images and data through these tools? Additionally, I would be grateful for any suggestions on encryption, access control, and compliance with applicable regulations. I appreciate your consideration and anticipation of your prompt response. I am eager to hear from you soon.", "type": "Request", "queue": "IT Support", "priority": "low", "language": "en"}
