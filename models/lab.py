from repo.Apprepo import AppRepo
class Lab:
    def __init__(self,lab_id,lab_name,equipment):
        self.__lab_id=lab_id
        self.__lab_name=lab_name
        self.__equipment=equipment
        AppRepo.lab[lab_id]=self
    def get_lab_id(self):
        return self.__lab_id
    def get_lab_name(self):
        return self.__lab_name
    def get_equipment(self):
        return self.__equipment