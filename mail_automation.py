import os
import json
import logging
from cryptography.fernet import Fernet
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

logging.basicConfig(filename='email_task.log', level=logging.INFO)

project_dir = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY_FILE = os.path.join(project_dir, 'secret.key')
CONFIG_FILE = os.path.join(project_dir, 'config.json')

if not os.path.exists(SECRET_KEY_FILE):
    raise Exception("Secret key file is missing! Please make sure 'secret.key' is available.")
else:
    with open(SECRET_KEY_FILE, 'rb') as key_file:
        SECRET_KEY = key_file.read()

# Function to load configuration
def load_config():
    if not os.path.exists(CONFIG_FILE):
        raise Exception("Configuration file 'config.json' is missing!")
    
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

# Function to decrypt the password
def decrypt_password(encrypted_password):
    fernet = Fernet(SECRET_KEY)
    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
    return decrypted_password

# Function to send email
def send_email(email_address, smtp_server, smtp_port, recipient, subject, message):
    try:
        config = load_config()
        encrypted_password = config["encrypted_password"]
        email_password = decrypt_password(encrypted_password)  # Decrypt the password

        email = MIMEMultipart()
        email['From'] = email_address
        email['To'] = recipient
        email['Subject'] = subject
        email.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.send_message(email)

        print(f"Email sent successfully to {recipient}")
        logging.info(f"Email sent successfully to {recipient}")

    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

# Function to check and send emails
def check_and_send_emails():
    try:
        config = load_config()
        email_address = config["email"]
        smtp_server = config["smtp_server"]
        smtp_port = config["smtp_port"]
        project_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is running
        file_path = os.path.join(project_dir, config["file_path"])
        if not email_address or not file_path:
            print("Incomplete configuration. Skipping email sending.")
            return

        # Read the Excel file to get client and email info
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            client_name = row['Clients']
            recipient = row['Gmail']
            days_left = row['Number of days left']

            # Determine the subject and message based on the number of days left
            if days_left == 30:
                subject = f"Reminder: {client_name}, your payment is due in 30 days"
                message = f"Hello {client_name},\n\nThis is a reminder that your payment is due in 30 days. Please take the necessary actions.\n\nBest regards."
            elif days_left == 15:
                subject = f"Reminder: {client_name}, your payment is due in 15 days"
                message = f"Hello {client_name},\n\nThis is a reminder that your payment is due in 15 days. Please take the necessary actions.\n\nBest regards."
            elif days_left == 1:
                subject = f"Urgent: {client_name}, your payment is due tomorrow!"
                message = f"Hello {client_name},\n\nThis is a final reminder that your payment is due tomorrow. Please take the necessary actions immediately.\n\nBest regards."
            else:
                continue  # Skip clients who don't have any reminders to send

            send_email(email_address, smtp_server, smtp_port, recipient, subject, message)

    except Exception as e:
        print(f"Error processing configuration or sending emails: {e}")

# Run the email sending process
if __name__ == '__main__':
    check_and_send_emails()
