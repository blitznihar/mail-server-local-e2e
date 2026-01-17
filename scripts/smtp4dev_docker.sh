docker run -d \
  --name smtp4dev \
  -p 3000:80 \
  -p 3025:25 \
  -p 3110:110 \
  -p 3143:143 \
  -e ServerOptions__Users="smtp4devuser:smtp4devpassword:All" \
  rnwood/smtp4dev:v3
# This command runs a smtp4dev Docker container with the following configurations:
# --name smtp4dev: Names the container "smtp4dev".
# -p 3025:25: Maps port 25 of the container to port 3025 on the host for SMTP.
# -p 3000:80: Maps port 80 of the container to port 3000 on the host for the web UI.
# -p 3110:110: Maps port 110 of the container to port 3110 on the host for POP3.
# -p 3143:143: Maps port 143 of the container to port 3143 on the host for IMAP.
# Port mappings:
#Port 3025: SMTP (Sending)
# Port 3110: POP3 (Receiving)
# Port 3000: Web UI (View emails at http://localhost:3000)
# ServerOptions__Users: Sets the username (smtp4devuser) and password (smtp4devpassword) required for authentication. 
# Run this file using the command: bash docker.sh
# chmod +x filename.sh