docker run -d \
  --name mailpit \
  -p 1025:1025 \
  -p 8025:8025 \
  -p 1110:1110 \
  -e MP_POP3_AUTH="testuser:secret" \
  axllent/mailpit
# This command runs a Mailpit Docker container with the following configurations:
# --name mailpit: Names the container "mailpit".
# -p 1025:1025: Maps port 1025 of the container to port 1025 on the host for SMTP.
# -p 8025:8025: Maps port 8025 of the container to port 8025 on the host for the web UI.
# -p 1110:1110: Maps port 1110 of the container to port 1110 on the host for POP3.
# -e MP_POP3_AUTH="testuser:secret": Sets the environment variable to enable POP3 authentication with the specified username and password.
# Port mappings:
#Port 1025: SMTP (Sending)
# Port 1110: POP3 (Receiving)
# Port 8025: Web UI (View emails at http://localhost:8025)
# MP_POP3_AUTH: Sets the username (testuser) and password (secret) required for POP3 retrieval. 
# Run this file using the command: bash docker.sh
# chmod +x filename.sh