"""Models for movie  Ticket Stub Journal."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"
    #TODO: Add nullables#
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    profile_pic = db.Column(db.Integer, db.ForeignKey('pictures.pic_id'))
    email = db.Column(db.Text, unique=True)
    name = db.Column(db.Text)
    password = db.Column(db.Text)
    join_date = db.Column(db.DateTime)
    bio = db.Column(db.Text)
    city = db.Column(db.Text)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Event(db.Model):
    """An Event."""

    __tablename__= "events"

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.venue_id'))
    # pic_id = db.Column(db.Integer, db.ForeginKey('pictures.pic_id'))
    event_name = db.Column(db.Text)
    date = db.Column(db.DateTime)

class Venue(db.Model):
    """A Venue"""
    #Add Whoosh? 
    __tablename__= "venues"

    venue_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    street_address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    #description = db.Column(db.Text)
    
    # def __repr__(self):
    #     return f'<location venue_id={self.loc_id} name={self.name}'

class Memory(db.Model): 
    """A Memory"""

    __tablename__ = "memories"

    memory_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    fav_song = db.Column(db.Text)
    memory = db.Column(db.Text)
    squad = db.Column(db.Text)

class UserEvent(db.Model):
    """A User's Event"""

    __tablename__= "user_event"

    user_event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    pic_id = db.Column(db.Integer, db.ForeignKey('pictures.pic_id'))

    user_event = db.relationship('User', backref='events')
    events_user = db.relationship('Event', backref='users')

class Picture(db.Model):
    """A Picture"""
    #TODO: install URL type furl? https://github.com/gruns/furl
    __tablename__ = "pictures"

    pic_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullablle=False)
    loc = db.Column(db.Text)



def connect_to_db(flask_app, db_uri='postgresql:///tsj', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)