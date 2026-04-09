from models.user import User
from repo.Apprepo import AppRepo
class LabCoordinator(User):
    def __init__(self,user_id, username,lab_id,lab_name, role):
        super().__init__(user_id, username, role)
        
        self.__lab_id=lab_id
        self.__lab_name=lab_name
        AppRepo.labCoordinator[user_id]=self
    def get_coor_id(self):
        return super().get_user_id()
    def get_coor_name(self):
        return super().get_username()
    def get_lab_id(self):
        return self.__lab_id
    def get_labname(self):
        return self.__lab_name