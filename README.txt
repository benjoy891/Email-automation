
Here's a README file that a new user can follow to set up and run the process in another system.

Email Automation Setup - 

This project automates the process of sending emails daily with a specified attachment. The process is divided into two 
main steps: configuring the email and uploading the necessary details via a web interface, and running a background task 
that sends the emails.

Prerequisites -

Before proceeding with the setup, ensure that the following are installed on the system:

Python 3.6 or higher
Virtual environment tool (venv)
You also need access to a terminal or command prompt.

Steps to Set Up and Run the Email Automation Process - 

1. Set Up Virtual Environment
To keep the dependencies isolated, set up a Python virtual environment.

Open the terminal or Command Prompt.
Activate the virtual environment:
For Windows:

bash
Copy code
auto\Scripts\activate

For macOS/Linux:
Copy code
source auto/bin/activate

Once activated, you should see (auto) in your terminal or command prompt.

2. Run the Flask Web App to Upload Configuration Details
Start the Flask web app by running app.py:

Copy code
python app.py

Open your browser and go to the following URL:

http://127.0.0.1:5000


This will open the web interface where you can upload the required configuration details. You will be asked to provide the 
following:

Email Address: The email address from which the emails will be sent.
Email Password : Your email password or the Pass key that can be created for Google Account settings which should be 
manually done by the user itself.
Attachment File Path: The path to the file that will be attached to the email.
Email Time: The time when the emails will be sent daily (in 24-hour format, e.g., "09:00").

3. Upload the Configuration Details

Use the web interface to upload the configuration details. Once the details are submitted, they will be stored in a config.json file.
The Flask app will generate a secret key and save it as secret.key in the project folder.

4. Running the Daily Email Task
Once the Flask app has successfully stored the configuration, you can run the background task to send emails daily.

In the terminal, ensure that the virtual environment is activated.
Run the following command:

Copy code

python daily_email.py

This command will run the email automation process, and emails will be sent daily at the specified time. 
Minimize the terminal to ensure the task runs daily, if in any case the terminal is closed or the system is shutdown, execute the 
same code to the terminal of the project directory (Mail_Automation) after activating the virt environment (auto\Scripts\activate).

Optional way - 

Code:
pythonw daily_email.py

This command will run the email automation process, and emails will be sent daily at the specified time. The task will keep 
running until the script is stopped. 

After running the task with pythonw, you can verify that the script is running in the background by checking the list of 
processes in the Task Manager (Windows) or Activity Monitor (macOS).The Python process should be visible, indicating that the 
task is running.


File Structure
The project includes the following key files:

app.py: The Flask web app that collects configuration details.
daily_email.py: The script that sends the emails based on the configuration.
config.json: The configuration file where email and SMTP details are stored.
secret.key: A file containing a secret key used for session management.
email_task.log: The log file where the status of the email task is recorded.


Final Notes

* Ensure that your system's time is synchronized with the specified time in config.json for accurate scheduling.
* If the system is restarted or the task is stopped or the command terminal where you've run the scripts is closed, you will 
need to run python daily_email.py again to resume the email task.
