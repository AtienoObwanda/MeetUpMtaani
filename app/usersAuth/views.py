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
        user = User.query.filter_by(username = form.username.data).first()
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


@auth.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = ProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated.','success')
        return redirect(url_for('auth.account'))
    elif request.method =='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename='profile_pics/' + current_user.image_file)
    return render_template('usersTemplate/dashboard.html', title='Account', image_file = image_file, form = form)

@auth.route('/reserve', methods=['GET', 'POST'])
@login_required
def reserve():
    form = ReservationForm()
    if form.validate_on_submit():
        reservation = Reservation(fname=form.fname.data, lname=form.lname.data, email=form.email.data,
                                    pnumber=form.pnumber.data,reserve=form.reserve.data)
        db.session.add(reservation)
        db.session.commit()
        flash('Your reservation has been updated', 'success')
    return redirect(url_for('main.index'))