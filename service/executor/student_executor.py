from http import HTTPStatus
from ..utils.validation_utils import ValidationUtils
from ..services.student_service import StudentService


class StudentExecutor:
    def addStudent(request):
      try:   
            ValidationUtils.isEmpty(request.get('fname'),'fname')
            ValidationUtils.isEmpty(request.get('lname'),'lname')
            ValidationUtils.isEmpty(request.get('email'),'email')
            ValidationUtils.isZero(request.get('degree_id'),'degree_id')
            ValidationUtils.isNone(request.get('joining_year'),'joining_year')
      except Exception as e:
          return {'message': str(e)}, HTTPStatus.BAD_REQUEST
      
      return StudentService.addStudent(request), HTTPStatus.OK
    
    def updateStudent(request):
        try:
            ValidationUtils.isEmpty(request.get('fname'),'fname')
            ValidationUtils.isEmpty(request.get('lname'),'lname')
            ValidationUtils.isEmpty(request.get('student_id'),'student_id')
            ValidationUtils.isEmpty(request.get('email'),'email')
            ValidationUtils.isZero(request.get('degree_id'),'degree_id')
            ValidationUtils.isNone(request.get('joining_year'),'joining_year')
        except Exception as e:
                return {'message': str(e)}, HTTPStatus.BAD_REQUEST
        
        return StudentService.updateStudent(request)