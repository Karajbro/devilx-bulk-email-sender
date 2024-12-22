import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from termcolor import colored
import os
def read_email_addresses(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]
def send_bulk_email():
    print(
        colored(
            '''               8888888b.  8888888888 888     888 8888888 888           Y88b   d88P 
               888  "Y88b 888        888     888   888   888            Y88b d88P  
               888    888 888        888     888   888   888             Y88o88P   
               888    888 8888888    Y88b   d88P   888   888              Y888P    
               888    888 888         Y88b d88P    888   888              d888b    
               888    888 888          Y88o88P     888   888             d88888b   
               888  .d88P 888           Y888P      888   888            d88P Y88b  
               8888888P"  8888888888     Y8P     8888888 88888888      d88P   Y88b 
               This Tool Created By Karaj Telegram 🚀 @ShadowCipher_org ''',
            "red"))
    host = input(
        colored("[+] 💻 Enter SMTP host (e.g., smtp.gmail.com): ", "cyan"))
    port = int(input(colored("[+] 💡 Enter SMTP port (e.g., 587): ", "cyan")))
    username = input(
        colored("[+] 🔑 Enter your email address (username): ", "cyan"))
    password = input(colored("[+] 🔒 Enter your email password: ", "cyan"))
    from_email = input(colored("[+] 📧 Enter your from email address: ",
                               "cyan"))
    from_name = input(
        colored("[+] 🧑‍💻 Enter your name (as it will appear on the emails): ",
                "cyan"))
    subject = input(colored("[+] 📝 Enter Your Email Subject: ", "cyan"))
    icon = input(
        colored(
            "[+] 🖼️ Enter your icon or logo (optional, leave empty for no icon): ",
            "cyan"))
    text_file = input(
        colored(
            "[+] 📂 Enter the path to the text file containing email addresses: ",
            "cyan"))
    template_file = input(
        colored("[+] 📝 Enter the path to the HTML template file: ", "cyan"))
    email_addresses = read_email_addresses(text_file)
    with open(template_file, 'r') as f:
        html_content = f.read()
    try:
        print(colored("[+] 🛠️ Connecting to SMTP server...", "yellow"))
        server = smtplib.SMTP(host, port)
        server.starttls()  # Start TLS encryption
        server.login(username, password)
        print(colored("[+] 🐲 SMTP connected successfully.", "green"))
    except Exception as e:
        print(
            colored(f"[+] ❌ ERROR: Unable to connect to SMTP server. {str(e)}",
                    "red"))
        return
    sent_emails = []
    failed_emails = []
    for email in email_addresses:
        try:
            msg = MIMEMultipart()
            msg['From'] = f"{from_name} <{from_email}>"
            msg['To'] = email
            msg['Subject'] = f"{subject}"
            msg.attach(MIMEText(html_content, 'html'))
            server.sendmail(from_email, email, msg.as_string())
            print(colored(f"[+] 🐲 SENT : {email}", "green"))
            sent_emails.append(email)
        except Exception as e:
            print(colored(f"[+] ❌ FAILED : {email} - {str(e)}", "red"))
            failed_emails.append(email)
    server.quit()
    with open('sent.txt', 'w') as f:
        for email in sent_emails:
            f.write(f"{email}\n")
    print(colored("\n[+] 📈 Bulk email sending process complete.", "blue"))
    print(colored(f"[+] 🟢 Sent emails: {len(sent_emails)}", "green"))
    print(colored(f"[+] 🔴 Failed emails: {len(failed_emails)}", "red"))
send_bulk_email()
