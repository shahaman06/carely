# Address to be to a new class
from Utility.util import validate_date, validate_phone_number


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
