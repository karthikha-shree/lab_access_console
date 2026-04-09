from repo.Apprepo import AppRepo
class book:
    def __init__(self,user_id,eq_id,slot_id,permit='pending',lab_id=None):
        self.__user_id=user_id
        self.__eq_id=eq_id
        self.__slot_id=slot_id
        self.__permit=permit
        self.__lab_id=lab_id if lab_id is not None else AppRepo.equipment[eq_id].get_lab_id()
        AppRepo.booking[(user_id,eq_id)]=self
    def get_user_id(self):
        return self.__user_id
    def get_eq_id(self):
        return self.__eq_id
    def get_slot_id(self):
        return self.__slot_id
    def get_permit(self):
        return self.__permit
    def get_lab_id(self):
        return self.__lab_id
    def set_permit(self,p):
        self.__permit=p
    
