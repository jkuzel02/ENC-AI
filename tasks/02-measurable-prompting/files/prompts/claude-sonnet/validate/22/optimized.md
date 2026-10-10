## Role
You are a precise data extraction and classification assistant for IT and customer support tickets.

## Context
You have received a support ticket. Your task is to extract its fields verbatim and classify the ticket into the correct type, queue, and priority.

Subject: Requirements for Wave Integration with Outlook 2021
Body: I am contacting you to seek information regarding the prerequisites for integrating Wave with Outlook 2021. Could you kindly furnish me with the essential details, including the minimum system specifications such as the operating system, processor speed, and memory capacity, to ensure a seamless integration process? Furthermore, are there any specific software or plugin prerequisites that need to be met? Additionally, it would be greatly appreciated if you could share any troubleshooting advice or typical issues that might occur during the integration. I am eagerly looking forward to your response and resolving this matter. Thank you for your time and support.

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

ANSWER: {"subject": "Requirements for Wave Integration with Outlook 2021", "body": "I am contacting you to seek information regarding the prerequisites for integrating Wave with Outlook 2021. Could you kindly furnish me with the essential details, including the minimum system specifications such as the operating system, processor speed, and memory capacity, to ensure a seamless integration process? Furthermore, are there any specific software or plugin prerequisites that need to be met? Additionally, it would be greatly appreciated if you could share any troubleshooting advice or typical issues that might occur during the integration. I am eagerly looking forward to your response and resolving this matter. Thank you for your time and support.", "type": "Request", "queue": "Technical Support", "priority": "low", "language": "en"}
