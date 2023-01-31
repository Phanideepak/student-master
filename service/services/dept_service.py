from  repository.students.service.student_repo_service import DepartmentRepoService
from  repository.students.model.student import Department
from http import HTTPStatus


class DeptService:
    def addDepartment(request):
        DepartmentRepoService.saveDepartment(Department(name = request.get('name'), description= request.get('description'),
                                                        hod = request.get('hod_details').get('name'),email =request.get('hod_details').get('email'),
                                                        phone = request.get('hod_details').get('phone')
                                                        ))
        return {'message': 'added sucessfully'}
    
    
    def updateDepartment(request):
        department = DepartmentRepoService.getById(request.get('department_id'))
        if department is None:
            return {'message': f"department with id : f{request.get('department_id')} not found"}
        
        is_update_required = False
        
        if request.get('name') != department.name:
            is_update_required = True
            department.name = request.get('name')
            
        if request.get('description') != department.description:
            is_update_required = True
            department.description = request.get('description')
        
        if request.get('hod_details').get('name') != department.hod:
            is_update_required = True
            department.hod = request.get('hod_details').get('name')
            
                    
        if request.get('hod_details').get('email') != department.email:
            is_update_required = True
            department.email = request.get('hod_details').get('email')
                
        if request.get('hod_details').get('phone') != department.phone:
            is_update_required = True
            department.phone = request.get('hod_details').get('phone')
        
        
        if not is_update_required:
            return {'message':'no field modified'}, HTTPStatus.NOT_MODIFIED
        
        DepartmentRepoService.saveDepartment(department)
        return  {'message':'updated successfully'}, HTTPStatus.OK   