# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Enquiries on Shopware Integrations with Google Cloud and Microsoft Azure
Body: Hello Customer Support, I am writing to inquire about the integrations that are currently available for Shopware with Google Cloud Platform and Microsoft Azure services. I am currently using Shopware as my e-commerce platform and I am keen to explore the integration opportunities with Google Cloud Platform and Microsoft Azure services. Would you be able to provide me with a detailed list of the available integrations and their descriptions? Furthermore, I would be grateful for any assistance in understanding how to set up and configure these integrations. Specifically, I am interested in knowing more about the integration with Google Cloud Storage, Google Cloud Functions, and Microsoft Azure Storage. Could you also inform me about any future plans for new integrations? Lastly, I would appreciate any insights into the limitations or restrictions on the use of these integrations. I look forward to your response and hope to receive detailed guidance on this matter. Thank you for your time and support. Kind regards, [Your Name]

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
  "subject": "Enquiries on Shopware Integrations with Google Cloud and Microsoft Azure",
  "body": "Hello Customer Support, I am writing to inquire about the integrations that are currently available for Shopware with Google Cloud Platform and Microsoft Azure services. I am currently using Shopware as my e-commerce platform and I am keen to explore the integration opportunities with Google Cloud Platform and Microsoft Azure services. Would you be able to provide me with a detailed list of the available integrations and their descriptions? Furthermore, I would be grateful for any assistance in understanding how to set up and configure these integrations. Specifically, I am interested in knowing more about the integration with Google Cloud Storage, Google Cloud Functions, and Microsoft Azure Storage. Could you also inform me about any future plans for new integrations? Lastly, I would appreciate any insights into the limitations or restrictions on the use of these integrations. I look forward to your response and hope to receive detailed guidance on this matter. Thank you for your time and support. Kind regards, [Your Name]",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
