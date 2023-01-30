import os 
from decouple import config
from datetime import timedelta

class Config:
    SECRET_KEY = config('SECRET_KEY','secret')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(30)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    
class DevelopmentConfig(Config):
    DEBUG = config('DEBUG', cast = bool)
    SQLALCHEMY_ECHO =True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/admin?password=Phani@dev'
    SQLALCHEMY_BINDS = {
    'my_sql1': 'mysql://root:password@localhost/quickhowto',
    'my_sql2': 'mysql://root:password@externalserver.domain.com/quickhowto2'
}
    
class QAConfig(Config):
    pass

class ProdConfig(Config):
    pass

config_dict = {
    'dev': DevelopmentConfig,
    'qa': QAConfig,
    'prod': ProdConfig
}