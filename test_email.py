import resend
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.environ.get("RESEND_API_KEY")

params = {
    "from": "onboarding@resend.dev",
    "to": ["dusshes@mail.ru"],
    "subject": "Test Email",
    "html": "<p>This is a test email.</p>",
}

try:
    response = resend.Emails.send(params)
    print(f"Response: {response}")
except Exception as e:
    print(f"Error: {e}")
