import argparse

desc = "Main Python file to use execute commands :- New Registation of Carely User\
                ,Booking Appointments, and View Records. "
parser = argparse.ArgumentParser(description=desc)
parser.add_argument("-i","--id",action="store",help = "Input of User Id for further function use")
# Here constant is stored in case no argument is passed
parser.add_argument("-r","--registration",action="store_true",help="To register new Carely User.")
parser.add_argument("-b","--booking",action="store_true"help="To Book Appointment")
parser.add_argument("-v","--view",const=True,nargs="?",help="to view records of Booking, Caretaker,Elderly,etc.")
arg = parser.parse()

if arg.registration:
    os.system("python Main/Registration.py")
elif not arg.view:
    os.system("python Main/View.py --view --id '"+arg.id+"'")
elif arg.booking:
    os.system("python Main/Booking.py")