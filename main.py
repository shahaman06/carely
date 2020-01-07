from argparse import ArgumentParser as ap

desc = "Main Python file to use execute commands :- New Registation of Carely User\
                ,Booking Appointments, and View Records. "
parser = ap(description=desc)
parser.add_argument("-i","--id",action="store",help = "Input of User Id for further function use")
# Here constant is stored in case no argument is passed
parser.add_argument("-r","--registration",action="store_true",help="To register new Carely User.")
parser.add_argument("-b","--booking",action="store_true"help="To Book Appointment")
parser.add_argument("-v","--view",const=True,nargs="?",help="to view records of Booking, Caretaker,Elderly,etc.")
arg = parser.parse()

if arg.registration:
    cli("python Main/Registration.py")
elif not arg.view:
    cli("python Main/View.py --view --id '"+arg.id+"'")
elif arg.booking:
    cli("python Main/Booking.py")