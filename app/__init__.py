from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail





from config import config_options

# Initializing extensions
db = SQLAlchemy()
bcrypt = Bcrypt() # Password encryption 
mail = Mail() 


# Login manager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = {
    'admin': '/admin/login',
    'site': '/login',
}
login_manager.login_message_category='info'



def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    # Adding the main blue print
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # user's bluePrint
    from .usersAuth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

    # Admin bluePrint
    # from .adminAuth import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint,url_prefix='/admin')
    
    return app