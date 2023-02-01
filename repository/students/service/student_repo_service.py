from ..model.student import Student,Department,UniversityDegree,DepartmentDegreeMapping


class StudentRepoService:
    def saveStudent(student):
        student.save()
        
    def getById(id):
        return Student.query.filter_by(id = id).first()
    
    def getByStudentId(student_id):
        return Student.query.filter_by(student_id = student_id).first()
    
    def getLatestStudentCountByDeptId(dept_id):
        return Student.query.filter_by(dept_id=dept_id).count()

class DepartmentRepoService:
    def saveDepartment(department : Department):
        department.save()
        
    def getById(department_id):
        return Department.query.filter_by(id = department_id).first()
    
class DegreeRepoService:
    def saveDegree(degree):
        degree.save()
    
    def getById(id):
        return UniversityDegree.query.filter_by(id = id).first()

class DepartmentDegreeMappingRepoService:
    def saveDepartmentDegreeMapping(mapping):
        mapping.save()
        
    def getByDeptIdAndDegreeId(dept_id, degree_id):
        return  DepartmentDegreeMapping.query.filter_by(degree_id = degree_id,dept_id = dept_id).first()  