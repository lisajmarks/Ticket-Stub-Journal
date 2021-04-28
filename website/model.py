"""Models for movie  Ticket Stub Journal."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"
    #TODO: Add nullables#
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    name = db.Column(db.string)
    password = db.Column(db.String)
    join_date = db.Column(db.DateTime)
    bio = db.Column(db.Text)
    city = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Event(db.Model):
    """An Event."""

    __tablename__= "events"

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.venue_id'), nullable=False)
    pic_id = db.Column(db.Integer, db.ForeginKey('pictures.pic_id'))
    event_name = db.Column(db.String)
    date = db.Column(db.DateTime)

class Venue(db.Model):
    """A Venue"""
    #Add Whoosh? 
    __tablename__= "venues"

    venue_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    description = db.Column(db.String)
    
    def __repr__(self):
        return f'<location venue_id={self.loc_id} name={self.name}'

class Memory(db.Model): 
    """A Memory"""

    __tablename__ = "memories"

    memory_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    fav_song = db.Column(db.String)
    memory = db.Column(db.Text)
    squad = db.Column(db.String)

class UserEvent(db.Model):
    """A User's Event"""

    __tablename__= "user_event"

    user_event_id = db.Column(db.integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))

    user_event = db.relationship('User', backref='events')
    events_user = db.relationship('Event', backref='users')

class Picture(db.Model):
    """A Picture"""
    #install URL type furl? https://github.com/gruns/furl
    __tablename__ = "pictures"

    pic_id = db.Column(db.integer, autoincrement=True, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullablle=False)
    loc = db.Column(URLType)


