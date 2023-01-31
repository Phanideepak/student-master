from http import HTTPStatus
from repository.students.model.student import UniversityDegree
from repository.students.service.student_repo_service import DegreeRepoService

class DegreeService:
    def addDegree(request):
        DegreeRepoService.saveDegree(UniversityDegree(name = request.get('name'),description=request.get('description'),
                                                      duration=request.get('duration'),is_single = request.get('single')))
        return {'message': 'added sucessfully'}