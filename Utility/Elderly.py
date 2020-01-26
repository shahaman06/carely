from .BaseInfo import BaseInfo
import mysql.connector

# format the sequence of variables
class Elderly:
    def __init__(self):

        self.bi = BaseInfo()
        self.strikes = 0  # less than 5 strikes
        self.health_condition = ""
        self.delayflag = "True"  # This indicates whether certain time delay is allowed
        self.no_of_caretaker = 0
        self.special_remarks = ""

    # def change_CT(self,status):
    #


def Registration():
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
