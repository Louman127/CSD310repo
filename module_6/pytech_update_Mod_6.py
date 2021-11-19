from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.nlhrc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names())

student_database = db.students

found_list = student_database.find({})

print("\nDisplaying List:\n")
for value in found_list:
	print("Student ID Number: " + value["student_id"] + "\nFirst Name: " + value["first_name"] + "\n" + 
	"Last Name: " + value["last_name"] + "\n")
	


result_updated = student_database.update_one({"student_id":"1007"},{"$set": {"last_name":"Smith"}})

single_record = student_database.find_one({"student_id":"1007"})

print("Displaying One Record:\n")
print("Student ID Number: " + single_record["student_id"] + "\nFirst Name: " + single_record["first_name"] + "\nLast Name: " +
single_record["last_name"])
