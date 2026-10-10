## Persona / Role
You are a data extraction assistant specializing in IT and customer support ticket classification.

## Context / State
You have received a support ticket. Extract its fields and classify it accurately.

Subject: Guidance on Optimizing Investment Strategies Using Data Analytics
Body: Dear Customer Support, I am writing to request assistance in optimizing my investment strategies through the use of data analytics. The abundance of data available can be daunting, and I believe data analytics tools can aid in making more precise forecasts and maximizing returns. However, I need guidance on how to effectively use these tools. Could you provide me with some pointers on getting started? It would be greatly appreciated if you could recommend the most suitable data analytics tools for investment analysis, as well as offer tips on how to interpret the data and make informed decisions. Additionally, I would like to know if you have any resources or tutorials available that can help me learn more about data analytics and its application in investment strategies. I am very eager to learn more about this topic and appreciate your assistance in this matter. I look forward to your response. Best regards, [Your Name]

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


ANSWER: {"subject": "Guidance on Optimizing Investment Strategies Using Data Analytics", "body": "Dear Customer Support, I am writing to request assistance in optimizing my investment strategies through the use of data analytics. The abundance of data available can be daunting, and I believe data analytics tools can aid in making more precise forecasts and maximizing returns. However, I need guidance on how to effectively use these tools. Could you provide me with some pointers on getting started? It would be greatly appreciated if you could recommend the most suitable data analytics tools for investment analysis, as well as offer tips on how to interpret the data and make informed decisions. Additionally, I would like to know if you have any resources or tutorials available that can help me learn more about data analytics and its application in investment strategies. I am very eager to learn more about this topic and appreciate your assistance in this matter. I look forward to your response. Best regards, [Your Name]", "type": "Request", "queue": "Technical Support", "priority": "low", "language": "en"}
