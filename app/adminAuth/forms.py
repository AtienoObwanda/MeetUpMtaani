from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators  import DataRequired, Length, Email,EqualTo, ValidationError
from flask_login import current_user

from ..models import Admin

class SignupForm(FlaskForm):
    username = StringField('Admin Username:', validators=[DataRequired(), Length(min=4, max=15)])
    
    email = StringField('Admin Email:', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password:', validators=[DataRequired(),Length(min=6,max=12),
                EqualTo('confirm_password',message='Passwords must match')])
    
    confirm_password = PasswordField('Confirm Password:', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Join as Admin')

    def validate_username(self, username):
        admin = Admin.query.filter_by(username=username.data).first()
        if admin:
            raise ValidationError('Admin username already in use!')

    def validate_email(self, email):
        admin = Admin.query.filter_by(email=email.data).first()
        if admin:
            raise ValidationError('Admin email already in use!')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])

    password = PasswordField('Password',
                    validators=[DataRequired(),Length(min=6,max=12)])

    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                    validators=[DataRequired(),Length(min=4, max=15)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    
    picture= FileField('Update profile picture',validators=[FileAllowed(['jpg','png','jpeg'])])
    
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            admin= Admin.query.filter_by(username=username.data).first()
            if admin:
                raise ValidationError('Username is already in use!')


    def validate_email(self, email):
        if email.data != current_user.email:
            admin= Admin.query.filter_by(email=email.data).first()
            if admin:
                raise ValidationError('Email is already in use!')


class AddDealForm(FlaskForm):
    title = StringField('Post Title',validators=[DataRequired()])

    picture= FileField('Update profile picture',validators=[FileAllowed(['jpg','png','jpeg'])])

    dealPrice = StringField('Post Title',validators=[DataRequired()])

    submit = SubmitField('Add Deal')


class UpdateDealForm(FlaskForm):
    title = StringField('Post Title',validators=[DataRequired()])

    picture= FileField('Update profile picture',validators=[FileAllowed(['jpg','png','jpeg'])])

    dealPrice = StringField('Post Title',validators=[DataRequired()])

    submit = SubmitField('Update Deal')



