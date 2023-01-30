from repository.admin.service.repo_service import UserRepoService
from werkzeug.security import generate_password_hash,check_password_hash
from repository.admin.model.user import User
from http import HTTPStatus
from flask_jwt_extended import create_access_token,create_refresh_token

class UserService:
    def insertUser(request):
        UserRepoService.saveUser(User(username= request.get('username'),email = request.get('email'), 
                                            password_hash = generate_password_hash(request.get('password'))))
        return {'message': 'added sucessfully'}
    
    def loginUser(request):
        user = UserRepoService.getUserByEmail(request.get('email'))
        if user is None:
            return {'message':f"user with email : {request.get('email')} not found"}, HTTPStatus.NOT_FOUND
        
        if not check_password_hash(user.password_hash,request.get('password')):
           return {'message': "Incorrect password given"}, HTTPStatus.UNAUTHORIZED
            
        response = {'accessToken':create_access_token(identity = user.username), 'refreshToken': create_refresh_token(identity = user.username)}
        response['message'] = 'login successful' 
        return response, HTTPStatus.OK