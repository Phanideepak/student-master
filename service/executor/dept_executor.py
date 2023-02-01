from http import HTTPStatus
from ..utils.validation_utils import ValidationUtils
from ..services.dept_service import DeptService

class DeptExecutor:
    def addDepartment(request):
        try:
            ValidationUtils.isEmpty(request.get('name'),'name')
            ValidationUtils.isEmpty(request.get('description'), 'description')
            ValidationUtils.isNone(request.get('hod_details'),'hod_details')
            ValidationUtils.isEmpty(request.get('hod_details').get('name'),'hod_details.name')
            ValidationUtils.isEmpty(request.get('hod_details').get('email'),'hod_details.email')
            ValidationUtils.isEmpty(request.get('hod_details').get('phone'),'hod_details.phone')
        except Exception as e:
            return {'message': str(e)}, HTTPStatus.BAD_REQUEST
        
        return DeptService.addDepartment(request), HTTPStatus.OK
    
    def updateDepartment(request):
        try:
            ValidationUtils.isZero(request.get('department_id'),'department_id')
            ValidationUtils.isEmpty(request.get('name'),'name')
            ValidationUtils.isEmpty(request.get('description'), 'description')
            ValidationUtils.isNone(request.get('hod_details'),'hod_details')
            ValidationUtils.isEmpty(request.get('hod_details').get('name'),'hod_details.name')
            ValidationUtils.isEmpty(request.get('hod_details').get('email'),'hod_details.email')
            ValidationUtils.isEmpty(request.get('hod_details').get('phone'),'hod_details.phone')
        except Exception as e:
            return {'message': str(e)}, HTTPStatus.BAD_REQUEST
        
        return DeptService.updateDepartment(request)