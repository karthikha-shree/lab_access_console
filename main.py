from models.lab import Lab
from models.equipment import Equipment
from models.timslot import TimeSlot
from models.labcoordination import LabCoordinator
from models.student import student
from repo.Apprepo import AppRepo
from controllers.StudentController import StudentController
def main():
    scontroler=StudentController()

    s1=student(1,"ab",8.5,"student")
    s2=student(2,"cd",9.5,"student")
    s3=student(3,"ef",7.5,"student")

    c1=LabCoordinator(4,'aicor01','l1','AI Lab',"Coordinator")
    c2=LabCoordinator(5,'clkcor01','l2','Cloud Lab',"Coordinator")
    c3=LabCoordinator(6,'nwcor01','l3','Network Lab',"Coordinator")

    tm1=TimeSlot(1,'9-10')
    tm2=TimeSlot(2,'10-11')
    tm3=TimeSlot(3,'11-12') 
    tm4=TimeSlot(4,'1-2')  
    tm5=TimeSlot(5,'2-3') 
    tm6=TimeSlot(6,'3-4') 
    
    eq1=Equipment("l1",'e1','SYS1',2)
    eq2=Equipment("l1",'e2','SYS2',2)
    eq3=Equipment("l1",'e3','SYS3',2)

    eq4=Equipment("l2","e4",'sys4',2)
    eq5=Equipment("l2","e5",'sys5',2)
    eq6=Equipment("l2","e6",'sys6',2)

    eq7=Equipment("l3","e7",'sys7',2)
    eq8=Equipment("l3","e8",'sys8',2)
    eq9=Equipment("l3","e9",'sys9',2)

    nwep={        eq7,eq8,eq9    }
    aieq={        eq1,eq2,eq3    }
    cleq={        eq4,eq5,eq6    }


    l1=Lab('l1','AI Lab',aieq)
    l2=Lab('l2','Cloud Lab',cleq)
    l3=Lab('l3','Network Lab',nwep)

    print("_____________  LAB ACCESS MANAGEMENT SYATEM   _______________")
    print("1. Student Login ")
    print("2. Coordinator login")
    print("3. Exit")
    choice=int(input("Enter you choice : "))
    if choice==1:
        if(not scontroler.login()):
            exit()
        else:
            scontroler.start()
    else:
            print("Invalid input ")

if __name__=="__main__":
    main()