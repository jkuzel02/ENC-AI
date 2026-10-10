## Role
You are a precise data extraction and classification assistant for IT and customer support tickets.

## Context
You have received a support ticket. Your task is to extract its fields verbatim and classify the ticket into the correct type, queue, and priority.

Subject: Guidance on Optimizing Investment Strategies Using Data Analytics
Body: Dear Customer Support, I am writing to request assistance in optimizing my investment strategies through the use of data analytics. The abundance of data available can be daunting, and I believe data analytics tools can aid in making more precise forecasts and maximizing returns. However, I need guidance on how to effectively use these tools. Could you provide me with some pointers on getting started? It would be greatly appreciated if you could recommend the most suitable data analytics tools for investment analysis, as well as offer tips on how to interpret the data and make informed decisions. Additionally, I would like to know if you have any resources or tutorials available that can help me learn more about data analytics and its application in investment strategies. I am very eager to learn more about this topic and appreciate your assistance in this matter. I look forward to your response. Best regards, [Your Name]

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

ANSWER: {"subject": "Guidance on Optimizing Investment Strategies Using Data Analytics", "body": "Dear Customer Support, I am writing to request assistance in optimizing my investment strategies through the use of data analytics. The abundance of data available can be daunting, and I believe data analytics tools can aid in making more precise forecasts and maximizing returns. However, I need guidance on how to effectively use these tools. Could you provide me with some pointers on getting started? It would be greatly appreciated if you could recommend the most suitable data analytics tools for investment analysis, as well as offer tips on how to interpret the data and make informed decisions. Additionally, I would like to know if you have any resources or tutorials available that can help me learn more about data analytics and its application in investment strategies. I am very eager to learn more about this topic and appreciate your assistance in this matter. I look forward to your response. Best regards, [Your Name]", "type": "Request", "queue": "Technical Support", "priority": "low", "language": "en"}
