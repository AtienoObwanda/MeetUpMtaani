from ctypes import addressof
from enum import unique
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from datetime import datetime

from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



#User Model:
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(120), nullable=False, default='adminDefault.png')
    firstName = db.Column(db.String(50), unique=False, nullable=False)
    lastName = db.Column(db.String(50), unique=False, nullable=False)
    address = db.Column(db.String(50), unique=False, nullable=False)
    pNumber = db.Column(db.Integer(), unique=False, nullable=False)
    password = db.Column(db.String(60),nullable=False)
    reservation = db.relationship('Reservation', backref='user',lazy=True)

    def __repr__(self):
        return f'User({self.username},{self.email},{self.image})'


#User Reservation:
class Reservation (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numberOfPeople= db.Column(db.Integer())
    deals = db.Column(db.String(255), index = True,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) 

def __repr__(self):
    return f"Reservation({self.numberOfPeople}, {self.deals},{self.user_id})"

# Comment
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(100))


def __repr__(self):
    return f'User({self.comment})'
