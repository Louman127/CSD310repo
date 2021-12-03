
#import mysql
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "schoolsql",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:

    db = mysql.connector.connect(**config) # connect to the pysports database    
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

cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --\n")
    
    # iterate over the player data set and display the results 
for value in players:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(value[0], value[1], value[2], value[3]))

input("\nPress any key to continue... ")

db.close()
