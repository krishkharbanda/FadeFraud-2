import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("EMAIL_USER")
SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("EMAIL_RECEIVER")


def send_email():
    subject = "Fraud Alert: Suspicious Transaction Detected on your Card"

    body = f"""
    Attention FadeFraud user,
    
    Alert! A potentially fraudulent transaction has been detected on your card. Please check FadeFraud for further actions! Immediate action may be required.
    
    Regards,
    The FadeFraud Team
    
    Please do not reply to this email. Check the website for more information.
    """

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("Sent")
    except Exception as e:
        print(f"Error sending email: {e}")