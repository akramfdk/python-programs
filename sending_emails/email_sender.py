import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
sender_email = os.getenv("EMAIL_USER")
sender_password = os.getenv("EMAIL_PASS")
receiver_email = os.getenv("EMAIL_RECEIVER")

BASE_DIR = Path(__file__).resolve().parent
HTML_PATH = BASE_DIR.joinpath("index.html")
# print(HTML_PATH)

html = HTML_PATH.read_text()

t = Template(html)
html_content = t.substitute(name="Akram")
# print(t.substitute(name="Akram"))

email = EmailMessage()
email["from"] = "CODER"
email["to"] = receiver_email
email["subject"] = "Invitation for Hackathon"
# email.set_content(content) # this is for plain content
email.add_alternative(html_content, subtype="html")
# email.set_content(html_content, "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.send_message(email)

print("Email sent successfully!")