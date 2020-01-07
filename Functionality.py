#to view records of file
import argparse
import time
from Utility.util import print_records
parser = argparse.ArgumentParser(description="Multi Function Python FIle to view ,update and verify")
parser.add_argument("-i","--id",action="store",help = "Input of User Id for further function use")
# Here constant is stored in case no argument is passed
parser.add_argument("-v","--view",const=True,nargs="?",help="to view records of Booking, Caretaker,Elderly,etc.")
parser.add_argument("-u","--update",help="To Update Caretaker/Elderly Records. Works only if -i/--id is present")
parser.add_argument("-p","--verify",help="To Verify Carely User.")

args = parser.parse_args()

if args.id == None:
    if args.view == None:
        print("No Relevant Arguments are passed.")
        print("Please Try Again Later.")
        time.sleep(3)
        exit()
    else:
        print_records("Caretaker")
        print_records("Elderly")
        print_records("BookingRecord")
        print_records("PendingBooking")
        print_records("VerificationProof")
        print_records("ReviewInfo")
        
else:
    if arg.id[:2] not in ["ct","el"]:
        print("Invalid Carely ID is passed.")
        print("Please Try Again Later.")
        time.sleep(3)
        exit()
    else:
        if arg.id[:2] =="ct":
            print_records("Caretaker",uid,"id")
        else:
            print_records("Elderly",uid,"id")
        print_records("BookingRecord",uid,"per_id")
        print_records("PendingBooking",uid,"per_id")
        print_records("VerificationProof",uid,"carely_id")
        print_records("ReviewInfo",uid,"id")
print("Thanks for Using")
time.sleep(3)
exit()