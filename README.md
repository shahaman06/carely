Required Dependencies :- 

mysql-connector-python
pandas
dateutil
phonenumbers

Configure Database :- 

If you are ubuntu user, use intital_setup.py . It will automatically configure system for project use.

If any other system is used, then follow this steps:-
    1. open cmd with admin rights
    2. run the command : pip3 install mysql-connector-python pandas dateutil phonenumbers pandas\
    3. run the commmand : sudo mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'carely_admin'@'localhost' IDENTIFIED BY 'carely_admin';"
    4. run the command : sudo mysql -u carely_admin -p < skeleton.sql

database_user : carely_admin
database_password : carely_admin