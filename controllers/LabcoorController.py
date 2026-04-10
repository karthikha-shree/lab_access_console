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
    # def setreject(self):
    #     corlab=LabCoordinator.get_lab_id(self.curent_user)
        
    def grant_boking(self):
        corlab=LabCoordinator.get_lab_id(self.curent_user)
        for i,v in AppRepo.booking.items():
            if book.get_lab_id(v)==corlab:
                print(f"Student id , Equipment id:{i} |Equipment:{Equipment.get_eq_name(AppRepo.equipment[book.get_eq_id(v)])} | slot:{book.get_slot_id(v)}")
        count=0
        while True:
            k=list(input("enter the studentid and equipment id to approve the slot separated by comma : ").split(","))
            print(k)
            if(k[0]=='stop'):
                break
            elif len(k)!=2:
                print("Enter the details properly ")
            else:
                if book.get_user_id(v) in AppRepo.userslot and book.get_slot_id(v) in AppRepo.userslot[book.get_user_id(v)]:
                    print("This student aldrady has a bookin at this slot ")
                elif(AppRepo.grantaccess[(AppRepo.equipment[book.get_eq_id(v)],book.get_slot_id(v))]>=Equipment.get_eq_count(AppRepo.equipment[book.get_eq_id(v)])) :
                    print("The equipment slot is aldrady filled !!")
                    break
                else:
                    if not book.get_user_id(v) in AppRepo.userslot :
                        AppRepo.userslot[book.get_user_id(v) ]=[]
                    AppRepo.userslot[book.get_user_id(v) ].append(book.get_slot_id(v))
                    book.set_permit(AppRepo.booking[int(k[0]),k[1]],"approved")
                    count+=1
                    AppRepo.grantaccess[(AppRepo.equipment[book.get_eq_id(v)],book.get_slot_id(v))]=count
                    print(book.get_permit(AppRepo.booking[int(k[0]),k[1]]))
        for i,v in AppRepo.booking.items():
            if book.get_lab_id(v)==corlab and book.get_permit(v)=='pending':
                book.set_permit(AppRepo.booking[i],"rejected")
        print("All pending requests are rejected ")
        print("Showing the student the booking details... ")
        from controllers.StudentController import StudentController
        StudentController.showmybooking(book.get_user_id(v))
