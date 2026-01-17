import imaplib
import email
import time
from email.policy import default

# Use the unique ports mapped in the 2026 setup
mail = imaplib.IMAP4('localhost', 4143)
#smtp4devuser/smtp4devpassword
# mail.login('smtp4devuser', 'smtp4devpassword') 
#testuser/secret
mail.login('testuser', 'secret') 

def fetch_and_print_body(msg_id):
    """Fetches and prints the plain text body of an email."""
    typ, data = mail.fetch(msg_id, "(RFC822)")
    if typ == 'OK':
        # data[0][1] contains the raw bytes of the email
        msg = email.message_from_bytes(data[0][1], policy=default)
        print(f"\n--- Email ID: {msg_id.decode()} ---")
        print(f"Subject: {msg['subject']}")
        
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    print(f"Body: {part.get_payload(decode=True).decode()}")
                    break
        else:
            print(f"Body: {msg.get_payload(decode=True).decode()}")
        print("-" * 25)


def process_unseen_emails():
    """Processes unread emails and marks them with a custom 'processing' tag."""
    mail.select("INBOX")
    # 'UNSEEN' is a standard, globally supported search key
    typ, data = mail.search(None, 'UNSEEN')
    msg_ids = data[0].split()

    if msg_ids:
        print(f"🔍 Found {len(msg_ids)} new emails.")
        for msg_id in msg_ids:
            fetch_and_print_body(msg_id)
            # Mark as Seen (Read) and add custom 'processing' keyword
            # Custom keywords MUST be in parentheses
            mail.store(msg_id, '+FLAGS', '(\\Seen processing)')
            print(f"✅ Tagged {msg_id.decode()} as 'processing'")
    else:
        print("ℹ️ No new unseen messages found.")


def process_processing_emails():
    """Client-side filter to find messages with the 'processing' tag."""
    mail.select("INBOX")
    # Fetch all message IDs and their flags to filter locally
    typ, data = mail.search(None, 'ALL')
    msg_ids = data[0].split()

    found_any = False
    for msg_id in msg_ids:
        # Fetch only the flags for this message to check for our tag
        typ, flag_data = mail.fetch(msg_id, '(FLAGS)')
        flags_str = str(flag_data[0])
        
        if 'processing' in flags_str:
            found_any = True
            print(f"⚙️ Finalizing processing for ID: {msg_id.decode()}")
            # Move from 'processing' to 'processed' status
            mail.store(msg_id, '-FLAGS', '(processing)')
            mail.store(msg_id, '+FLAGS', '(processed)')
            print(f"✅ Message {msg_id.decode()} is now 'processed'.")
            
    if not found_any:
        print("ℹ️ No emails currently in 'processing' state.")


def processedemails_to_donefolder():
    """Moves emails with 'processed' tag to 'done' folder."""
    
    # if 'done' folder does not exist, create it
    # if 'done' not in [folder.decode().split(' "/" ')[1] for folder in mail.list()[1]]:
    mail.create('done')
    mail.select("INBOX")
    typ, data = mail.search(None, 'ALL')
    msg_ids = data[0].split()

    for msg_id in msg_ids:
        typ, flag_data = mail.fetch(msg_id, '(FLAGS)')
        flags_str = str(flag_data[0])
        
        if 'processed' in flags_str:
            print(f"📂 Moving message ID: {msg_id.decode()} to 'done' folder.")

            # Copy to 'done' folder
            mail.copy(msg_id, 'done')
            # Mark original for deletion
            mail.store(msg_id, '+FLAGS', '(\\Deleted)')
            print(f"✅ Message {msg_id.decode()} moved to 'done' folder.")

    # Expunge to permanently delete marked messages
    mail.expunge()
    print("🗑️ Expunged deleted messages from INBOX.")


if __name__ == "__main__":
    try:
        print("--- Phase 1: Processing UNSEEN ---")
        process_unseen_emails()
        
        time.sleep(1) 
        
        print("\n--- Phase 2: Finishing 'processing' tagged emails ---")
        process_processing_emails()

        print("\n--- Phase 3: Moving 'processed' emails to folder ---")
        processedemails_to_donefolder()
    finally:
        mail.logout()
        print("\nLogged out safely.")