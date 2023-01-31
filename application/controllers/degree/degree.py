from flask_restx import Namespace,Resource
from flask import request
from api.dto.dto import DegreeDto
from service.executor.degree_executor import DegreeExecutor

degree_namespace = DegreeDto.api

@degree_namespace.route("")
class addorUpdateDegree(Resource):
    
    @degree_namespace.expect(DegreeDto.add_degree_request,validate=True)
    def post(self):
        return DegreeExecutor.addDegree(request.get_json())
    
    @degree_namespace.expect(DegreeDto.update_degree_request)
    def put(self):
        return DegreeExecutor.updateDegree(request.get_json())