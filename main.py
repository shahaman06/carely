from argparse import ArgumentParser as ap
from os import system as cli
from Utility.Utility import chgdir

chgdir()
desc = "Main Python file to use execute commands :- New Registation of Carely User\
                ,Booking Appointments, and View Records. "
parser = ap(description=desc)
parser.add_argument(
    "-i", "--id", action="store_true", help="Input of User Id for further function use"
)
# Here constant is stored in case no argument is passed
parser.add_argument(
    "-r", "--registration", action="store_true", help="To register new Carely User."
)
parser.add_argument("-b", "--booking", action="store_true", help="To Book Appointment")
parser.add_argument(
    "-v",
    "--view",
    const=True,
    nargs="?",
    help="to view records of Booking, Caretaker,Elderly,etc.",
)
arg = parser.parse_args()
print(arg)
if arg.registration:
    cli("python Main/Registration.py")
elif arg.view:
    if arg.id == False:
        cond = ""
    else:
        cond = " --id '" + arg.id + "'"
    cli("python Main/View.py --view" + cond)
elif arg.booking:
    cli("python Main/Booking.py")
