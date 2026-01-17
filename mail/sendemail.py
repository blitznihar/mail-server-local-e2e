import smtplib
from email.message import EmailMessage


def send_test_email(body, subject, from_addr, to_addr,
                    smtp_host="localhost", smtp_port=1025):
    print(f"1. Sending email via SMTP ({smtp_host}:{smtp_port})...")
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = from_addr
        msg["To"] = to_addr
        with smtplib.SMTP(smtp_host, smtp_port) as smtp:
            smtp.send_message(msg)
        print("   -> Email sent successfully.")

    except Exception as e:
        print(f"   -> Failed to send email: {e}")
        return f"Failed: {e}"

    return "Success"
