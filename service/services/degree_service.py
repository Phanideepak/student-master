from http import HTTPStatus
from repository.students.model.student import UniversityDegree,DepartmentDegreeMapping
from repository.students.service.student_repo_service import DegreeRepoService,DepartmentRepoService, DepartmentDegreeMappingRepoService

class DegreeService:
    def addDegree(request):
        DegreeRepoService.saveDegree(UniversityDegree(name = request.get('name'),description=request.get('description'),
                                                      duration=request.get('duration'),is_single = request.get('single')))
        return {'message': 'added sucessfully'}
    
    def updateDegree(request):
        degree =  DegreeRepoService.getById(request.get('id'))
        if degree is None:
            return {'message': f"degree with id : f{request.get('id')} not found"}
        
        is_updated_required = False
        
        if request.get('name') != degree.name:
            is_updated_required = True
            degree.name = request.get('name')
            
        if request.get('description') != degree.description:
            is_updated_required = True
            degree.description = request.get('description')
        
        if request.get('duration') != degree.duration:
            is_updated_required = True
            degree.duration = request.get('duration')
        
        if request.get('single') != degree.is_single:
            is_updated_required = True
            degree.is_single = request.get('single')
            
        if not is_updated_required:
            return {'message':'no field modified'}, HTTPStatus.NOT_MODIFIED
        
        DegreeRepoService.saveDegree(degree)
        
        return  {'message':'updated successfully'}, HTTPStatus.OK    
        
    def associateDept(request):
        degree = DegreeRepoService.getById(request.get('degree_id'))
        if degree is None:
            return {'message': f"degree with id : f{request.get('id')} not found"}
        
        department = DepartmentRepoService.getById(request.get('dept_id'))
        if department is None:
            return {'message': f"department with id : f{request.get('dept_id')} not found"}
        
        mapping = DepartmentDegreeMappingRepoService.getByDeptIdAndDegreeId(request.get('dept_id'),request.get('degree_id'))
        if mapping is None:
            DepartmentDegreeMappingRepoService.saveDepartmentDegreeMapping(DepartmentDegreeMapping(dept_id=request.get('dept_id'),degree_id=request.get('degree_id')))
        
        return {'message':'associated successfully'}, HTTPStatus.OK
            