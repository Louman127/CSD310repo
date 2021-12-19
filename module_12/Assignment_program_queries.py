# Louis Thiemann
# CSD 310 312A
# 12/14/2021
# Assignment 11.2

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "schoolsql",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

try:

    db = mysql.connector.connect(**config) # connect to the whatabook database    
    # output the connection status 
    print("Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\nPress any key to continue...\n")

except mysql.connector.Error as error:

    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username and/or password")

    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("The database does not exist")

    else:
        print(error)
y = 1
while y == 1:
	""" METHODS """

	def show_menu():
		cursor = db.cursor()
		cursor.execute("show tables;") # show tables of the whatabook database
		menu = cursor.fetchall()	
		print("MENU: \n")
			
		for index, item in enumerate(menu):	# Display menu items
			print("{}. {}.".format(index+1, item[0].title()))


	def show_books():	
		cursor = db.cursor()
		cursor.execute("SELECT * from book;")
		books = cursor.fetchall()	
		for item in books:	# Dsiplay the elements
			print("\n BOOK ID: {}). Name: {}. Author: {}. Comments: {}".format(item[0],item[1],item[2],item[3]))


	def show_locations():
			cursor = db.cursor()
			cursor.execute("select * from store;")
			locations = cursor.fetchall()
			
			for item in locations: # print the store locations
				print()
				print(item[1])


	def validate_user(): # Take in user selection 
		print("\nPlease enter the number of your user ID: \n")
		user_input_id = int(input())	
		cursor = db.cursor()
		
		cursor.execute("select * from whatabook.user where user_id = {};".format(user_input_id))
		user_Ids = cursor.fetchall()	
		print()
		print("USER INFORMATION: \n\nUser ID: {}\nFirst Name: {}\nLast Name: {}".format(user_Ids[0][0], user_Ids[0][1],user_Ids[0][2]))
		input(("\nPress Enter to see the Account Menu: \n"))
		show_account_menu() # created method to print an account menu per instruction
		try:	
			user_in = int(input("Enter Selection: ")) # Take input and invoke method
			if user_in == 1:
				show_wishlist()
			elif user_in == 2:
				show_books_to_add()
				books_to_add_wish()
			elif user_in == 3:
				show_menu()
			elif user_in == -1:
				y = -1 
		except ValueError:
			print("Incorrect input.")

	def show_wishlist():
		print("\nPlease enter the number of your user ID: \n")
		user_input_id = int(input())
		cursor = db.cursor()				
		cursor.execute("select * from wishlist inner join user on wishlist.user_id = user.user_id inner join book on wishlist.book_id = book.book_id where user.user_id = {};".format(user_input_id)   )	
		user_ids = cursor.fetchall()
		for item in user_ids:
			print("\nWISHLIST ID: {}. USER ID: {}. FIRST AND LAST NAME: {} {}\n\nBOOK ID: {}. AUTHOR: {}. BOOK NAME: {}".format(item[0], item[1], item[4], item[5],item[6],item[8], item[7]   ))
		
		input("\nPress enter to view books to add to wishlist\n")
		show_books_to_add()	
		books_to_add_wish()


	def show_books_to_add():
		cursor = db.cursor()
		cursor.execute("select * from whatabook.book;")
		books = cursor.fetchall()	
		for item in books:
			print("\n BOOK ID: {}). Name: {}. Author: {}. Comments: {}".format(item[0],item[1],item[2],item[3]))
		
		
	def books_to_add_wish():
		cursor = db.cursor()
		cursor.execute("select * from whatabook.book;")
		books = cursor.fetchall()
		user_id = input("\nPlease Enter user_id again to proceed adding the book: ")
		add_this_book = input("\nPlease enter the number of the book ID of the book to add: ")
		cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {});".format(user_id, add_this_book))
		db.commit()
		additions = cursor.fetchall()
		
			
	def show_account_menu():
		print("ACCOUNT MENU:")
		print("1. Wishlist\n2. Add book\n3. Main Menu\n")

	""" END OF METHODS """	
			
	show_menu()
	print("\nPlease select 1, 2, 3, or 4 from the menu. or -1 to quit at any time")
	try:
		user_input = int(input())
		if user_input == 1:
			show_books()
		if user_input == 2:
			show_locations()
		if user_input == 3:
			validate_user()	
		if user_input == 4:
			show_wishlist()	
		if user_input == -1:
			y = -1			
	except ValueError:
		print("Incorrect input.")
		
db.close()
