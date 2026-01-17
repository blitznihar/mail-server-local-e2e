import imaplib

# Connect to smtp4dev
mail = imaplib.IMAP4('localhost', 3143)
mail.login('smtp4devuser', 'smtp4devpassword')

# 1. Try creating the folder again and print the result
typ, data = mail.create("processing")
print(f"Creation Attempt: {typ}, {data}")

# 2. List ALL folders available on the server
print("\n--- Available Folders ---")
typ, folders = mail.list()
for folder in folders:
    print(folder.decode())
print("-------------------------")

mail.logout()
