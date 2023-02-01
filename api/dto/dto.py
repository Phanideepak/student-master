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
    add_student_request = api.model('add_student_request',{
        'fname': fields.String(attribute = 'fname', description = 'student fname',required=True),
        'lname': fields.String(attribute = 'lname', description = 'student lname',required=True),
        'student_id': fields.String(attribute='student_id', description='student id',required=True),
        'email': fields.String(attribute = 'email', description = 'student email', required=True),
        'degree_id': fields.Integer(attribute = 'degree_id', description =' student degree identifier', required=True),
        'joining_date': fields.Date(attribute = 'joining_date', required=True) 
    })
    
    update_student_request = api.model('update_student_request',{
        'id' : fields.String(attribute = 'id',description = 'student id',required=True),
        'fname': fields.String(attribute = 'fname', description = 'student fname',required=True),
        'lname': fields.String(attribute = 'fname', description = 'student fname',required=True),
        'email': fields.String(attribute = 'email', description = 'student email', required=True),
        'degree_id': fields.Integer(attribute = 'degree_id', description =' student degree identifier', required=True),
        'joining_year': fields.Date(attribute = 'joining_year', required=True) 
    })
    
class DegreeDto:
    api = Namespace('degree', description='Namespace for degree apis')
    add_degree_request = api.model('add_degree_request',{
        'name': fields.String(attribute = 'name', description = 'degree name', required=True),
        'description': fields.String(attribute = 'description', description = 'degree description', required=True),
        'duration': fields.Integer(attribute = 'duration', description = 'duration', required=True),
        'single': fields.Boolean(attribute='single', description= 'single or dual degree', required=True)
    })
    update_degree_request = api.model('update_degree_request',{
        'id': fields.Integer(attribute='id', description= 'degree id', required=True),
        'name': fields.String(attribute = 'name', description = 'degree name', required=True),
        'description': fields.String(attribute = 'description', description = 'degree description', required=True),
        'duration': fields.Integer(attribute = 'duration', description = 'duration', required=True),
        'single': fields.Boolean(attribute='single', description= 'single or dual degree', required=True)
    })
    associate_dept_degree_request = api.model('associate_dept_degree_request',{
        'dept_id': fields.Integer(attribute ='dept_id', description = 'department id',required=True),
        'degree_id': fields.Integer(attribute = 'degree_id',description = 'degree_id',required=True)
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