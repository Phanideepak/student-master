from flask_restx import Namespace,Resource
from api.dto.dto import UserDto
from flask import request
from service.executor.auth_executor import AuthExecutor
from http import HTTPStatus
from flask_jwt_extended import jwt_required,get_jwt_identity,create_access_token
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
    @auth_name_space.expect(UserDto.login_request_dto, validate = True)
    def post(self):
        """
        generate JWT token
        """
        return AuthExecutor.loginUser(request = request.get_json())
        
@auth_name_space.route("/refresh")
class Refresh(Resource):
    
    #refresh token needed in authorization header.
    @jwt_required(refresh = True)
    def post(self):
        """
          refresh token
        """
        username = get_jwt_identity()
        access_token = create_access_token(identity = username)
        return {'accessToken':access_token}, HTTPStatus.OK
        