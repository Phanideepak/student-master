from ..model.student import Student,Department,UniversityDegree

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