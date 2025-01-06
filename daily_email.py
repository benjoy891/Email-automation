import schedule
import logging
import time
import mail_automation
import os
import json

project_dir = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(project_dir, 'config.json')

def load_config():
    if not os.path.exists(CONFIG_FILE):
        raise Exception("Configuration file 'config.json' is missing!")
    
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

# Setup logging to a file
logging.basicConfig(filename='email_task.log', level=logging.INFO)

logging.info("Your email task has started successfully, emails will be sent at the given time daily")
print("Your email task has started successfully, emails will be sent at the given time daily")

def job():
    try:
        logging.info("Running the job...")
        print("Running the job...")
        mail_automation.check_and_send_emails()
        logging.info("The job was executed successfully")
        print("The job was executed successfully")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Load the configuration
config = load_config()

# Ensure 'email_time' is present in the config
email_time = config.get("email_time")
if not email_time:
    logging.error("The 'email_time' key is missing in the configuration.")
    raise ValueError("Missing 'email_time' in the configuration file.")

# Schedule the job at the specified time
schedule.every().day.at(email_time).do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
