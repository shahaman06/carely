import argparse
from Caretaker import Registration as creg
from Elderly import Registration as ereg

parser = argparse.ArgumentParser(description = "New Registration of user (Caretaker/Elderly)")
parser.add_argument('-c','--caretaker',default=1,action ="store_true", help='Selection of Caretaker')
parser.add_argument('-e','--elderly',default=2,action ="store_true", help='Selection of Elderly')

args = parser.parse_args()

if type(args.caretaker) == type(True):
    print("\n***************New Carely Caretaker Registration***************\n")
    creg()
    print("\n*********************Registration is Done*********************\n")
if type(args.elderly) == type(True):
    print("\n***************New Carely Elderl Registration***************\n")
    ereg()
    print("\n*********************Registration is Done*********************\n")
else:
    print("No Arguments passed here")

    print("***************Registration is Done***************")