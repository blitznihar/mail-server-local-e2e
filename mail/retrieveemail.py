import poplib
from email import parser
import os
from dotenv import load_dotenv


load_dotenv()


def retrieve_email_via_pop3(pop3_host=os.getenv("POP3_HOST", "localhost"),
                            pop3_port=int(os.getenv("POP3_PORT", 1110)),
                            pop3_user=os.getenv("POP3_USER", "testuser"),
                            pop3_pass=os.getenv("POP3_PASS", "secret")):
    print(f"\n2. Retrieving email via POP3 ({pop3_host}:{pop3_port})...")
    # Connect to POP3 server
    server = poplib.POP3(pop3_host, pop3_port)

    # Authenticate
    server.user(pop3_user)
    server.pass_(pop3_pass)

    # Get message count
    num_messages = len(server.list()[1])
    print(f"   -> Inbox contains {num_messages} message(s).")

    if num_messages > 0:
        # Retrieve the latest message (index starts at 1)
        resp, lines, octets = server.retr(num_messages)

        # Decode and parse the raw email bytes
        raw_email = b"\r\n".join(lines).decode("utf-8")
        parsed_email = parser.Parser().parsestr(raw_email)

        print(f"   -> Retrieved Subject: '{parsed_email['subject']}'")
        print(f"   -> Retrieved Body: '{parsed_email.get_payload().strip()}'")

        # Optional: Delete message after retrieval
        # server.dele(num_messages)
    else:
        print("   -> No emails found.")

    server.quit()
