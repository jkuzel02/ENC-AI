# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Strategies for Brand Expansion
Body: Hello Customer Support Team, I am writing to seek advice on digital methods that can aid in expanding my brand. In the current digital era, a robust online footprint is essential for business success. I am keen to learn about the strategies you suggest for boosting brand visibility and attracting more customers. Particularly, I am interested in exploring social media marketing, search engine optimization, and content development. I think applying the appropriate digital strategies could significantly advance my brand. Would you be able to offer some insights on this? I look forward to your response. Thanks for your time and support.

# Instructions/Tasks
Extract the ticket information into the required JSON structure.

# Constraints
- Preserve the original wording where possible.
- Do not fabricate information.
- Output must be valid JSON.

# Few-shot Examples
Example Input:
Subject: Example Subject
Body: Example body text.

Example Output:
{
  "subject": "Example Subject",
  "body": "Example body text.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}

# Expected Format of Output
```json
{
    "subject": "string | null",
    "body": "string",
    "type": "'Request' | 'Change' | 'Problem' | 'Incident'",
    "queue": "'Customer Service' | 'Technical Support' | 'IT Support' | 'Billing and Payments'",
    "priority": "'low' | 'medium' | 'high'",
    "language": "'en'",
}
```


ANSWER: {
  "subject": "Strategies for Brand Expansion",
  "body": "Hello Customer Support Team, I am writing to seek advice on digital methods that can aid in expanding my brand. In the current digital era, a robust online footprint is essential for business success. I am keen to learn about the strategies you suggest for boosting brand visibility and attracting more customers. Particularly, I am interested in exploring social media marketing, search engine optimization, and content development. I think applying the appropriate digital strategies could significantly advance my brand. Would you be able to offer some insights on this? I look forward to your response. Thanks for your time and support.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
