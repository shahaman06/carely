from datetime import datetime
import mysql.connection
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

#create function to add implement customized query for different function using arguments
#create function to print records