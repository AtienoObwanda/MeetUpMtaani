from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_user,current_user, logout_user, login_required
import secrets
from PIL import Image

from .. import db, bcrypt
from ..models import Admin,User,Reservation,Deals,Review

from . import admin

