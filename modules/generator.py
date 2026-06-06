from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_email(
    sender_name,
    receiver_name,
    purpose,
    tone,
    length,
    word_limit
):

    # Greeting based on tone
    if receiver_name.strip():

        if tone == "Formal":
            greeting = f"Respected {receiver_name},"

        elif tone == "Professional":
            greeting = f"Greetings {receiver_name},"

        elif tone == "Polite":
            greeting = f"Dear {receiver_name},"

        elif tone == "Friendly":
            greeting = f"Hello {receiver_name},"

        elif tone == "Persuasive":
            greeting = f"Dear {receiver_name},"

        else:
            greeting = f"Dear {receiver_name},"

    else:

        if tone == "Formal":
            greeting = "Respected Sir/Madam,"

        elif tone == "Professional":
            greeting = "Greetings,"

        elif tone == "Polite":
            greeting = "Dear Sir/Madam,"

        elif tone == "Friendly":
            greeting = "Hello,"

        elif tone == "Persuasive":
            greeting = "Dear Sir/Madam,"

        else:
            greeting = "Dear Sir/Madam,"

    prompt = f"""
Write a professional email.

Sender Name:
{sender_name}

Recipient Name:
{receiver_name}

Purpose:
{purpose}

Tone:
{tone}

Length:
{length}

Maximum Words:
{word_limit}

Greeting:
{greeting}

IMPORTANT:
- Use the EXACT greeting provided above.
- Do NOT replace the greeting.
- Do NOT use any other greeting.
- Start the email with the greeting exactly as written.

Requirements:
- Generate ONLY the final email.
- Include exactly one subject line.
- Include greeting.
- Include email body.
- Include professional closing.
- Use sender name in signature.
- Keep the email within {word_limit} words.
- Do not provide explanations.
- Do not provide notes.
- Do not provide multiple subject options.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
