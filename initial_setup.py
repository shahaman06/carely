import os
def main():
    cmd = "GRANT ALL PRIVILEGES ON *.* TO 'carely_admin'@'localhost' IDENTIFIED BY 'carely_admin';"
    os.system("echo 'Installing Dependencies'")
    os.system("pip3 install mysql-connector-python pandas python-dateutil phonenumbers pandas")
    os.system('sudo mysql -u root -e "'+cmd+'"')
    os.system('sudo mysql -u carely_admin -p < skeleton.sql')

if __name__ == "__main__":
    main()

#to load data from .csv to database using certain format
#import pandas as pd
