from VerificationProof import VerificationProof
from BaseInfo import BaseInfo
from ReviewInfo import ReviewInfo

# format the sequence of variables
class Elderly{
    
    def __init__(self):
    
        bi = BaseInfo()
        review = ReviewInfo() #
        strikes = 0 # less than 5 strikes
        health_condition = ""
        delayflag = "True" #This indicates whether certain time delay is allowed
        no_of_caretaker = 0
        special_remarks = ""
    
    def change_CT(self,status):
        #
}
def Registration():
    entry = Caretaker()
    print("Enter Information of Elderly :- \n\n")
    val = entry.bi.fill_info("el")
    health_condition = input("Enter specific Health Condition: ")
    #delayflag is problematic as it uses string for boolean value
    delayflag = input("Is Elderly okay with 30 minute delay(True/False): ")
    special_remarks = input("Enter Special Remarks of Caretaker: ")
    val += (health_condition,strikes,no_of_caretaker,special_remarks,delayflag)
    conn = mysql.connector.connect(host="localhost",user="carely_admin",passwd="carely_admin",database="carelydb")
    sql = "INSERT INTO CARETAKER VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%d,%s,%s)"
    cur = conn.cursor()
    cur.execute(sql,val)
    conn.commit()
    sql = "INSERT INTO VERIFICATIONPROOF (carely_id) VALUES (%s)"
    cur.execute(sql,(val[0],))
    conn.commit()