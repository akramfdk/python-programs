import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# load the environment variables
load_dotenv()
sender_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")
receiver_email = os.getenv("EMAIL_RECEIVER")


email = EmailMessage()
email["from"] = "CODER"
email["to"] = receiver_email
email["subject"] = "Hurray, You won $1,000,000!"

email.set_content("I am a Python Programmer")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() # Greet the server and announce client capabilities
    smtp.starttls() # Upgrade the connection to a secure encrypted connection
    smtp.login(sender_email, password)
    smtp.send_message(email)
    print("Email sent successfully!!")