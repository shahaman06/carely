#Address to be to a new class
from util import create_id
from dateutil import parser
from phonenumbers import parse as num_val
# import create_id from util.py 

class BaseInfo:
    """
        [summary] Class defined to contain Basic Information about any person on portal
    """
    
    def __init__(self):
    
        self.id = ""
        self.fname = ""
        self.lname = ""
        self.mname = ""
        #map_loc = ""
        self.dob = ""
        self.mobno = ""
        self.bg = ""
        self.picpath = ""
        self.address = ""
        self.flagged = "False"
        self.verified = "False" # create a function which inserts record, and manipulates tables
    
    def fill_info(self,cat):
        
        fname = input("Enter First Name: ")
        while not fname.isalpha():
            fname = input("Re-Enter First Name: ")
        lname = input("Enter Last Name: ")
        while not lname.isalpha():
            lname = input("Re-Enter First Name: ")
        mname = input("Enter Middle Name: ")
        # input of map coordinate by selecting map location
        dob = parser.parse(input("Enter Date of Birth: "))
        mob_no = num_val(input("Enter Mobile Number: "))
        while not mob_no:
            mob_no = num_val(input("Re-Enter Mobile Number:  "))
        address = input("Enter Address(max 100 character): \n")
        bg = input("Enter Blood Group: ")  #NOT VALIDATED
        #Picture not Validated
        photo_path = input("Input Photo Path(present in images/caretaker/ directory ith extension): ")
        id = create_id(cat)
        #This is a temporary solution to photo gain, also NOT VALIDATED
        return (id,fname,lname,mname,mob_no,dob,address,bg,photo_path,"False",flagged)
        
        #This might turn irrelevant
    #def retrieve_info():

        #if id:
            #return personal information
