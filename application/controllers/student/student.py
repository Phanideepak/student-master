from flask_restx import Namespace,Resource

student_name_space = Namespace('student', description ='Namespace for student apis')

@student_name_space.route("")
class StudentApi(Resource):
    def post(self):
        """
        Register new student
        """
        pass
    
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
    def get(self, active):
       """
       Get all students
       """ 
       pass