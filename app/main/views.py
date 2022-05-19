from flask import render_template,request,redirect,url_for
from . import main
from ..models import Review, Reservation,User
from flask_login import login_required


# Views

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    title = "Home- Welcome to the most reliable meetup website "

    
    return render_template('index.html', title=title )

@main.route('/aboutUs')
def aboutUs():
    '''
    View page function that returns the aboutUs page and its data.
    '''
    title = 'About Us'
    return render_template('aboutUs.html', title=title)

@main.route('/reviews')
def reviews():

    title = 'Reviews'
    return render_template('viewReviews.html',title=title)



@main.route('/deals')
def deals():

    title = 'deals'
    return render_template('viewDeals.html', title=title)