from flask_restx import Namespace,Resource
from api.dto.dto import StudentDto
from flask import request
from service.executor.student_executor import StudentExecutor


student_name_space = StudentDto.api

@student_name_space.route("")
class StudentApi(Resource):
    
    @student_name_space.expect(StudentDto.add_student_request,validate=True)
    def post(self):
        """
        Register new student
        """
        return StudentExecutor.addStudent(request.get_json())
    
    @student_name_space.expect(StudentDto.update_student_request,validate=True)    
    def put(self):
        """
        Update new student
        """
        return StudentExecutor.updateStudent(request.get_json())
    
@student_name_space.route("/<student_id>")
class StudentOperationsById(Resource):
    def get(self, student_id):
        """
        Fetch student by id
        """
        pass
    def put(self, student_id):
        """
        Update student by id
        """
        pass
    def delete(self, student_id):
        """
        Delete student by id
        """
        pass

@student_name_space.route("/all")
class FetchStudentLists(Resource):
    def get(self):
       """
       Get all students
       """ 
       return StudentExecutor.getallStudents()
       