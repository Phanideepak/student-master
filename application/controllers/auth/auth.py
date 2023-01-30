from flask_restx import Namespace,Resource
from api.dto.dto import UserDto
from flask import request
from service.executor.auth_executor import AuthExecutor
from http import HTTPStatus

auth_name_space = UserDto.api


@auth_name_space.route("/signup")
class SignUp(Resource):
    @auth_name_space.expect(UserDto.user_request_dto, validate = True)
    def post(self):
        """
        create new user
        
        """
        return AuthExecutor.addUser(request= request.get_json())
    
@auth_name_space.route("/login")
class Login(Resource):
    def post(self):
        """
        generate JWT token
        """
        pass