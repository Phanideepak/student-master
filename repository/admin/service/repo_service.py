from ..model.user import User

class UserRepoService:
    def saveUser(user):
        user.save()
    
    def getUserByEmail(email):
        return User.query.filter_by(email = email).first()