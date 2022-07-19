#import paramiko 
import pymongo
from pymongo import MongoClient
connection_string = "mongodb://localhost:27017/FeedHumain"

client = MongoClient(connection_string)

mydb=client.get_database("FeedHumain")
mycollection=mydb.get_collection("addservers")
#print(mycollection)

username = input('enter usename')
myResult = mycollection.find({"username": input('enter usename')})

for each_doc in myResult:
   
    if each_doc.username==username:
          print(each_doc)

#one_record=mycollection.find({},{"username":1,"_id":0})


#command = "df"

# Update the next three lines with your
# server's information

#host = "YOUR_IP_ADDRESS"
#username = "YOUR_LIMITED_USER_ACCOUNT"
#password = "YOUR_PASSWORD"

#client = paramiko.client.SSHClient()
#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.connect(host, username=username, password=password)
#_stdin, _stdout,_stderr = client.exec_command("df")
#print(stdout.read().decode())
#client.close()



 