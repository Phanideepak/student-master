from repository.students.service.student_repo_service import StudentRepoService,DegreeRepoService
from repository.students.model.student import Student

class StudentService:
    def addStudent(request):
        degree = DegreeRepoService.getById(request.get('degree_id'))

        if degree is None:
            return {'message': f"degree with id : f{request.get('degree_id')} not found"}
        StudentRepoService.saveStudent(Student(first_name=request.get('fname'),last_name=request.get('lname'),
                                               email=request.get('email'),degree_id=request.get('degree_id'),
                                               joining_date=request.get('joining_date'), student_id = request.get('student_id')
                                               ))
        return {'message': 'added sucessfully'}
        
    def updateStudent(request):
        pass