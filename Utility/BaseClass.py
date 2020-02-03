# Address to be to a new class
from Utility import validate_date, validate_phone_number


class BaseInfo:
    """
        [summary] Class defined to contain Basic Information about any person on portal
    """

    def __init__(self):

        self.id = ""
        self.fname = ""
        self.lname = ""
        self.mname = ""
        # map_loc = ""
        self.dob = ""
        self.mobno = ""
        self.bg = ""
        self.picpath = ""
        self.address = ""
        self.flagged = "False"
        self.verified = "False"
        self.reviewed = (
            "False"  # create a function which inserts record, and manipulates tables
        )

    def fill_info(self, cat):

        self.id = create_id(cat)
        self.fname = input("Enter First Name: ")
        while not self.fname.isalpha():
            self.fname = input("Re-Enter First Name: ")
        self.lname = input("Enter Last Name: ")
        while not self.lname.isalpha():
            self.lname = input("Re-Enter First Name: ")
        self.mname = input("Enter Middle Name: ")
        # input of map coordinate by selecting map location
        self.dob = validate_date(input("Enter Date of Birth: "))
        self.mob_no = validate_phone_number()
        self.address = input("Enter Address(max 100 character): \n")
        self.bg = input("Enter Blood Group: ")  # NOT VALIDATED
        # Picture not Validated,This is a temporary solution to photo gain, also NOT VALIDATED
        self.photo_path = input(
            "Input Photo Path(present in Data/images/"
            + cat
            + "/ directory ith extension): "
        )
        return (
            self.id,
            self.fname,
            self.lname,
            self.mname,
            self.mob_no,
            self.dob,
            self.address,
            self.bg,
            self.photo_path,
            "False",
            self.flagged,
            self.verified,
        )


class Caretaker:
    def __init__(self):

        self.bi = BaseInfo()
        self.strikes = 0
        self.speciality = ""


class Elderly:
    def __init__(self):

        self.bi = BaseInfo()
        self.strikes = 0  # less than 5 strikes
        self.health_condition = ""
        self.delayflag = "True"  # This indicates whether certain time delay is allowed
        self.no_of_caretaker = 0
        self.special_remarks = ""

    # def change_CT(self,status):


class PendingBooking:
    def __init__(self):
        self.per_id = ""
        self.req_id = ""
        self.reg_date = ""
        self.reg_time = ""
        self.no_of_hours = 0
        self.confirmation = "Pending"  # ACCEPTED REJECTED PENDING

    def fill_info():
        self.reg_date = input("Enter Date of Appointment: ")
        self.reg_time = input("Enter Time of Appointment ( 24 hour format HH:MM): ")
        self.no_of_hours = input("For how many hours, can you attend: ")
        return (self.reg_date, self.reg_time, self.no_of_hours, self.confirmation)


class ReviewInfo:
    def __init__(self):
        self.review = ""
        self.rating = 0
        self.null_flag = False
        self.name = ""


class VerificationProof:
    def __init__(self):

        self.ver_flag = False
        self.id_type = ""
        self.id_no = ""
        self.id_path = ""
        self.carely_id = ""
        self.under_ver = "False"

    # def get_verified(cat, info):
    # show id proof and details of person and check if verified or not

    def update_details(self):  # (,image):
        print("\nVerification ID Details :- \n")
        self.id_type = input("Enter ID Type: ")
        self.id_no = input("Enter ID Number: ")
        self.id_path = input("Enter ID file path(images/vp/): ")
        self.under_ver = "True"
        return (self.ver_flag, self.under_ver, self.id_type, self.id_no, self.id_path)
