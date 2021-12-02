
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "root",
    "password": "schoolsql",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/except blocks for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    # output the connection status 
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as error:

    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" Invalid username and/or password")

    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database does not exist")

    else:
        print(error)

finally:
    """ close database after all try/except """

    db.close()
