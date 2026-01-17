import time
import os
from dotenv import load_dotenv

# from mail.retrieveemail import retrieve_email_via_pop3
from mail.sendemail import send_test_email

load_dotenv()

# Configuration matching Docker command for mailpit
# SMTP_HOST = os.getenv("MAILPIT_SMTP_HOST", "localhost")
# SMTP_PORT = int(os.getenv("MAILPIT_SMTP_PORT", 1025))
# POP3_HOST = os.getenv("MAILPIT_POP3_HOST", "localhost")
# POP3_PORT = int(os.getenv("MAILPIT_POP3_PORT", 1110))
# POP3_USER = os.getenv("MAILPIT_POP3_USER", "testuser")
# POP3_PASS = os.getenv("MAILPIT_POP3_PASS", "secret")


# # Configuration matching Docker command for smtp4dev
# SMTP_HOST = os.getenv("SMTP4DEV_SMTP_HOST", "localhost")
# SMTP_PORT = int(os.getenv("SMTP4DEV_SMTP_PORT", 3025))
# POP3_HOST = os.getenv("SMTP4DEV_POP3_HOST", "localhost")
# POP3_PORT = int(os.getenv("SMTP4DEV_POP3_PORT", 3110))
# POP3_USER = os.getenv("SMTP4DEV_POP3_USER", "smtp4devuser")
# POP3_PASS = os.getenv("SMTP4DEV_POP3_PASS", "smtp4devpassword")
# IMAP_HOST = os.getenv("SMTP4DEV_IMAP_HOST", "localhost")
# IMAP_PORT = int(os.getenv("SMTP4DEV_IMAP_PORT", 3143))

# Configuration matching Docker command for greenmail
SMTP_HOST = os.getenv("GREENMAIL_SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("GREENMAIL_SMTP_PORT", 4025))
POP3_HOST = os.getenv("GREENMAIL_POP3_HOST", "localhost")
POP3_PORT = int(os.getenv("GREENMAIL_POP3_PORT", 4110))
POP3_USER = os.getenv("GREENMAIL_USER", "testuser")
POP3_PASS = os.getenv("GREENMAIL_PASS", "secret")
IMAP_HOST = os.getenv("GREENMAIL_IMAP_HOST", "localhost")
IMAP_PORT = int(os.getenv("GREENMAIL_IMAP_PORT", 4143))


def send_multiple_test_email():
    random_id = int(time.time())
    print(f"\n=== E2E Test Run ID: {random_id} ===")
    send_test_email(
        body=(
            f"This is a test email sent via local SMTP server. "
            f"Run ID: {random_id}"
        ),
        subject=f"Test Email from E2E Run ID: {random_id}",
        from_addr="sender@localhost",
        to_addr="testuser@localhost",
        smtp_host=SMTP_HOST,
        smtp_port=SMTP_PORT
        )


if __name__ == "__main__":
    # 1. Send the email
    for _ in range(25):  # Send multiple emails if desired
        send_multiple_test_email()

    # 2. Wait briefly for processing
    time.sleep(1)

    # # 3. Fetch it back
    # retrieve_email_via_pop3(pop3_host=POP3_HOST, pop3_port=POP3_PORT,
    #                         pop3_user=POP3_USER, pop3_pass=POP3_PASS)
