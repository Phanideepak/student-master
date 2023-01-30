from flask_restx import Namespace,Resource

auth_name_space = Namespace('auth', description ='Namespace for authentication')

@auth_name_space.route("/")
class HomeAuth(Resource):
    def get(self):
        return {"home":"welcome back"}