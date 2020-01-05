#Address to be to a new class

from dateutil import parser
from phonenumbers import parse as num_val
# import create_id from util.py 

class BaseInfo{
    """
        [summary] Class defined to contain Basic Information about any person on portal
    """
    
    def __init__(self, *args, **kwargs):
    
        id = ""
        fname = ""
        lname = ""
        mname = ""
        #map_loc = ""
        dob = ""
        mob_no = ""
        bg = ""
        photo_path = ""
        address = ""
    
    def fill_info(cat):
        fname = input("Enter First Name: ")
        while not fname.isalpha():
            fname = input("Re-Enter First Name: ")
        lname = input("Enter Last Name: ")
        while not lname.isalpha():
            lname = input("Re-Enter First Name: ")
        mname = input("Enter Middle Name: ")
        while not mname.isalpha():
            mname = input("Re-Enter Middle Name: ")
        # input of map coordinate by selecting map location
        dob = parser.parse(input("Enter Date of Birth"))
        mob_no = num_val(input("Enter Mobile Number:  "))
        while not mob_no:
            mob_no = num_val(input("Re-Enter Mobile Number:  "))
        address = input("Enter Address: \n")
        bg = input("Enter Blood Group: ")  #NOT VALIDATED
        photo_path = input("Input Photo Path(present in /caretaker directory ith extension): ")
        id = create_id(cat)
        #This is a temporary solution to photo gain, also NOT VALIDATED
        
    def retrieve_info():
        
        if id:
            # return personal information
        
}