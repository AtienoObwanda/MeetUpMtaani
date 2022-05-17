from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_user,current_user, logout_user, login_required
import secrets
from . import auth



@auth.route('/register', methods=['GET','POST'])
def register():
    title = 'Register'


    flash(f'Account created successfully!', 'success')
    # return redirect(url_for('auth.login'))
    
    return render_template("auth/register.html", title='Meet up Mtaani',form=form)