from flask import Flask
from flask_restx import Api
from .controllers.auth.auth import auth_name_space
from .controllers.student.student import student_name_space
from .controllers.department.department import department_namespace
from config.main.config import config_dict
from repository import adminDB
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)
    adminDB.init_app(app)
    migrate = Migrate(app , adminDB)
    api = Api(app)
    api.add_namespace(auth_name_space, path= "/auth")
    api.add_namespace(student_name_space, path="/student")
    api.add_namespace(department_namespace, path= "/department")
    jwt = JWTManager(app)
    
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':adminDB
        }
    
    
    return app