from datetime import datetime
from phonenumbers import parse as num_val
import sql.connector
import time
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

def print_records(db,uid = False,id_name):
    conn = mysql.connector.connect(host="localhost",user="carely_admin",passwd="carely_admin",database="carelydb")
    cur = conn.cursor()
    if not (db == "ReviewInfo"):
        if not uid: 
            cur.execute("Select * from "+db)
        else:
            cur.execute("Select * from "+db+" where "+id_name+" = '"+uid+"'")
    else:
        sub_query = "create table temp (select id ,CONCAT(fname," ",lname) as name from Caretaker UNION select id ,CONCAT(fname," ",lname) from Elderly)"
        cur.execute(sub_query)
        if not uid:
            cur.execute("select "+db+".id,temp.name,"+db+".review,"+db+".rating from "+db+" inner join temp on temp.id = "+db+".id")
        else:
            cur.execute("select "+db+".id,temp.name,"+db+".review,"+db+".rating from "+db+" inner join temp on temp.id = "+db+".id where "+db+"."+id_name+" = '"+uid+"'")
    res = cur.fetch_all()
    print("\n***************"+db+" Data***************\n")
    for x in res:
        print(x)
def verify_user(uid,db,id_name):
    conn = mysql.connector.connect(host="localhost",user="carely_admin",passwd="carely_admin",database="carelydb")
    cur = conn.cursor()
    cur.execute("Select * from "+db+" where "+id_name+" = '"+uid+"'")
    res = cur.fetch_all()
    return not res == []
def invalid_user():
    print("\nInvalid Carely ID is passed.")
    print("Please Try Again Later.")
    time.sleep(3)
    exit()

#create function to add implement customized query for different function using arguments
#create function to print records