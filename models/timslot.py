from repo.Apprepo import AppRepo
class TimeSlot:
    def __init__(self,ts_id,ts_t):
        self.ts_id=ts_id
        self.ts_t=ts_t
        AppRepo.timeslot[ts_id]=self

