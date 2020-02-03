from argparse import ArgumentParser as ap
import time
from Utility.util import print_records
import sys

parser = ap(description="Python FIle to view Records")
parser.add_argument(
    "-i", "--id", action="store", help="Input of User Id for further function use"
)
# Here constant is stored in case no argument is passed
parser.add_argument(
    "-v",
    "--view",
    const=True,
    nargs="?",
    help="to view records of Booking, Caretaker,Elderly,etc.",
)
args = parser.parse_args()
print("WORKING")
if args.id == None:
    if args.view == None:
        invalid_arg()
    else:
        print_records("Caretaker")
        print_records("Elderly")
        print_records("BookingRecord")
        print_records("PendingBooking")
        print_records("VerificationProof")
        print_records("ReviewInfo")

else:
    if arg.id[:2] not in ["ct", "el"]:
        print("Invalid Carely ID is passed.")
        print("Please Try Again Later.")
        time.sleep(3)

    else:
        if arg.id[:2] == "ct":
            print_records("Caretaker", "id", uid)
        else:
            print_records("Elderly", "id", uid)
        print_records("BookingRecord", "per_id", uid)
        print_records("PendingBooking", "per_id", uid)
        print_records("VerificationProof", "carely_id", uid)
        print_records("ReviewInfo", "id")
print("Thanks for Using")
time.sleep(3)
