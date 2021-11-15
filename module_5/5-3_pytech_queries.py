from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.nlhrc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names())

students = db.students
student_list = students.find({})

for value in student_list:
	print(value)

student_list = students.find_one({"student_id": "1007"})
print(student_list["student_id"])

student_list = students.find_one({"student_id": "1008"})
print(student_list["student_id"])

student_list = students.find_one({"student_id": "1009"})
print(student_list["student_id"])
