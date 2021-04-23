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

    show_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)