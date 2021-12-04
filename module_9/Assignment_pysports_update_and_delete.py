
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
	print("Team Name: {}\n".format(team[1]))

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()

for player in players:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3] )) 

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()

# Insert new player
cursor.execute("INSERT INTO player(first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 7);")
db.commit()
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()

cursor.execute(print("AFTER INSERT\n"))

for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
#Update the record
cursor.execute("UPDATE player SET team_id = 8, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
db.commit()
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()
cursor.execute(print("AFTER UPDATE\n"))

for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

# Delete the record
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")
db.commit()
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()
cursor.execute(print("AFTER DELETION\n"))
for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

cursor.execute(print("AFTER INNER JOIN\n"))
# Inner join 
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()
for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
