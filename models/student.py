from models.user import User
from repo.Apprepo import AppRepo
class student(User):
    def __init__(self, user_id, username, cgpa,role):
        super().__init__(user_id, username, role)
        
        self.__cgpa=cgpa
        AppRepo.student[user_id]=self
    def get_reg_no(self):
        return super().get_user_id()
    def get_name(self):
        return super().get_username()
    def get_cgpa(self):
        return self.__cgpa
    