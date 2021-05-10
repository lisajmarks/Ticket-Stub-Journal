"""Script to seed database."""

import os
from random import choice, randint
from datetime import datetime

import crud
from model import db, connect_to_db, Picture, Venue, Event, User, Memory
from server import app


def generate_user_test_data():
    test_pic= Picture(pic_id='10', loc='test')
    db.session.add(test_pic)
    db.session.commit()

    for i in range(10):
        test_pic= Picture(pic_id=i, loc=f'test{i}')
        db.session.add(test_pic)
        db.session.commit()
        test_user= User(profile_pic=i, email=f'test{i}@test.com', name='test', password='test', join_date='1000-10-10', bio='test', city='test')
        db.session.add(test_user)
        db.session.commit()

def generate_venue_test_data():
    test_venue = Venue(venue_id='1', latitude = '37.782766928294', longitude = '-122.41017050455274', street_address = '982 Market St', city = 'San Francisco', state ='CA')
    db.session.add(test_venue)
    db.session.commit()

def generate_event_test_data():
    venue_id= Venue(venue_id='1')
    # db.session.add(venue_id)
    # db.session.commit()
    test_event= Event(event_id='1',venue_id='1', event_name='OSL', date='1001-11-11')
    db.session.add(test_event)
    db.session.commit()


def generate_memory_test_data():
    # user_id = User(user_id='1')
    # # db.session.add(user_id)
    # # db.session.commit()
    # event_id = Event(event_id='1')
    # # db.session.add(event_id)
    # # db.session.commit()
    test_memory = Memory(memory_id='1', user_id='1', event_id='1', fav_song='Light It Up', memory='Dancing with my friends.', squad ='Daisy, Mario, Yoshi')
    db.session.add(test_memory)
    db.session.commit()


# def clear_tables():
#     db.create_all()
#     Memory.query.delete()
#     User.query.delete()
#     Event.query.delete()
#     Venue.query.delete()
#     Picture.query.delete()
#     db.session.commit()

# os.system('clearing tsj')
# os.system('seeding tsj')
os.system('dropdb tsj')
os.system('createdb tsj')
connect_to_db(app)
db.create_all()
# clear_tables()

generate_user_test_data()
generate_venue_test_data()
generate_event_test_data()
generate_memory_test_data()


# generate_user_test_data()
# More code will go here

# if __name__ == '__main__': 
#     connect_to_db(app)
#     app.run(host='0.0.0.0', debug=True)
