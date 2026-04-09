from repo.Apprepo import AppRepo
from models.labcoordination import LabCoordinator
from repo.Apprepo import AppRepo
from models.bookslot import book
from models.equipment import Equipment

class labController:
    def __init__(self):
        self.curent_user=None
    def login(self):
        corid=int(input("Enter your coordinator id :"))
        if corid not in AppRepo.labCoordinator:
            print("CHECK YOUR id ")
            return False
        print("LOGIN SUCCESSFULL")
        self.curent_user=AppRepo.labCoordinator[corid]
        print("welcome",LabCoordinator.get_coor_name(self.curent_user))
        return True
    def askpermission(self,u_id,lab_id):
        # if u_id in [1,2,3]:
        #     if lab_id =='l1':
        return True
    def grant_boking(self):
        corlab=LabCoordinator.get_lab_id(self.curent_user)
        for i,v in AppRepo.booking.items():
            if book.get_lab_id(v)==corlab:
                print(f"Student id:{book.get_user_id(v)}  |  Equipment:{Equipment.get_eq_name(AppRepo.equipment[book.get_eq_id(v)])} | slot:{book.get_slot_id(v)}")