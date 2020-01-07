class PendingBooking:
    
    def __init__(self):
        self.per_id = ""
        self.req_id = ""
        self.reg_date = ""
        self.reg_time = ""
        self.no_of_hours = 0
        self.confirmation = "Pending" #ACCEPTED REJECTED PENDING
    
    def fill_info():
        self.reg_date = input("Enter Date of Appointment: ")
        self.reg_time = input("Enter Time of Appointment ( 24 hour format HH:MM): ")
        self.no_of_hours = input("For how many hours, can you attend: ")
        return(self.reg_date,self.reg_time,self.no_of_hours,self.confirmation)