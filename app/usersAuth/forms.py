from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import Form,StringField, TextAreaField, SubmitField,PasswordField,BooleanField,IntegerField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo, ValidationError
from app.models import *
from flask_login import current_user
from datetime import datetime


class RegistrationForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password: ', validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(),EqualTo('password')])
    
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. PLease choose a different one.')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. PLease choose a different one.')

    
    
class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Sign In')
    
    
    
class ReviewForm(FlaskForm):
    comment = TextAreaField('Say something', validators = [DataRequired()])
    submit = SubmitField('Comment')
    
class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    
    bio =TextAreaField('About yourself', validators=[DataRequired()])
    
    submit = SubmitField('Update')
    
    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. PLease choose a different one.')
    
    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. PLease choose a different one.')

class ReservationForm(FlaskForm):
    fname = StringField('First Name: ', validators=[DataRequired()])
    
    lname = StringField('Last Name: ', validators=[DataRequired()])
    
    address = StringField('Address: ', validators=[DataRequired()])
    
    pnumber = IntegerField('Mobile Number: ',validators=[DataRequired()])
    
    reserveFrom = StringField('Date From:', validators=[DataRequired()])
    
    reserveTo = StringField('Date To:', validators=[DataRequired()])
    
    mDeal = SelectField('Mtaani Deal', choices=[("She's Mine", "She's mine"), (
        'Pick In a Nick', 'Pick In a Nick'), ('Working Space', 'Working Space')], validators=[DataRequired()])

    submit = SubmitField('Reserve')
        