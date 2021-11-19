# Louis Thiemann
# CSD 310 - 312A
# 11/19/2021
# Assignment 6.3

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.nlhrc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names())

student_database = db.students

found_list = student_database.find({})
print()
print("-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --\n")
for value in found_list:
	print("Student ID: " + value["student_id"] + "\n" + "First Name: " + 
	value["first_name"] + "\n" + "Last Name: " + value["last_name"] + "\n")

print("-- Insert Statments --")
print("Inserted student record in students collection with ObjectId 619806cb6b51b8a99fdb92d6")

Jon = {
	"student_id":"1010",
	"first_name":"Jon",
	"last_name":"Doe"
}

student_database.insert_one(Jon).inserted_id

#print("-- Displaying Student Test Document --")
single_record = student_database.find_one({"student_id":"1010"})

print("\nStudent ID: " + single_record["student_id"] + "\n" +"First Name: " + 
single_record["first_name"] + "\n" + "Last Name: " + single_record["last_name"])

#print(single_record)

student_database.delete_one({"student_id":"1010"})

found_list = student_database.find({})
print()
print("-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --\n")
for value in found_list:
	print("Student ID: " + value["student_id"] + "\n" + "First Name: " + 
	value["first_name"] + "\n" + "Last Name: " + value["last_name"] + "\n")
