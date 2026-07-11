import base64
import json
import logging
import os
import urllib.error
import urllib.request

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("uvicorn.error")

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
SMTP_FROM = os.getenv("SMTP_FROM", "info@agrigem.in")
CONTACT_TO_EMAIL = os.getenv("CONTACT_TO_EMAIL")


def _brevo_send(subject: str, body: str, to_email: str, reply_to: str, attachments: list | None = None) -> bool:
    if not BREVO_API_KEY:
        logger.warning("BREVO_API_KEY not set — skipping email send")
        return False

    payload: dict = {
        "sender": {"name": "AgriGem", "email": SMTP_FROM},
        "to": [{"email": to_email}],
        "replyTo": {"email": reply_to},
        "subject": subject,
        "textContent": body,
    }

    if attachments:
        payload["attachment"] = attachments

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.brevo.com/v3/smtp/email",
        data=data,
        headers={
            "api-key": BREVO_API_KEY,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 201
    except urllib.error.HTTPError as e:
        logger.error("Brevo API HTTP error %s: %s", e.code, e.read().decode())
        return False
    except Exception:
        logger.exception("Failed to send email via Brevo API")
        return False


def send_contact_email(name: str, email: str, phone: str | None, subject: str | None, message: str) -> bool:
    if not CONTACT_TO_EMAIL:
        logger.warning("CONTACT_TO_EMAIL not set — skipping email send")
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
    return _brevo_send(mail_subject, body, CONTACT_TO_EMAIL, email)


def send_application_email(
    job_title: str,
    name: str,
    email: str,
    phone: str | None,
    message: str | None,
    resume_path: str | None,
) -> bool:
    if not CONTACT_TO_EMAIL:
        logger.warning("CONTACT_TO_EMAIL not set — skipping email send")
        return False

    body = (
        f"You received a new job application via the website.\n\n"
        f"Position: {job_title}\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone or '-'}\n\n"
        f"Message:\n{message or '-'}\n"
    )

    attachments = None
    if resume_path and os.path.isfile(resume_path):
        with open(resume_path, "rb") as f:
            content = base64.b64encode(f.read()).decode()
        attachments = [{"name": os.path.basename(resume_path), "content": content}]

    return _brevo_send(
        f"New Job Application: {job_title} — {name}",
        body,
        CONTACT_TO_EMAIL,
        email,
        attachments,
    )
