from repository.admin.service.repo_service import UserRepoService
from werkzeug.security import generate_password_hash,check_password_hash
from repository.admin.model.user import User

class UserService:
    def insertUser(request):
        UserRepoService.saveUser(User(username= request.get('username'),email = request.get('email'), 
                                            password_hash = generate_password_hash(request.get('password'))))
        return {'message': 'added sucessfully'}