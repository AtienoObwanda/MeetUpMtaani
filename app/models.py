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
    password = db.Column(db.String(60),nullable=False)
    reservation = db.relationship('Reservation', backref='user',lazy=True)

    def __repr__(self):
        return f'User({self.username},{self.email},{self.image})'



# Deals:
class Deals (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dealPrice = db.Column(db.Integer, unique=False, nullable=False)
    title = db.Column(db.String(100), unique=True, nullable=False)
    image = db.Column(db.String(120), nullable=False)

def __repr__(self):
    return f"Deals({self.title},{self.dealPrice},{self.image})"

#User Reservation:
class Reservation (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservedFrom = db.Column(db.DateTime, nullable=False,default=datetime) # yet to confirm format
    reservedTill = db.Column(db.DateTime, nullable=False,default=datetime)   # yet to confirm format
    deals_id = db.Column(db.Integer,db.ForeignKey('deals.id'),nullable=False) #deal
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #user

def __repr__(self):
    return f"Reservation({self.reservedFrom},{self.reservedTill})"

# Comment
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(100))


def __repr__(self):
    return f'User({self.comment})'
