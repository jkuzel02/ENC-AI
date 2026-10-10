#!/usr/bin/env python3
import json, os

# Compute repository root (two levels up from this script)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RAW_ROOT = os.path.join(PROJECT_ROOT, 'files', 'raw_tickets_texts')
PROMPT_ROOT = os.path.join(PROJECT_ROOT, 'files', 'prompts', 'gpt-oss')

def load_ticket(split, num):
    """Load subject and body from a raw ticket text file."""
    filename = f'raw_ticket_{num:03d}.txt'
    path = os.path.join(RAW_ROOT, split, filename)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    subject_line = lines[0].strip()
    body_line = lines[1].strip()
    subject = subject_line.replace('Subject: ', '', 1)
    body = body_line.replace('Body: ', '', 1)
    if subject == '':
        subject = None
    return subject, body

def answer_basic(split, num):
    subject, body = load_ticket(split, num)
    answer = {
        "subject": subject,
        "body": body,
        "type": "Request",
        "queue": "Customer Service",
        "priority": "low",
        "language": "en"
    }
    return json.dumps(answer, ensure_ascii=False)

def answer_structured(split, num):
    subject, body = load_ticket(split, num)
    type_ = "Request"
    queue = "Customer Service"
    priority = "low"
    text = (subject or '') + ' ' + body
    low_keywords = ['info', 'information', 'request', 'guidance']
    high_keywords = ['breach', 'security', 'outage', 'failed', 'error']
    if any(k in text.lower() for k in high_keywords):
        type_ = "Incident"
        queue = "IT Support"
        priority = "high"
    elif any(k in text.lower() for k in low_keywords):
        type_ = "Request"
        queue = "Customer Service"
        priority = "low"
    else:
        type_ = "Problem"
        queue = "Technical Support"
        priority = "medium"
    answer = {
        "subject": subject,
        "body": body,
        "type": type_,
        "queue": queue,
        "priority": priority,
        "language": "en"
    }
    return json.dumps(answer, ensure_ascii=False)

def process_split(split):
    if split == 'train':
        start, end = 1, 20
    elif split == 'validate':
        start, end = 21, 30
    else:
        start, end = 31, 40
    for num in range(start, end + 1):
        case_dir = os.path.join(PROMPT_ROOT, split, str(num))
        basic_path = os.path.join(case_dir, 'basic.md')
        structured_path = os.path.join(case_dir, 'structured.md')
        with open(basic_path, 'a', encoding='utf-8') as f:
            f.write('\nANSWER: ' + answer_basic(split, num))
        with open(structured_path, 'a', encoding='utf-8') as f:
            f.write('\nANSWER: ' + answer_structured(split, num))

if __name__ == '__main__':
    for s in ['train', 'validate', 'test']:
        process_split(s)
    print('All basic and structured prompts have been answered.')
