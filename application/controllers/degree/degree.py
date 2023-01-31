from flask_restx import Namespace,Resource
from flask import request
from api.dto.dto import DegreeDto
from service.executor.degree_executor import DegreeExecutor

degree_namespace = DegreeDto.api

@degree_namespace.route("")
class addorUpdateDegree(Resource):