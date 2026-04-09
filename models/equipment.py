from repo.Apprepo import AppRepo
class Equipment:
    def __init__(self,labid,eq_id,eq_name,eq_count):
        self.__lab_id=labid
        self.__eq_id=eq_id
        self.__eq_name=eq_name
        self.__eq_count=eq_count
        AppRepo.equipment[eq_id]=self
    def get_lab_id(self):
        return self.__lab_id
    
    def get_eq_id(self):
        return self.__eq_id
    
    def get_eq_name(self):
        return self.__eq_name
    
    def get_eq_count(self):
        return self.__eq_count

    # def set_eq_count(self):
    #     self.__eq_count-=1
    
    # def update_eq_count(self):
    #     self.__eq_count+=1