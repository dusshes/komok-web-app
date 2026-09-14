import resend
import os
from flask import current_app

# Set your Resend API Key in .env
resend.api_key = os.environ.get("RESEND_API_KEY")

def send_verification_email(email, code):
    if not resend.api_key:
        print(f"Resend API Key not set. Verification code for {email}: {code}")
        return
        
    params = {
        "from": "onboarding@resend.dev", # Using Resend's test sender
        "to": [email],
        "subject": "Код подтверждения регистрации в Komok",
        "html": f"<p>Ваш код подтверждения: <strong>{code}</strong>. Срок действия кода: 15 минут.</p>",
    }
    try:
        print(f"Attempting to send email to {email} from {params['from']}...")
        response = resend.Emails.send(params)
        print(f"Resend API Response: {response}")
    except Exception as e:
        print(f"Error sending email: {e}")
        # Re-raise to see if it causes issues in the flow
        raise e
