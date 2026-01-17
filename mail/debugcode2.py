import imaplib

mail = imaplib.IMAP4('localhost', 3143)
mail.login('smtp4devuser', 'smtp4devpassword')
mail.select("INBOX")

# Search for UNSEEN (Unread) messages - This is the most reliable "unread" filter
typ, data = mail.search(None, 'UNSEEN')
msg_ids = data[0].split()

if msg_ids:
    latest_id = msg_ids[-1]
    
    # FIX: Custom flags must be in parentheses: (processed)
    # Also, we use \\Seen to ensure it looks "Read" in the Web UI
    try:
        # This marks it as "Read" (Seen) and adds your custom label
        mail.store(latest_id, '+FLAGS', '(\\Seen processed)')
        print(f"✅ Marked message {latest_id.decode()} as processed and seen.")
    except imaplib.IMAP4.error as e:
        print(f"❌ Server rejected custom flag. Trying standard \\Seen flag. Error: {e}")
        mail.store(latest_id, '+FLAGS', '(\\Seen)')
        
else:
    print("ℹ️ No new unseen messages to process.")

mail.logout()