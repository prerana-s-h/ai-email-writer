# ai-email-writer

# AI Email Writer

AI Email Writer is a Streamlit-based application that generates professional emails using AI.

## Features

- Generate professional emails
- Multiple tone options
- Rewrite existing emails
- Analyze readability
- Generate follow-up sequences
- Subject line generation

## Tech Stack

- Python
- Streamlit
- Groq API
- Llama 3.3 70B

## Project Structure

ai-email-writer/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── modules/
│ ├── generator.py
│ ├── rewrite.py
│ ├── analyzer.py
│ └── followup.py
│
├── prompts/
│ ├── email_templates.py
│ └── tone_prompts.py
│
├── utils/
│ └── helpers.py
│
└── assets/

## Installation

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

## Future Improvements

- Gmail integration
- CRM integration
- Multilingual support
- Email analytics dashboard

## Author

Prerana S H
