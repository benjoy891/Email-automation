Email Automation Setup
This project automates the process of sending emails daily with a specified attachment. The process is divided into two main steps: configuring the email and uploading the necessary details via a web interface, and running a background task that sends the emails.

Prerequisites
Ensure the following are installed on your system before proceeding:

Python (version 3.6 or higher)
Virtual Environment Tool (venv)
Access to a terminal or command prompt.
Steps to Set Up and Run the Email Automation Process
1. Set Up Virtual Environment
To keep dependencies isolated, set up a Python virtual environment:

Open the terminal or Command Prompt.

Navigate to the project directory.

Activate the virtual environment:

For Windows:

bash
Copy code
auto\Scripts\activate
For macOS/Linux:

bash
Copy code
source auto/bin/activate
Once activated, you should see (auto) in your terminal or command prompt.

2. Run the Flask Web App to Upload Configuration Details
Start the Flask web app by running app.py:

bash
Copy code
python app.py
Open your browser and navigate to the following URL:

http://127.0.0.1:5000

This will open the web interface where you can upload the required configuration details.

You will be asked to provide:

Email Address: The email address from which the emails will be sent.
Email Password: Your email password or a passkey generated from Google Account settings.
Attachment File Path: The path to the file that will be attached to the email.
Email Time: The time when the emails will be sent daily (in 24-hour format, e.g., "09:00").
3. Upload the Configuration Details
Using the web interface:

Submit the configuration details.
The details will be stored in a config.json file in the project directory.
A secret key will be generated and saved as secret.key in the project folder.
4. Running the Daily Email Task
Once the configuration is stored, run the background task to send emails daily:

Ensure the virtual environment is activated.

Run the following command:

bash
Copy code
python daily_email.py
This will start the email automation process, sending emails at the specified time. Minimize the terminal to allow the task to run continuously.

Optional: Running in the Background
You can run the task silently in the background:

bash
Copy code
pythonw daily_email.py
This will run the script without keeping the terminal open.
To confirm the script is running, check for the Python process in the Task Manager (Windows) or Activity Monitor (macOS).
File Structure
The project includes the following key files:

app.py: The Flask web app that collects configuration details.
daily_email.py: The script that sends emails based on the configuration.
config.json: The configuration file where email and SMTP details are stored.
secret.key: A file containing a secret key used for session management.
email_task.log: The log file recording the status of the email task.
Final Notes
Ensure your system's time is synchronized with the specified time in config.json for accurate scheduling.
If the system restarts or the task stops (e.g., terminal closes), you will need to re-run python daily_email.py to resume the task.
Contact
For questions or issues, please contact the project maintainer.
