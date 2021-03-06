from datetime import datetime
from dateutil import parser
from phonenumbers import parse as num_val
from BaseClass import Caretaker, Elderly
import mysql.connector
import time
import os
from os import system as cli
import sys

# agecalc for calculating age
def chgdir():
    #Use it to change direcory to Carely/
    path_list = os.getcwd().split()
    path = "/".join(path_list[:path_list.index("Carely")+1])
    path = os.getcwd()
    os.chdir(path)
    sys.path.append(path)


def create_id(cat):
    now = datetime.now()
    id = cat + now.strftime("%m%H%y%M%d%S")
    return id


def validate_phone_number():
    num = num_val(input("Enter Mobile Number: "))
    while not num:
        num = num_val(input("Re-Enter Mobile Number:  "))
    return "+" + str(num.country_code) + " " + str(num.national_number)


def print_records(db, id_name, uid=False):
    conn = mysql.connector.connect(
        host="localhost",
        user="carely_admin",
        passwd="carely_admin",
        database="carelydb",
    )
    cur = conn.cursor()
    if not (db == "ReviewInfo"):
        if not uid:
            cur.execute("Select * from " + db)
        else:
            cur.execute(
                "Select * from " + db + " where " + id_name + " = '" + uid + "'"
            )
    else:
        sub_query = (
            "create table temp (select id ,CONCAT(fname,"
            ",lname) as name from Caretaker UNION select id ,CONCAT(fname,"
            ",lname) from Elderly)"
        )
        cur.execute(sub_query)
        if not uid:
            cur.execute(
                "select "
                + db
                + ".id,temp.name,"
                + db
                + ".review,"
                + db
                + ".rating from "
                + db
                + " inner join temp on temp.id = "
                + db
                + ".id"
            )
        else:
            cur.execute(
                "select "
                + db
                + ".id,temp.name,"
                + db
                + ".review,"
                + db
                + ".rating from "
                + db
                + " inner join temp on temp.id = "
                + db
                + ".id where "
                + db
                + "."
                + id_name
                + " = '"
                + uid
                + "'"
            )
    res = cur.fetch_all()
    print("\n***************" + db + " Data***************\n")
    for x in res:
        print(x)


def verify_user(uid, db, id_name):
    conn = mysql.connector.connect(
        host="localhost",
        user="carely_admin",
        passwd="carely_admin",
        database="carelydb",
    )
    cur = conn.cursor()
    cur.execute("Select * from " + db + " where " + id_name + " = '" + uid + "'")
    res = cur.fetch_all()
    return not res == []


def invalid_user():
    print("\nInvalid Carely ID is passed.")
    print("Please Try Again Later.")
    time.sleep(3)


def validate_date(inp):
    return parser.parse(inp).strftime("%x")


def invalid_arg():
    print("No Relevant Arguments are passed.")
    print("Please Try Again Later.")
    time.sleep(3)


def Register_Elderly():
    entry = Elderly()
    print("Enter Information of Elderly :- \n")
    val = entry.bi.fill_info("el")
    entry.health_condition = input("Enter Specific Health Condition: ")
    # delayflag is problematic as it uses string for boolean value
    entry.delayflag = input("Is Elderly okay with 30 minute delay(True/False): ")
    entry.special_remarks = input("Enter Special Remarks for Caretaker: ")
    val += (
        entry.health_condition,
        entry.strikes,
        entry.no_of_caretaker,
        entry.special_remarks,
        entry.delayflag,
    )
    conn = mysql.connector.connect(
        host="localhost",
        user="carely_admin",
        passwd="carely_admin",
        database="carelydb",
    )
    sqlcmd = "INSERT INTO Elderly VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(sqlcmd, val)
    conn.commit()
    sqlcmd = "INSERT INTO VerificationProof (carely_id) VALUES (%s)"
    cur.execute(sqlcmd, (val[0],))
    conn.commit()


def Register_Caretaker():
    entry = Caretaker()
    print("Enter Information of Caretaker :- \n")
    val = entry.bi.fill_info("ct")
    entry.specialty = input("Enter Speciality of Caretaker: ")
    val += (entry.strikes, entry.specialty)
    print(val)
    conn = mysql.connector.connect(
        host="localhost",
        user="carely_admin",
        passwd="carely_admin",
        database="carelydb",
    )
    # Here Table names are case sensitive
    sqlcmd = "INSERT INTO Caretaker VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(sqlcmd, val)
    conn.commit()
    sqlcmd = "INSERT INTO VerificationProof (carely_id) VALUES (%s)"
    cur.execute(sqlcmd, (val[0],))
    conn.commit()
