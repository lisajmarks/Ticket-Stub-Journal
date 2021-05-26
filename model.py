"""Models for movie  Ticket Stub Journal."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.orm import backref


db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"
    #TODO: Add nullables#
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.Text, unique=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    profile_pic = db.Column(db.Integer, db.ForeignKey('pictures.pic_id'))
    email = db.Column(db.Text, unique=True)
    name = db.Column(db.Text)
    password = db.Column(db.Text)
    join_date = db.Column(db.Date)
    bio = db.Column(db.Text)
    city = db.Column(db.Text)

    memories = db.relationship('Memory', backref='user') #create user attribute

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} >'

class Event(db.Model):
    """An Event."""

    __tablename__= "events"

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.venue_id'))
    # pic_id = db.Column(db.Integer, db.ForeignKey('pictures.pic_id'))
    event_name = db.Column(db.Text)
    headliner = db.Column(db.Text)
    date = db.Column(db.Date)

    venue = db.relationship('Venue', backref='event')
    # pic = db.relationship('Picture', backref='event')

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
    name = db.Column(db.Text)
    
    # def __repr__(self):
    #     return f'<location venue_id={self.loc_id} name={self.name}'

class Memory(db.Model): 
    """A Memory"""

    __tablename__ = "memories"

    memory_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    pic_id = db.Column(db.Integer, db.ForeignKey('pictures.pic_id'))

    fav_song = db.Column(db.Text)
    memory = db.Column(db.Text)
    squad = db.Column(db.Text)

    event = db.relationship('Event', backref='memory')
    pic = db.relationship('Picture')

    def set_picture(self, pic):
        self.pic = pic
        db.session.add(self)
        db.session.commit()
# class UserEvent(db.Model):
#     """A User's Event"""

#     __tablename__= "user_event"

#     user_event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
#     pic_id = db.Column(db.Integer, db.ForeignKey('pictures.pic_id'))

#     user_event = db.relationship('User', backref='events')
#     events_user = db.relationship('Event', backref='users')

class Picture(db.Model):
    """A Picture"""
    #TODO: install URL type furl? https://github.com/gruns/furl
    __tablename__ = "pictures"

    pic_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullablle=False)
    loc = db.Column(db.Text)

    memory_pic = db.relationship('Memory', backref='picture')



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