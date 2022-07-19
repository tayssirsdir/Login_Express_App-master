import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='variables',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='variables',
                                         user='root',
                                         password='')

 
    mySql_Create_Table_Query = """CREATE TABLE Samevar( 
                             Id int AUTO_INCREMENT,
                             Name varchar(250) NOT NULL,
                             Val varchar(250) NOT NULL,
                             PRIMARY KEY (Id)) """
                             
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")
    

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='variables',
                                         user='root',
                                         password='')

 
    mySql_Create_Table_Query = """CREATE TABLE DifferentVar( 
                             Id int AUTO_INCREMENT,
                             Name varchar(250) NOT NULL,
                             Val varchar(250) NOT NULL,
                             PRIMARY KEY (Id)) """
                             
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")
    

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))    


  # Open File in Read Mode
file_1 = open('inifile1.ini', 'rb')
file_2 = open('inifile2.ini', 'rb')


  
file_1_line = file_1.readline()
file_2_line = file_2.readline()
# Use as a COunter
line_no = 1
  
print()
print("comm line ")
i=0
dic = {}
list_same = []
list_different = []


with open('inifile1.ini') as file1:
    with open('inifile2.ini') as file2:
        same = set(file1).intersection(file2)
        diff = set(file1).difference(file2)
       
        badword='#,['
        list_same = []
        sql_insertion = "INSERT INTO Samevar (name,val) VALUES (%s,%s)"
        for line in same:
            a_strings = line
            partitioned_strings = a_strings.rpartition('=')
            a_string =line
            partitioned_string = a_string.partition('=')
            before_first_period = partitioned_string[0]
            before_last_period = partitioned_strings[2]
            if not any(badword in line for badword in badword):
               #list_same.append(line)
               #print(before_first_period)
               #print(before_last_period)
               value = (before_first_period , before_last_period )
               cursor.execute(sql_insertion , value)
               #print(partitioned_strings)

connection.commit()

print("customer records inserted!")

            
            
             
with open('inifile1.ini') as file1:
    with open('inifile2.ini') as file2:
        diff = set(file1).difference(file2)
        
        badword='#,['
        list_different = []
        sql_insertion1 = "INSERT INTO DifferentVar (name,val) VALUES (%s,%s)"
        for line in diff:
            a_strings = line
            partitioned_strings = a_strings.rpartition('=')
            a_string =line
            partitioned_string = a_string.partition('=')
            before_first_period = partitioned_string[0]
            before_last_period = partitioned_strings[2]
            if not any(badword in line for badword in badword):
               #list_different.append(line)
               print(before_first_period)
               #print(before_last_period)
               value1 = (before_first_period , before_last_period )
               cursor.execute(sql_insertion1 , value1)


              
       
        
data = {
    'same' : list_same,
    'diff' : list_different
}
#print('data : ', data)