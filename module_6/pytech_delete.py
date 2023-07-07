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

print("\n -- DISPLAYING STUDENT DOCUMENT FROM find() QUERY --")

#loops collection and displays output
for doc in student_list:
    print("Student ID:" + doc["student_id"] + "\n First name:" + doc["first_name"] + "\n Last name:" + doc["last_name"])

#test doc
test_doc = {
    "student_id": "1010",
    "first_name": "Timothy",
    "last_name": "Garcia"
}

#inserts test doc into MongoDB
test_doc_id = students.insert_one(test_doc).inserted_id

#message
print("\n -- INSERT STATEMENTS --")
print("Inserted student record into the students collection with document_id" + str(test_doc_id))

#find method
student_test_doc = students.find_one({"student_id": "1010"})

#results
print("\n -- DISPLAYING STUDENT TEST DOC --")
print("Inserted student record into the students collection with document_id " + str(test_doc_id))

#delete one method to delete student_test_doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

#find method for all students in the collection
new_student_list = students.find({})

#message
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#loops collection and displays output
for doc in new_student_list:
    print("Student ID:" + doc["student_id"] + "\n First name:" + doc["first_name"] + "\n Last name:" + doc["last_name"])

#end message
input("\n End of program, press any key to continue...")
