from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.nlhrc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names())

Thorin = {
    
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield",
     

    "enrollments": [
        {
            "term": "spring",
            "gpa": "3.9",
            "start": "01/01/2022",
            "end": "04/01/2022"
        },
        {
            "term": "summer",
            "gpa": "3.9",
            "start": "04/01/2022",
            "end": "07/01/2022"
        },
        {
            "term": "fall",
            "gpa": "3.9",
            "start": "07/01/2022",
            "end": "10/01/2022"					
        },
        {
            "term": "winter",
            "gpa": "3.9",
            "start": "10/01/2022",
            "end": "01/01/2022"		                
        }
    ],
    "courses": [
        {
            "course_id": "Tech123",
            "description": "Tech Support",
            "instructor": "Bob Smith",
            "grade": "Senior"
        },
        {
            "course_id": "Tech456",
            "description": "Tech Support",
            "instructor": "Bob Smith",
            "grade": "Senior"
        },
        {
            "course_id": "Tech789",
            "description": "Tech Support",
            "instructor": "Bob Smith",
            "grade": "Senior"
        },    
        {
            "course_id": "Tech10",
            "description": "Tech Support",
            "instructor": "Bob Smith",
            "grade": "Senior"
        }        
    ]
}

Bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins",
    
    "enrollments": [
        {
            "term": "spring",
            "gpa": "3.9",
            "start": "01/01/2022",
            "end": "04/01/2022"
        },
        {
            "term": "summer",
            "gpa": "3.9",
            "start": "04/01/2022",
            "end": "07/01/2022"
        }    
	],

    "courses": [
        {
            "course_id": "Tech123",
            "description": "Tech Support",
            "instructor": "Bob Smith",
            "grade": "Senior"
        },
        {
            "course_id": "Tech456",
            "description": "Tech Support",
            "instructor": "Bob Smith",
            "grade": "Senior"
        }
	]
}

Frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggons",
    
    "enrollments": [
        {
            "term": "spring",
            "gpa": "3.9",
            "start": "01/01/2022",
            "end": "04/01/2022"
        },
        {
            "term": "summer",
            "gpa": "3.9",
            "start": "04/01/2022",
            "end": "07/01/2022"
        }    
	],

    "courses": [
        {
            "course_id": "Tech123",
            "description": "Tech Support",
            "instructor": "Bob Smith",
            "grade": "Senior"
        },
        {
            "course_id": "Tech456",
            "description": "Tech Support",
            "instructor": "Bob Smith",
            "grade": "Senior"
        }
	]    
}

students = db.students
Thorin_student_id = students.insert_one(Thorin).inserted_id
print("  Inserted student record Thorin Oakenshield into the students collection with document_id " + str(Thorin_student_id))
student_list = students.find({})

students = db.students
Bilbo_student_id = students.insert_one(Bilbo).inserted_id
print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(Bilbo_student_id))
student_list = students.find({})

students = db.students
Frodo_student_id = students.insert_one(Frodo).inserted_id
print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(Frodo_student_id))
student_list = students.find({})
