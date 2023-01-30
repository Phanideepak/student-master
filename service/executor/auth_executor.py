from service.services.user_service import UserService
from http import HTTPStatus
from ..utils.validation_utils import ValidationUtils

class AuthExecutor:
    def addUser(request):
        try:
            ValidationUtils.isEmpty(request.get('username'),'username')
            ValidationUtils.isEmpty(request.get('email'),'email')
            ValidationUtils.isEmpty(request.get('password'),'password')
        except Exception as e:
            return {'message': str(e)}, HTTPStatus.BAD_REQUEST
        return UserService.insertUser(request), HTTPStatus.CREATED
    
    def loginUser(request):
        try:
            ValidationUtils.isEmpty(request.get('email'),'email')
            ValidationUtils.isEmpty(request.get('password'),'password')
        except Exception as e:
            return {'message': str(e)}, HTTPStatus.BAD_REQUEST
        return UserService.loginUser(request)