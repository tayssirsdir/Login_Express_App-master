#import paramiko 
import pymongo 
client = pymongo.MongoClient('mongodb://localhost:27017/FeedHumain')

mydb=client["FeedHumain"]
mycollection=mydb["addserver"]
print(mycollection)

username='hello'
myResult = mycollection.find({})
print(myResult)
for item in myResult:
    if item == username:
        print(item)
#one_record=mycollection.find({},{"username":1,"_id":0})

#print(one_record)
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



 