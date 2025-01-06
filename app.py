import os
import json
from cryptography.fernet import Fernet
from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)

# Secret key for session and flash messages
app.secret_key = Fernet.generate_key()  # This should be kept secure in production

UPLOAD_FOLDER = 'uploads'
CONFIG_FILE = 'config.json'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Default configuration
DEFAULT_CONFIG = {
    "email": "",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "file_path": "",
    "email_time": "",
    "encrypted_password": ""  # We'll store the encrypted password here
}

# Key for encryption (should be stored securely and not hardcoded in production)
SECRET_KEY = Fernet.generate_key()  # Generate a key for encryption

# Save the secret key to a file
with open('secret.key', 'wb') as key_file:
    key_file.write(SECRET_KEY)

print("Secret key file 'secret.key' generated successfully.")

# Initialize the config file if not present
if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(DEFAULT_CONFIG, f)

# Function to load config
def load_config():
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

# Function to save config
def save_config(new_config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(new_config, f)

# Function to encrypt the password
def encrypt_password(password):
    fernet = Fernet(SECRET_KEY)
    encrypted_password = fernet.encrypt(password.encode())  # Encrypt and convert to bytes
    return encrypted_password.decode()  # Return as string for storage

# Route to render the HTML form
@app.route('/')
def upload_form():
    return render_template('index.html')

# Route to handle form submission and update configuration
@app.route('/update_config', methods=['POST'])
def update_config():
    email_address = request.form['email']
    email_password = request.form['password']
    email_time = request.form['time']

    # Encrypt the password before saving it
    encrypted_password = encrypt_password(email_password)

    # Save uploaded file
    uploaded_file = request.files['file']

    new_filename = uploaded_file.filename

    # Construct the file path dynamically by appending the new filename to the upload folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)

    # Save the file to the constructed path
    uploaded_file.save(file_path)
    # Update configuration with encrypted password
    new_config = {
        "email": email_address,
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "file_path": file_path,
        "email_time": email_time,
        "encrypted_password": encrypted_password
    }
    save_config(new_config)


    return redirect(url_for('success'))  # Redirect back to the form

@app.route('/success')
def success():
    return render_template('success.html')  # Render a separate success page


if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
