from repository.students.service.student_repo_service import StudentRepoService
from repository.students.model.student import Student

class StudentService:
    def addStudent(request):
        """
                'fname': fields.String(attribute = 'fname', description = 'student fname',required=True),
        'lname': fields.String(attribute = 'fname', description = 'student fname',required=True),
        'email': fields.String(attribute = 'email', description = 'student email', required=True),
        'degree_id': fields.Integer(attribute = 'degree_id', description =' student degree identifier', required=True),
        'joining_year': fields.Date(attribute = 'joining_year', required=True) 
        }),
        """
        print(request)
        StudentRepoService.saveStudent(Student(first_name=request.get('fname'),last_name=request.get('lname'),
                                               email=request.get('email'),degree_id=request.get('degree_id'),
                                               joining_date=request.get('joining_date')
                                               ))
        return {'message': 'added sucessfully'}
        
    def updateStudent(request):
        pass