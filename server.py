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
    user_id = session.get("user_id")
    if not user_id: 
        flash("Please log in")
        return redirect('/') 
    user = crud.get_user_by_id(user_id)
    
    memories = {}
    #keys event ids, values list of memories 
    events = {} 
    #event ids, events 

    for memory in user.memories: 
        event = memory.event
        events[event.event_id] = event

        if event.event_id in memories:
            memories[memory.event_id].append(memory)
        else: 
            memories[memory.event_id] = [memory]
    
    print(memories)
    print(events)
    # events = crud.get_memories_by_userid(user_id)
    return render_template('events.html', user=user, memories=memories, events=events)

# @app.route('/shows')
# def shows():
#     """View user shows"""
#     return render_template('shows.html')


@app.route('/register', methods=['POST'])
def register_user():
#TODO: finish updating create_user function
    """Create a new user""" 

    email = request.form.get('email')
    username = request.form.get('username')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    password = request.form.get('password')
    bio = request.form.get('bio')
    city = request.form.get('city')

    user = crud.get_user_by_email(email)
    if user: 
        flash("There's already another user with that email! Try again.")
    else: 
        crud.create_user(email, password)
        flash("Account created! Log in and join the party!")

    return redirect('/')


@app.route("/register")
def register():
    """Display Registration Page""" 

    return render_template("/register.html")

@app.route("/user/<user_id>")
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
        flash("Hey you're not on the guestlist. Register to join the party!")
    else: 
        #log in user by storing the user's email in session 
        session["user_email"] = user.email 
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.email}!")
    
    return redirect("/home")

@app.route("/home")
def auth():
    """Return Homepage When User Is Authorized"""
    return render_template("/homepage-auth.html")

@app.route("/events/create", methods=["POST"])
def create_event_backend():
    """Create User Event"""
    event_name = request.form.get("event_name")
    date = request.form.get("date")
    venue_name = request.form.get("venue")
    fav_song = request.form.get("fav_song")
    memories = request.form.get("memory")
    squad = request.form.get("squad")
    user_id = session["user_id"]

    v = crud.create_venue(venue_name)
    e = crud.create_event(v.venue_id, event_name, date)
    m = crud.create_memory(user_id, e.event_id, fav_song, memories, squad)
    # user_event = crud.create_user_event(user_id, e.event_id)

    return redirect("/events")

@app.route("/events/create")
def create_event_page():
    """Display Create User Event Page""" 

    return render_template("/create-event.html")

if __name__ == '__main__': 
#only if we run this file we will excute app.run(debug=True). 
#Only run web server if we run this file. 
#Turn off when running in production
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
