from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
from jinja2 import StrictUndefined
# from website import create_app


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'k23lkjfwa-9adkljfg' #secures cookies and sessions data

    return app 

@app.route('/')
def homepage():
    """View homepage"""
    return render_template(homepage.html)

# @app.route('/user', method=['POST'])
# def user():
#     return render_tempalte(user.html)


app = create_app()

if __name__ == '__main__': 
#only if we run this file we will excute app.run(debug=True). 
#Only run web server if we run this file. 
#Turn off when running in production
    app.run(debug=True)
