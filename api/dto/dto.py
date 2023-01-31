from flask_restx import Namespace,fields

class DepartmentDto:
    api = Namespace('department',description= 'Namespace for department apis')
    hod_details = api.model('hod_details',{
        'name' : fields.String(attribute = 'name', description = 'hod name', required=True),
        'email': fields.String(attribute = 'email', description = 'hod email', required=True),
        'phone' : fields.String(attribute = 'phone', description = 'hod contact', required=True) 
    })
    add_department_request = api.model('department',{
        'name': fields.String(attribute = 'name', description = 'department name', required=True),
        'description': fields.String(attribute = 'description', description = 'department description', required=True),
        'hod_details': fields.Nested(hod_details,required=True)        
    })
    update_department_request = api.model('department',{
        'department_id': fields.Integer(attribute = 'id', description = 'department id', required=True),
        'name': fields.String(attribute = 'name', description = 'department name', required=True),
        'description': fields.String(attribute = 'description', description = 'department description', required=True),
        'hod_details': fields.Nested(hod_details,required=True) 
    })

class StudentDto:
    api = Namespace('student', description ='Namespace for student apis')
    student = api.model('student',{
        'name': fields.String(attribute = 'name', description = 'student name',required=True)
    })

class UserDto:
    api = Namespace('auth', description ='Namespace for authentication')
    user_request_dto = api.model('user',{
        'id' : fields.Integer(),
        'username': fields.String(attribute = 'user_name', description = 'user name', required=True),
        'email': fields.String(attribute = 'email', description = 'user email id', required=True),
        'password': fields.String(attribute = 'pwd',description = 'user password', required = True),        
    })
    login_request_dto = api.model('user',{
        'email': fields.String(attribute = 'email', description = 'user email id', required=True),
        'password': fields.String(attribute = 'pwd',description = 'user password', required = True),
    })
    
    """
     id = adminDB.Column(adminDB.Integer, primary_key = True)
     username = adminDB.Column(adminDB.String(45), unique = True, nullable = False)
     email = adminDB.Column(adminDB.String(50), unique = True, nullable = False)
     password_hash = adminDB.Column(adminDB.Text(), nullable = False)
     is_admin = adminDB.Column(adminDB.Boolean(), default = False)
     is_active = adminDB.Column(adminDB.Boolean(), default = True)
    """