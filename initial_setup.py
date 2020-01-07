import os
from argparse import ArgumentParser as ap
def install_db_dep():
    """
        Install Dependencies and Setup Database
    """
    cmd = "GRANT ALL PRIVILEGES ON *.* TO 'carely_admin'@'localhost' IDENTIFIED BY 'carely_admin';"
    os.system("echo 'Installing Dependencies'")
    os.system("pip3 install mysql-connector-python python-dateutil phonenumbers")
    os.system('sudo mysql -u root -e "'+cmd+'"')
    os.system('sudo mysql -u root -p < Data/Query/skeleton.sql')

def load_data():
    #to load data from .csv to database using certain format
    #used command to export data out of mysql : sudo mysql -u root -e "use carelydb;select* from Caretaker;" | sed 's/\t/,/g' > Data/Sample_CSV/Caretaker.csv
    os.system('sudo mysql -u root -p < Data/Query/load_cs_db.sql')

def main():
    parser = ap(help="To install dependencies, setting up database and load data into it. ")
    #parser.add("-i","--install",action="store_true",help = "Installing Dependencies and Setting Up Database")
    parser.add("-l","--load",action="store_true",help = "Load Data from csv file to database (File Should be present in Data/CSV_Database Directory). Note: Only Sample Format to be used for structure and file name. For Sample Format of csv file Check Data/Sample_CSV Folder" )
    arg = parser.parse()
    install_db_dep()
    if arg.load:
        load_data()

if __name__ == "__main__":
    main()