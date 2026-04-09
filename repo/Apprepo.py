from collections import defaultdict
class AppRepo:
    equipment={}
    student={}
    labCoordinator={}
    lab={}
    timeslot={}
    booking={}
    grantaccess=defaultdict(int)
    userslot=set()