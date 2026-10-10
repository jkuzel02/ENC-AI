# Persona/Role
You are a data extraction assistant.

# Context/State
Subject: Data Analytics for Investment
Body: I am contacting you to request information on data analytics tools that can be utilized with the Eclipse IDE for enhancing investment optimization. I am seeking suggestions for tools that can aid in making data-driven decisions. Particularly, I am interested in tools that can manage large datasets and offer advanced analytics features. These tools should be compatible with the Eclipse IDE and can smoothly integrate into my workflow. Key features I am interested in include data visualization, predictive modeling, and machine learning capabilities. I would greatly appreciate any recommendations or advice on how to begin with data analytics for investment optimization using the Eclipse IDE.

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
  "subject": "Data Analytics for Investment",
  "body": "I am contacting you to request information on data analytics tools that can be utilized with the Eclipse IDE for enhancing investment optimization. I am seeking suggestions for tools that can aid in making data-driven decisions. Particularly, I am interested in tools that can manage large datasets and offer advanced analytics features. These tools should be compatible with the Eclipse IDE and can smoothly integrate into my workflow. Key features I am interested in include data visualization, predictive modeling, and machine learning capabilities. I would greatly appreciate any recommendations or advice on how to begin with data analytics for investment optimization using the Eclipse IDE.",
  "type": "Request",
  "queue": "Customer Service",
  "priority": "low",
  "language": "en"
}
