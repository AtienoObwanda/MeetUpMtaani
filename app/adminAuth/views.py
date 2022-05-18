import os
import email
from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_user,current_user, logout_user, login_required
import secrets
from PIL import Image

from .. import db, bcrypt
from ..models import Admin,User,Reservation,Deals,Review
from .forms import SignupForm,LoginForm,UpdateAccountForm,AddDealForm,UpdateDealForm

from . import admin

@admin.route('/signup', methods=['GET','POST'])
def adminSignup():
    # if current_user.is_authenticated():
    #     return redirect(url_for('admin.dashboard'))

    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        admin = Admin(username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(admin)
        db.session.commit()
    #Insert mails to admin message
        flash(f'{form.username.data} added successfully as admin!','success')
        return redirect(url_for('admin.adminLogin'))
    return render_template("adminTemplate/signup.html", title='Admin-SignUP', form=form)

@admin.route('/login',methods=['GET', 'POST'])
def adminLogin():

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()

    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin, remember = form.remember.data)

            next_page = request.args.get('next') #  when user tries to acccess restricted page

            return redirect(next_page) if next_page else redirect(url_for('main.index')) # redirects to requested page after loggin in if it exists... if none, redirects to home page
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
# @login_required 
def adminDashboard():

    return render_template("adminTemplate/adminDashboard.html", title='Account')


    