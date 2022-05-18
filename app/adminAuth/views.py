import os
import email
from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_user,current_user, logout_user, login_required
import secrets
from PIL import Image

from .. import db, bcrypt
from ..models import User,Reservation,Deals,Review
from .forms import SignupForm,LoginForm,UpdateAccountForm,AddDealForm,UpdateDealForm

from . import admin

@admin.route('/signup' , methods=['GET','POST'])
def adminRegister():
    if current_user.is_authenticated:
        return redirect(url_for('admin.adminDashboard'))
    
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        db.session.add(user) # add user
        db.session.commit() # commit session
        

        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('admin.adminLogin'))
    return render_template("adminTemplate/signup.html", title='Admin-SignUP', form=form)


@admin.route('/login',methods=['GET', 'POST'])
def adminLogin():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next') #  when user tries to acccess restricted page
            return redirect(next_page) if next_page else redirect(url_for('admin.adminDashboard')) # redirects to requested page after loggin in if it exists... if none, redirects to home page
        else:
            flash('Login Failed. Kindly check your email and password then try again','danger')
    return render_template("adminTemplate/login.html",form=form,title='Admin-Login')


@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))



def save_picture(form_picture): # saving image
    random_hex = secrets.token_hex(8) # generates new name for the picture
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('app/static/images', picture_fn)
    
    #image resizing
    output_size=(125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path) # resized image

    return picture_fn

# Update Admin account
@admin.route('/dashboard',methods=['GET', 'POST'])
@login_required 
def adminDashboard():
    user_id = current_user._get_current_object().id
    users=User.query.all()
    reservations=Reservation.query.all()
    deals = Deals.query.all()
    reviews = Review.query.all()
    form = UpdateAccountForm()
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
        form.username.data = current_user.username 
        form.email.data = current_user.email 
        image = url_for('static', filename='images/' + current_user.image) 
    return render_template("adminTemplate/adminDashboard.html", title='Account', users=users, reviews=reviews,deals=deals,reservations=reservations,form=form)


    