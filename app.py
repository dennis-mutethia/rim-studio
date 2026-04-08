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
    if request.method == 'POST':       
        if request.form['action'] == 'edit':  
            id = request.form['id']
            name = request.form['name'] 
                        
    return render_template('index.html')


if __name__ == '__main__':
    debug_mode = os.getenv('IS_DEBUG', False) in ['True', '1', 't']
    app_port = int(os.getenv('APP_PORT', 5000))
    if debug_mode:
        app.run(debug=debug_mode, port=app_port)
    else:
        app.run()
