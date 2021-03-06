"""CRUD operations."""

from jinja2.runtime import Undefined
from model import db, User, Event, Venue, Memory, Picture, connect_to_db


# Functions start here!

def clear_tables():
    db.create_all()
    Memory.query.delete()
    User.query.delete()
    Event.query.delete()
    Venue.query.delete()
    Picture.query.delete()
    db.session.commit()

def create_user(email, password, username, first_name, last_name, bio, city ):
    """Create and return a new user."""

    user = User(email=email, password=password, username=username, 
                first_name=first_name, last_name=last_name, bio=bio, city=city)

    db.session.add(user)
    db.session.commit()

    return user

# def create_venue(latitude, longitude, street_address, city, state):
#     """Create and return a venue"""
    
#     venue = Venue(latitude=latitude, longitude=longitude, street_address=street_address, city=city, state=state)
#     db.session.add(venue)
#     db.session.commit()

#     return venue

def create_venue(name, address='', latitude=0, longitude=0):
    """Create and return a venue"""
    
    venue = Venue(name=name, latitude=latitude, longitude=longitude, 
                address=address)
    db.session.add(venue)
    db.session.commit()

    return venue



def create_event(venue_id, event_name, headliner, date):
    """Create and return a new event"""
    event = Event(venue_id=venue_id, event_name=event_name, 
                headliner=headliner, date=date)

    db.session.add(event)
    db.session.commit()

    return event 



def create_memory(user_id, event_id, fav_song, memory, squad, pic_id=None):
    """Create and return a memory"""

    # user = User(user_id=user_id)
    # db.session.add(user)
    # db.session .commit()

    # event = Event(event_id=event_id)
    # db.session.add(event)
    # db.session.commit()

    memory = Memory(user_id=user_id, event_id=event_id, fav_song=fav_song, memory=memory, squad=squad, pic_id=pic_id)
    db.session.add(memory)
    db.session.commit()

    return memory 

def create_picture(pic_id, loc):
    pic = Picture(pic_id=pic_id, loc=loc)
    db.session.add(pic)
    db.session.commit()

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

def get_user_by_username(username):
    """Return a user by username""" 
    return User.query.filter(User.username == username).first()

# def create_user_event(user_id, event_id, pic_id=""):
#     user_event = UserEvent(user_id=user_id, event_id=event_id, pic_id=pic_id)
#     db.session.add(user_event)
#     db.session.commit()

#     return user_event

def get_memories_by_userid(user_id): 
    """Return a users event info by user id"""
    user = User.query.get(user_id)

    # user.memories[0].fav_song
    # user.memories[0].memory
    # user.memories[0].squad
    # user.memories[0].event.event_name
    # user.memories[0].pic.loc
    # user.memories[0].event.venue.name
    return user.memories

def add_picture(loc):
    """Add an image url to db"""
    pic = Picture(loc=loc)
    db.session.add(pic)
    db.session.commit()
    return pic



if __name__ == '__main__':
    from server import app
    connect_to_db(app)