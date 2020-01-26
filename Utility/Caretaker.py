from .BaseInfo import BaseInfo
import mysql.connector


class Caretaker:
    def __init__(self):

        self.bi = BaseInfo()
        self.strikes = 0
        self.speciality = ""


def Registration():
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
