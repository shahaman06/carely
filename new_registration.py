import argparse
from Caretaker import Registration as creg
from Elderly import Registration as ereg

parser = argparse.ArgumentParser(description = "New Registration of user (Caretaker/Elderly)")
parser.add_argument('-c','--caretaker',default=1,action ="store_true", help='Selection of Caretaker')
parser.add_argument('-e','--elderly',default=2,action ="store_true", help='Selection of Elderly')

args = parser.parse_args()

if type(args.caretaker) == type(True):
    creg()
if type(args.elderly) == type(True):
    ereg()
else:
    print("No Arguments passed here")