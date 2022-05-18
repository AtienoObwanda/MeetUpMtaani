import os

class Config:
    '''
    Parent config class
    '''
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://atieno:mishi@localhost/mtaani'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # Mail confugurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX = 'PITCH SPLASH!'
    SENDER_EMAIL = 'splashpitch@gmail.com'


    @staticmethod
    def init_app(app):
        pass



class ProdConfig(Config):
    pass

DEBUG = True


class DevConfig(Config):
    '''
    development class
    '''
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
# SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')
SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://atieno:mishi@localhost/mtaani'

DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

DEBUG = True
