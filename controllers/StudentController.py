from repo.Apprepo import AppRepo
from models.student import student
from models.equipment import Equipment
from models.lab import Lab
from models.bookslot import book
from controllers.LabcoorController import labController
class StudentController:
    def __init__(self):
        self.curent_user=None
        pass
    def login(self):
        reg=int(input("Enter your reg no :"))
        if reg not in AppRepo.student:
            print("CHECK YOUR REG NO : ")
            return False
        print("LOGIN SUCCESSFULL")
        self.curent_user=AppRepo.student[reg]
        print("welcome",student.get_name(self.curent_user))
        return True
    def start(self):
        print("1.Request lab access  ")
        for i,v in AppRepo.lab.items():
            print(f"labid:{i} | labname : {Lab.get_lab_name(v)}")
        k=input("Enter the lab you need access :")
        if k not in AppRepo.lab:
            print("No Such lab Exits")
            exit("Wrong data entered")
        else:
            m=labController.askpermission(self,student.get_reg_no(self.curent_user),k)
        if m:
            v=AppRepo.lab[k]
            print("Equipments of ",{Lab.get_lab_name(v)})
            for id,eq in AppRepo.equipment.items():
                if Equipment.get_lab_id(eq)==k:
                    print(f"Equipment id : {id} | Equipment Name : {Equipment.get_eq_name(eq)} ")
            equip=input("Enter the Equipment id you want to book:")
            if equip not in AppRepo.equipment:
                print("NO SUCH EQUIPMENT FOUND")
                exit( "Wrong data entered" )
            for i,t in AppRepo.timeslot.items():
                print(f"TimeSlot id : { i }  ==== Timeslot : {t.ts_t}")
            slot=int(input("Enter the id of  slot for using equipment : "))
            if slot not in AppRepo.timeslot:
                print("ENTER PROPER TIMESLOT ID")
                exit( "Wrong data entered" )
        k=book(student.get_reg_no(self.curent_user),equip,slot)
        self.curent_user=None
        l=labController.login(self)
        if l:
            print("LABCORDINATOR IS REVIEEW AND GRANTING THE SLOT REQUESTS")
            labController.grant_boking(self)
        else:
            print("you are not a coordinator")

            





        # print("2.Book Equipment Slot ")
        # print("3.See Booking Status")
        # print("4.Exit   ")
        # k=int(input("Enter your choice :"))
        # while True:
        #     if k==1:
        #         lab=input("Enter the lab id you need to access : ")
        #         labController.askpermission(student.get_reg_no(),lab)

                

            

