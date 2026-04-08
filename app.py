import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # One year in seconds

# Load environment variables from .env file
load_dotenv()

# Load Configuration
sender_email = os.getenv('EMAIL_USERNAME')
app_password = os.getenv('EMAIL_PASSWORD')

@staticmethod
def send_email(receiver_email, subject, body):

    # Create the message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP(os.getenv('EMAIL_HOST'), int(os.getenv('EMAIL_PORT'))) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():   
    error = None  
    error_message = None  
    if request.method == 'POST':       
        if request.form['action'] == 'send':  
            name = request.form['name'] 
            phone = request.form['phone']
            email = request.form['email']
            message = request.form['message']
            
            subject = "New Contact Form Submission"
            body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"
            if send_email(sender_email, subject, body):
                body = "Your message has been received successfully! We will get back to you shortly."
                send_email(email, "Your Message Has Been Received", body)
                error_message = "Your message has been sent successfully!"  # Set success message
            else:
                error = "Failed to send email."  # Set error message

    return render_template('index.html', error=error, error_message=error_message)


if __name__ == '__main__':
    debug_mode = os.getenv('IS_DEBUG', False) in ['True', '1', 't']
    app_port = int(os.getenv('APP_PORT', 5000))
    if debug_mode:
        app.run(debug=debug_mode, port=app_port)
    else:
        app.run()
