from cloudinary.utils import now
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db
from secrets import CLOUDINARY_KEY, CLOUDINARY_SECRET, FLASK_SECRET, G_MAPS_API_KEY
import crud
from jinja2 import StrictUndefined
from geocoding import get_coordinates
import cloudinary.uploader
import googlemaps
from datetime import datetime 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = FLASK_SECRET #secures cookies and sessions data

    return app 
app = create_app()


@app.route('/')
def homepage():
    """View homepage"""
    return render_template('homepage.html')

@app.route("/home")
def auth():
    """Return Authorized Page"""
    return render_template("/homepage-auth.html")

@app.route('/profile')
def profile():
    """View user profile"""
    return render_template('profile.html')

@app.route('/map')
def map():
    """View user event map"""
    return render_template('map.html')

# @app.route('/form')
# def form():
#     """View form page"""
#     return render_template('form.html')

# @app.route('/post-form-data', methods=["POST"])
# def user_form():
#     """Process form page"""

#     my_file = request.files['my-file']
#     result = cloudinary.uploader.upload(my_file, 
#     api_key=CLOUDINARY_KEY, api_secret=CLOUDINARY_SECRET, cloud_name="ticketstubjournal")

#     crud.add_picture(result['secure_url'])

#     return redirect('/form')

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
    


    # print(memories)
    # print(events)
    # events = crud.get_memories_by_userid(user_id)
    return render_template('events.html', user=user, 
    memories=memories, events=events)

# @app.route('/shows')
# def shows():
#     """View user shows"""
#     return render_template('shows.html')


@app.route('/register', methods=['POST'])
def register_user():
    """Create a new user""" 

    email = request.form.get('email')
    username = request.form.get('username')
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    password = request.form.get('password')
    bio = request.form.get('bio')
    city = request.form.get('city')

    user = crud.get_user_by_email(email)
    uname = crud.get_user_by_username(username)

    if user: 
        flash("There's already another user with that email! Try again.")
        return redirect('/register')
    elif uname: 
        flash("Someone has claimed that username! Try another.")
        return redirect('/register')
    else: 
        crud.create_user(email, password, username, first_name, last_name, bio, city,)
        flash("Account created! Log in and join the party!")

    return redirect('/home')


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
        return redirect("/")
    else: 
        #log in user by storing the user's email in session 
        session["user_email"] = user.email 
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.email}!")
    return redirect("/home")
    

@app.route("/events/create", methods=["POST"])
def create_event_backend():
    """Create User Event"""
    event_name = request.form.get("event_name")
    date = request.form.get("date")
    headliner = request.form.get("headliner")
    venue_name = request.form.get("venue")
    fav_song = request.form.get("fav_song")
    memories = request.form.get("memory")
    squad = request.form.get("squad")
    user_id = session["user_id"]
    address = request.form.get("address")

    #TODO: Fix so empty date is accepted
    if (date == False):
        date = date.today()

    gmaps = googlemaps.Client(key=G_MAPS_API_KEY)
    # Geocoding an address
    geocode_result = gmaps.geocode(address)

    lat = geocode_result[0]["geometry"]["location"].get("lat")
    lng = geocode_result[0]["geometry"]["location"].get("lng")

    v = crud.create_venue(venue_name, address, lat, lng)
    e = crud.create_event(v.venue_id, event_name, headliner, date)
    m = crud.create_memory(user_id, e.event_id, fav_song, memories, squad)
    # user_event = crud.create_user_event(user_id, e.event_id)

    my_file = request.files['my-file']
    if my_file:
        result = cloudinary.uploader.upload(my_file, 
        api_key=CLOUDINARY_KEY, api_secret=CLOUDINARY_SECRET, cloud_name="ticketstubjournal")

        pic = crud.add_picture(result['secure_url'])
        m.set_picture(pic)

    return redirect("/events")

@app.route('/mapevents')
def event_markers():
    """get markers for user events"""
    user_id = session.get("user_id")
    if not user_id: 
        flash("Please log in")
        return redirect('/') 
    markers = []
    memories = crud.get_memories_by_userid(user_id)
    for memory in memories:
        if memory.event.venue.latitude and memory.event.venue.latitude:
            markers.append({
                'name':memory.event.venue.name,
                'lng': memory.event.venue.longitude,
                'lat': memory.event.venue.latitude,
            })

    # marker = [{'lat':'47.62063283279521', 'lng': '-122.34925057978872', 'name': 'Space Needle'}]
    return jsonify(markers)

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
