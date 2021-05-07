from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
# from website import create_app


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'k23lkjfwa-9adkljfg' #secures cookies and sessions data

    return app 
app = create_app()


@app.route('/')
def homepage():
    """View homepage"""
    return render_template('homepage.html')

@app.route('/profile')
def profile():
    """View user profile"""
    return render_template('profile.html')

@app.route('/map')
def map():
    """View user event map"""
    return render_template('map.html')

@app.route('/events')
def events():
    """View user events"""
    return render_template('events.html')

@app.route('/shows')
def shows():
    """View user shows"""
    return render_template('shows.html')

@app.route('/addshow')
def add_show():
    """Add show info"""
    return render_template('addshow.html')

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user""" 

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user: 
        flash("Oops - Cannot create an account with that email. Try again.")
    else: 
        crud.create_user(email, password)
        flash("Account created! Log in and join the party!")

    return redirect('/')

@app.route("/users/<user_id>")
def show_user(user_id): 
    """Show details on a particular view."""

    user = crud.get_user_by_id(user_id)
    return render_template ("user_details.html", user=user) 

@app.route("/login", methods=["POST"])
def process_login(): 
    """Process User login.""" 
    email = request.form.get("login_email")
    password = request.form.get("login_password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password: 
        flash("Whoa - your email or password is incorrect!")
        print("{user.email}")
        print("{user.password}")
        print(email)
        print(password)
    else: 
        #log in user by storing the user's email in session 
        session["user_email"] = user.email 
        flash(f"Welcome back, {user.email}!")
    
    return redirect("/")

if __name__ == '__main__': 
#only if we run this file we will excute app.run(debug=True). 
#Only run web server if we run this file. 
#Turn off when running in production
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
