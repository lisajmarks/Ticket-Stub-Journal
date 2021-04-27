from flask import Flask 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'k23lkjfwa-9adkljfg' #secures cookies and sessions data

    return app 
