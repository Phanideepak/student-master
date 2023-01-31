from http import HTTPStatus
from ..utils.validation_utils import ValidationUtils
from ..services.degree_service import DegreeService

class DegreeExecutor:
    def addDegree(request):
        try:
          ValidationUtils.isEmpty(request.get('name'),'name')
          ValidationUtils.isEmpty(request.get('description'),'description')
          ValidationUtils.isZero(request.get('duration'),'duration')
          ValidationUtils.isNone(request.get('single'),'single')
        except Exception as e:
            return {'message': str(e)}, HTTPStatus.BAD_REQUEST
        
        return DegreeService.addDegree(request),HTTPStatus.OK
    
    def updateDegree(request):
       try:
          ValidationUtils.isZero(request.get('id'),'id')
          ValidationUtils.isEmpty(request.get('name'),'name')
          ValidationUtils.isEmpty(request.get('description'),'description')
          ValidationUtils.isZero(request.get('duration'),'duration')
          ValidationUtils.isNone(request.get('single'),'single')
       except Exception as e:
            return {'message': str(e)}, HTTPStatus.BAD_REQUEST
        
       return DegreeService.updateDegree(request)
   
    def associateDepartment(request):
        try:
            ValidationUtils.isZero(request.get('dept_id'),'dept_id')
            ValidationUtils.isZero(request.get('degree_id'),'degree_id')
        except Exception as e:
            return {'message':str(e)},HTTPStatus.BAD_REQUEST
        
        return DegreeService.associateDept(request)
       
              