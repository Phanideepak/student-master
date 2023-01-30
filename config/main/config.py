import os 
from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY','secret')
    
class DevelopmentConfig(Config):
    DEBUG = config('DEBUG', cast = bool)
    
class QAConfig(Config):
    pass

class ProdConfig(Config):
    pass

config_dict = {
    'dev': DevelopmentConfig,
    'qa': QAConfig,
    'prod': ProdConfig
}