from flask import Flask
from flask_restx import Api
from .controllers.auth.auth import auth_name_space
from .controllers.student.student import student_name_space
from config.main.config import config_dict

def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    api.add_namespace(auth_name_space, path= "/auth")
    api.add_namespace(student_name_space, path="/student")
    
    return app