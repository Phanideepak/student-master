from flask_restx import Namespace,Resource
from flask import request
from api.dto.dto import DepartmentDto
from service.executor.dept_executor import DeptExecutor

department_namespace = DepartmentDto.api

@department_namespace.route("")
class addorUpdateDepartment(Resource):
    @department_namespace.expect(DepartmentDto.add_department_request, validate = True)
    def post(self):
        return DeptExecutor.addDepartment(request.get_json())
    
    @department_namespace.expect(DepartmentDto.update_department_request, validate = True)
    def put(self):
        return DeptExecutor.updateDepartment(request.get_json())