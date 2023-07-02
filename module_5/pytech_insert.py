from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.v4jjizu.mongodb.net/pytech"

client = MongoClient(url)

db = client.pytech

#three student documents
#first student
somer = {
    "student_id": "1007",
    "first_name": "Somer",
    "last_name": "Smith",
    "enrollments": [
        {
            "term": "Fall Term",
            "grade": "3.8",
            "start_date": "September 2022",
            "end_date": "November 2022",
            "courses": [
                {
                    "course_id": "CY123",
                    "description": "Access Control Management",
                    "instructor": "Professor Yamada",
                    "grade": "A"
                },
                {
                    "course_id": "CY321",
                    "description": "Advanced Intrusion Detection and Response",
                    "instructor": "Professor Baku",
                    "grade": "A+"
                }
            ]
        }
    ]
}
#second student
autumn = {
    "student_id": "1007",
    "first_name": "Autumn",
    "last_name": "Jones",
    "enrollments": [
        {
            "term": "Winter Term",
            "grade": "3.6",
            "start_date": "December 2022",
            "end_date": "February 2023",
            "courses": [
                {
                    "course_id": "CY789",
                    "description": "Network Security",
                    "instructor": "Professor Rhoades",
                    "grade": "A+"
                },
                {
                    "course_id": "CY987",
                    "description": "Operational Security",
                    "instructor": "Professor Axelrod",
                    "grade": "A"
                }
            ]
        }
    ]
}
#third student
winter = {
    "student_id": "1007",
    "first_name": "Winter",
    "last_name": "Mendoza",
    "enrollments": [
        {
            "term": "Spring Term",
            "grade": "3.4",
            "start_date": "February 2023",
            "end_date": "May 2023",
            "courses": [
                {
                    "course_id": "CY456",
                    "description": "Assessments and Audits",
                    "instructor": "Professor Xavier",
                    "grade": "A"
                },
                {
                    "course_id": "CY654",
                    "description": "Penetration Testing",
                    "instructor": "Professor Grey",
                    "grade": "A-"
                }
            ]
        }
    ]
}

students = db.students

#insert student documents
somer_student_id = students.insert_one(somer).inserted_id
print("Inserted student record Somer Smith into students collection with document ID" + str(somer_student_id))

autumn_student_id = students.insert_one(autumn).inserted_id
print("Inserted student record Autumn Jones into students collection with document ID" + str(autumn_student_id))

winter_student_id = students.insert_one(winter).inserted_id
print("Inserted student record Winter Mendoza into students collection with document ID" + str(winter_student_id))

