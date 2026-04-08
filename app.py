import os
from dotenv import load_dotenv
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # One year in seconds

# Load environment variables from .env file
load_dotenv()

# Routes
@app.route('/')
def index():   
    error = None  
    error_message = None  
    if request.method == 'POST':       
        if request.form['action'] == 'send':  
            name = request.form['name'] 
            phone = request.form['phone']
            email = request.form['email']
            message = request.form['message']
            
            #send email logic here using the collected data
            error_message = "Your message has been sent successfully!"  # Set success message
                        
    return render_template('index.html', error=error, error_message=error_message)


if __name__ == '__main__':
    debug_mode = os.getenv('IS_DEBUG', False) in ['True', '1', 't']
    app_port = int(os.getenv('APP_PORT', 5000))
    if debug_mode:
        app.run(debug=debug_mode, port=app_port)
    else:
        app.run()
