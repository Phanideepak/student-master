from flask_restx import Namespace,Resource

auth_name_space = Namespace('auth', description ='Namespace for authentication')

@auth_name_space.route("/signup")
class SignUp(Resource):
    def post(self):
        """
        create new user
        
        """
        pass
    
@auth_name_space.route("/login")
class Login(Resource):
    def post(self):
        """
        generate JWT token
        """
        pass