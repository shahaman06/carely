from datetime import datetime
from phonenumbers import parse as num_val
# agecalc for calculating age
# phonenumbers validate moblie number

def create_id(cat):     
    """[summary] To create a id using certain format of date and time of registration
    
    Arguments:
        cat {[string]} -- Used to define category of id
    """
    now = datetime.now()
    id = cat + now.strftime("%m%H%y%M%d%S")

    return id

def validate_phone_number():
    num = num_val(input("Enter Mobile Number: "))
    while not num:
        num = num_val(input("Re-Enter Mobile Number:  "))
    return "+"+str(num.country_code)+" "+str(num.national_number)
#create function to add implement customized query for different function using arguments
#create function to print records