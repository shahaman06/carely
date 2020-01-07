import argparse

miscellaneous = "Miscellaneous Python file to use execute commands :- New Registation of Carely User\
                ,Booking Appointments, and View Records. "
parser = argparse.ArgumentParser(description=miscellaneous)
parser.add_argument("-i","--id",action="store",help = "Input of User Id for further function use")
# Here constant is stored in case no argument is passed
parser.add_argument("-v","--view",const=True,nargs="?",help="to view records of Booking, Caretaker,Elderly,etc.")
parser.add_argument("-b","--booking",help="To Book Appointment")
parser.add_argument("-r","--registration",help="To register new Carely User.")

args = parser.parse()