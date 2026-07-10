import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("uvicorn.error")

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM = os.getenv("SMTP_FROM", SMTP_USER)
CONTACT_TO_EMAIL = os.getenv("CONTACT_TO_EMAIL")


def send_contact_email(name: str, email: str, phone: str | None, subject: str | None, message: str) -> bool:
    """Send the contact form submission to the business inbox. Returns True on success."""
    if not SMTP_USER or not SMTP_PASSWORD or not CONTACT_TO_EMAIL:
        logger.warning("SMTP not configured (.env missing) — skipping email send, message saved to DB only.")
        return False

    mail_subject = f"New Website Enquiry: {subject}" if subject else f"New Website Enquiry from {name}"

    body = (
        f"You received a new enquiry from the website contact form.\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone or '-'}\n"
        f"Subject: {subject or '-'}\n\n"
        f"Message:\n{message}\n"
    )

    msg = MIMEMultipart()
    msg["From"] = SMTP_FROM
    msg["To"] = CONTACT_TO_EMAIL
    msg["Reply-To"] = email
    msg["Subject"] = mail_subject
    msg.attach(MIMEText(body, "plain"))

    try:
        if SMTP_PORT == 465:
            with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=15) as server:
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SMTP_FROM, [CONTACT_TO_EMAIL], msg.as_string())
        else:
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=15) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SMTP_FROM, [CONTACT_TO_EMAIL], msg.as_string())
        return True
    except Exception:
        logger.exception("Failed to send contact form email")
        return False


def send_application_email(
    job_title: str,
    name: str,
    email: str,
    phone: str | None,
    message: str | None,
    resume_path: str | None,
) -> bool:
    """Send a job application notification with the resume attached. Returns True on success."""
    if not SMTP_USER or not SMTP_PASSWORD or not CONTACT_TO_EMAIL:
        logger.warning("SMTP not configured (.env missing) — skipping email send, application saved to DB only.")
        return False

    body = (
        f"You received a new job application via the website.\n\n"
        f"Position: {job_title}\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone or '-'}\n\n"
        f"Message:\n{message or '-'}\n"
    )

    msg = MIMEMultipart()
    msg["From"] = SMTP_FROM
    msg["To"] = CONTACT_TO_EMAIL
    msg["Reply-To"] = email
    msg["Subject"] = f"New Job Application: {job_title} — {name}"
    msg.attach(MIMEText(body, "plain"))

    if resume_path and os.path.isfile(resume_path):
        with open(resume_path, "rb") as f:
            attachment = MIMEApplication(f.read(), Name=os.path.basename(resume_path))
        attachment["Content-Disposition"] = f'attachment; filename="{os.path.basename(resume_path)}"'
        msg.attach(attachment)

    try:
        if SMTP_PORT == 465:
            with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=15) as server:
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SMTP_FROM, [CONTACT_TO_EMAIL], msg.as_string())
        else:
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=15) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SMTP_FROM, [CONTACT_TO_EMAIL], msg.as_string())
        return True
    except Exception:
        logger.exception("Failed to send job application email")
        return False
