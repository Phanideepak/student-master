from flask_restx import Namespace,Resource

student_name_space = Namespace('student', description ='Namespace for student apis')

@student_name_space.route("/")
class HomeAuth(Resource):
    def get(self):
        return {"student":"welcome back"}