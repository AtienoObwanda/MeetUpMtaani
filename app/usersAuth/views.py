import os
from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_user,current_user, logout_user, login_required
import secrets
from . import auth
from .. import bcrypt,db
from .forms import *
from ..models import *
from PIL import Image



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email = form.email.data, username = form.username.data,password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('usersTemplate/register.html',form = form)

@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('Invalid')
    return render_template('usersTemplate/login.html', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

def save_picture(form_picture): # saving image
    random_hex = secrets.token_hex(8) # geneates new name for the picture
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('app/static/images', picture_fn)
    
    #image resizing
    output_size=(125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path) # resized image

    return picture_fn

@auth.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = ProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data) # seting picture 
            current_user.image = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Account details for {form.username.data} successfully updated!', 'sucess')
        return redirect(url_for('auth.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username # Populate user username on to the form
        form.email.data = current_user.email # Populate user email on to the form
    image = url_for('static', filename='profile/' + current_user.image) # route for default profile picture
     
    return render_template("usersTemplate/dashboard.html", title='Account', image=image, form=form)

@auth.route('/reserve', methods=['GET', 'POST'])
@login_required
def reserve():
    form = ReservationForm()
    if form.validate_on_submit():
        reservation = Reservation(firstName=form.firstName.data, lastName=form.lastName.data, deal=form.deal.data,
                                user_id = current_user.id, pNumber=form.pNumber.data, address=form.address.data)
        db.session.add(reservation)
        db.session.commit()
        flash('Your reservation has been updated', 'success')
        return redirect(url_for('main.index'))
    return render_template("usersTemplate/reservation.html", title='reserve', form=form)





@auth.route('/userdashboard/')
def userAccount():
    '''
    View page function that returns the aboutUs page and its data.
    '''
    
    return render_template('usersTemplate/userDashboard.html')