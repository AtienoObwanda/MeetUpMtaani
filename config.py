import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL').replace("://", "ql://", 1)


class ProdConfig(Config):
    '''
    Prod
    '''
SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL') .replace("://", "ql://", 1)

DEBUG = True

class DevConfig(Config):
   pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}