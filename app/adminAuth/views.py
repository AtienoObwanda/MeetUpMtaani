import email
from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_user,current_user, logout_user, login_required
import secrets
from PIL import Image

from .. import db, bcrypt
from ..models import Admin,User,Reservation,Deals,Review
from .forms import SignupForm

from . import admin

@admin.route('/register', methods=['GET','POST'])
def admin():
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
        return redirect(url_for('admin.login'))
    return render_template("admin/register.html", title='Admin', form=form)

