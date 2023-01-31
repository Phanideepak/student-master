from ..model.student import Student,Department

class DepartmentRepoService:
    def saveDepartment(department : Department):
        department.save()
        
    def getById(department_id):
        return Department.query.filter_by(id = department_id).first()