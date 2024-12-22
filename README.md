# devilx-bulk-email-sender
This Bulk Email Sender Tool is designed for sending bulk emails efficiently using SMTP. Whether you're conducting email marketing or sending notifications, this tool simplifies the process by automating bulk email delivery with customizable templates.
## Features
- **Bulk Email Sending**: Send emails to multiple recipients at once.
- **SMTP Integration**: Connect to any SMTP server (e.g., Gmail, Yahoo, etc.).
- **Custom Email Templates**: Use an HTML file for personalized email design.
- **Logs Sent and Failed Emails**: Keeps track of successful and failed email deliveries.
- **Secure Connection**: Uses TLS encryption for secure communication with the SMTP server.

## Prerequisites
- Python 3.6+
- Required Python libraries:
  - `smtplib`
  - `email`
  - `termcolor`

You can install `termcolor` using pip:
```bash
pip install termcolor
```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bulk-email-sender.git
   cd bulk-email-sender
   ```
2. Create a text file containing the email addresses of recipients (one email per line).
3. Prepare an HTML file to use as the email template.

## How to Use
1. Run the script:
   ```bash
   python bulk_email_sender.py
   ```
2. Follow the prompts to configure SMTP settings, input email addresses, and specify the email template.
3. The tool will attempt to send emails to all the addresses and log the results in `sent.txt`.

## Example
```
[+] 💻 Enter SMTP host (e.g., smtp.gmail.com): smtp.gmail.com
[+] 💡 Enter SMTP port (e.g., 587): 587
[+] 🔑 Enter your email address (username): your_email@gmail.com
[+] 🔒 Enter your email password: ********
[+] 📧 Enter your from email address: your_email@gmail.com
[+] 🧑‍💻 Enter your name (as it will appear on the emails): Your Name
[+] 📝 Enter Your Email Subject: Welcome to Our Service
[+] 🖼️ Enter your icon or logo (optional, leave empty for no icon):
[+] 📂 Enter the path to the text file containing email addresses: emails.txt
[+] 📝 Enter the path to the HTML template file: template.html
```

## Output
- **Sent Emails**: Logs of successfully sent emails are stored in `sent.txt`.
- **Failed Emails**: Errors are displayed in the terminal for failed email deliveries.

## Disclaimer
This tool is for educational and authorized use only. Sending bulk emails without recipient consent may violate anti-spam laws in your country.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Created by Karaj Singh. Connect on Telegram: [@ShadowCipher_org](https://t.me/ShadowCipher_org).
