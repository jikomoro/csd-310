from pymongo import MongoClient

#MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.v4jjizu.mongodb.net/pytech"

#connects to MongoDB cluster
client = MongoClient(url)

#connects to the pytech database
db = client.pytech

#connects to the students collection
students = db.students

#retrieves student data from collection
student_list = students.find({})

#find method and output
for doc in student_list:
    print("Student ID:" + doc["student_id"] + "\n First name:" + doc["first_name"] + "\n Last name:" + doc["last_name"])

#updates student 1007 info
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": Gomez}})

#retrieves student 1007's updated doc
somer = students.find_one({"student_id": "1007"})

print("\n -- DISPLAYING STUDENT DOCUMENT FROM find() QUERY --")

#displays updated doc
print("Student ID:" + somer["student_id"] + "\n First name:" + somer["first_name"] + "\n Last name:" + somer["last_name"])

#end message
input("\n End of program, press any key to continue...")
