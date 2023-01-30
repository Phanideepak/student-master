import os 
from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY','secret')
    
class DevelopmentConfig(Config):
    DEBUG = config('DEBUG', cast = bool)
    SQLALCHEMY_ECHO =True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Phani@dev@127.0.0.1/admin'
    
class QAConfig(Config):
    pass

class ProdConfig(Config):
    pass

config_dict = {
    'dev': DevelopmentConfig,
    'qa': QAConfig,
    'prod': ProdConfig
}