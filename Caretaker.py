from BaseInfo import BaseInfo
from ReviewInfo import ReviewInfo
import mysql.connector

class Caretaker:

    def __init__(self):

        bi = BaseInfo()
        review = ReviewInfo()
        strikes = 0
        specialty = ""

def Registration():
    entry = Caretaker()
    print("Enter Information of Caretaker :- \n\n")
    val = entry.bi.fill_info("ct")
    specialty = input("Enter Specialty of Caretaker: ")
    val += (strikes,specialty)
    conn = mysql.connector.connect(host="localhost",user="carely_admin",passwd="carely_admin",database="carelydb")
    sql = "INSERT INTO CARETAKER VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s)"
    cur = conn.cursor()
    cur.execute(sql,val)
    conn.commit()
    sql = "INSERT INTO VERIFICATIONPROOF (carely_id) VALUES (%s)"
    cur.execute(sql,(val[0],))
    conn.commit()