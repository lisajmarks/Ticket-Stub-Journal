"""CRUD operations."""

from model import db, User, Event, Venue, Memory, UserEvent, Picture, connect_to_db


# Functions start here!

def clear_tables():
    db.create_all()
    Memory.query.delete()
    User.query.delete()
    Event.query.delete()
    Venue.query.delete()
    UserEvent.query.delete()
    Picture.query.delete()
    db.session.commit()

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_venue(venue_id, latitude, longitude, street_address, city, state):
    """Create and return a venue"""
    
    venue = Venue(venue_id=venue_id, latitude=latitude, longitude=longitude, street_address=street_address, city=city, state=state)
    db.session.add(venue)
    db.session.commit()

    return venue


def create_event(event_id, venue_id, event_name, date):
    """Create and return a new event"""
    venue = Venue(venue_id=venue_id)
    db.session.add(venue)
    db.session.commit()

    event = Event(event_id=event_id, venue_id=venue_id, event_name=event_name, date=date)

    db.session.add(event)
    db.session.commit()

    return event 



def create_memory(memory_id, user_id, event_id, fav_song, memory, squad):
    """Create and return a memory"""

    user = User(user_id=user_id)
    db.session.add(user)
    db.session.commit()

    event = Event(event_id=event_id)
    db.session.add(event)
    db.session.commit()

    memory = Memory(memory_id=memory_id, user_id=user_id, event_id=event_id, fav_song=fav_song, memory=memory, squad=squad)
    db.session.add(memory)
    db.session.commit()

    return memory 



if __name__ == '__main__':
    from server import app
    connect_to_db(app)