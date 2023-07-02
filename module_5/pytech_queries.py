from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.v4jjizu.mongodb.net/pytech"

client = MongoClient(url)

db = client.pytech

students = db.students

#find students in collection
student_list = students.find({})

for doc in student_list:
    print("Student ID:" + doc["student_id"] + "\n First name:" + doc["first_name"] + "\n Last name:" + doc["last_name"] + "\n")

#find with student_id
somer = students.find_one({"student_id": "1007"})

#output results
print("Student ID:" + somer["student_id"] + "\n First name:" + somer["first_name"] + "\n Last name:" + somer["last_name"] + "\n")

#end message
input("\n End of program, press any key to continue...")
