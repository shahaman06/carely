from util import verify_user,invalid_user
from argparse import ArgumentParser as ap
from os import system as cli

miscellaneous = "Miscellaneous Python file to Update Carely user records and confirm Booking status and Verify Carely Users "
parser = ap(description=miscellaneous)
parser.add_argument("-u","--update",action="store_true",help="To Book Appointment")
parser.add_argument("-v","--verification",action="store_true",help="To register new Carely User.")
args = parser.parse()

uid = input("Enter a Valid Carely Id")
if uid[:2] not in ["el,ct"]:
    invalid_user()
db = "Caretaker" if uid[:2] else "Elderly"
if verify_user(uid,db,"id"):
    if arg.update:
        cli("python Miscellaneous/Update.py -i '"+uid+"'")
    if arg.verification:
        cli("python Miscellaneous/Verification.py -i '"+uid+"'")