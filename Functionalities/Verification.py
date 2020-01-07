#verification of user using proper identification --> This has to updated by checking real info and not laid back method
import mysql.connector
import os
import time
from Utility.VerificationProof import VerificationProof

print("\n**************Welcome to Carely User Verification**************\n")
user_id = input("Enter Carely Id of Pre-Registered to be verified: ")
if user_id[:2] == "ct":
    db = "Caretaker"
elif user_id[:2] == "el":
    db = "Elderly"
else:
    print("Wrong Id. Try Again")
    time.sleep(3)
    os.system("python Verification.py")
    exit()
conn = mysql.connector.connect(host="localhost",user="carely_admin",passwd="carely_admin",database = "carelydb")
cur = conn.cursor()
sqlcmd = "select * from "+db+" where id = '"+user_id+"'"
cur.execute(sqlcmd) 
res = cur.fetchall()
if res == []:
    print("No such user id found")
    print("Kindly Exiting")
    time.sleep(3)
    exit()
sqlcmd = "select * from VerificationProof where carely_id = '"+user_id+"'"
cur.execute(sqlcmd) 
res = cur.fetchall()
if len(res) > 1:
    print("Multiple Records of Same Identity Found,Delete Records and try again")
    print("Suggestion : Use delete_record.py to do perform that")
    print("Kindly Exiting")
    time.sleep(3)
    exit()
else:
    if res[0][1] == "True":
        print("Carely User is Already Verified")
    else:
        if res[0][2] == "True":
            sqlcmd = "update table VerificationProof set under_ver ='False',ver_flag='True' where carely_id = '"+user_id+"'"
            cur.execute(sqlcmd)
            conn.commit()
            sqlcmd = "update table "+db+" set verified='True' where id = '"+user_id+"'"
            conn.commit()
            print("\nCarely User is Verified now")
        else:
            verify = VerificationProof()
            val = (user_id,)+verify.update_details()
            sqlcmd = "delete from VerificationProof where carely_id = '"+user_id+"'"
            cur.execute(sqlcmd)
            sqlcmd = "insert into VerificationProof values (%s,%s,%s,%s,%s,%s)"
            cur.execute(sqlcmd,val)
            conn.commit()
            print("\nApplication generated, currently under verification.")
print("Kindly Exiting")
time.sleep(3)
exit()