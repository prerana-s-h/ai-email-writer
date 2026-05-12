from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_email(purpose, tone, length):

    prompt = f"""
    Write a professional email.

    Purpose:
    {purpose}

    Tone:
    {tone}

    Length:
    {length}

    Requirements:
    - Generate 3 subject line options
    - Proper greeting
    - Clear and professional body
    - Strong closing statement
    - Proper signature
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