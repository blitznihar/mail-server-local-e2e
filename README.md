# Mail Server Local E2E

## Overview

`mail-server-local-e2e` is a local end-to-end testing setup for email servers using Python. This project allows you to send, retrieve, and process emails using various local SMTP, POP3, and IMAP servers. It is designed for testing email functionalities in a controlled environment.

## Features

- Send test emails using SMTP.
- Retrieve emails via POP3 and IMAP.
- Process unseen emails and manage their states.
- Supports multiple email server configurations (Mailpit, smtp4dev, GreenMail).

## Prerequisites

- Python 3.14 or higher
- Docker (for running email server containers)
- `python-dotenv` package for environment variable management

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/blitznihar/mail-server-local-e2e.git
   cd mail-server-local-e2e


First Setup the local SMTP using docker

- FOR SMTP4DEV
`docker compose -f compose.smtp4dev.yml up -d`

- FOR MAILPIT
`docker compose -f compose.mailpit.yml up -d`

- FOR GREENMAIL with ROUNDCUBE
`docker compose -f compose.greenmail-roundcube.yml up -d`


`uv venv`

`uv sync`

`python main.py`

`python mail/retrieveemailimap.py`