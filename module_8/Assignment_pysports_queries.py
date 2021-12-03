
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

cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()

for team in teams:
	print("Team Name: {}".format(team[1]))

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()

for player in players:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))
input("\n\nPress any key to continue... ")

db.close()
