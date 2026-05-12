from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_followups(context):

    prompt = f"""
    Generate 3 professional follow-up emails.

    Context:
    {context}

    Requirements:
    - Each email shorter than previous
    - Different angle in each email
    - Professional tone
    - Clear CTA
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