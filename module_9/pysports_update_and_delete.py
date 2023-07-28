"""
Title: pysports_update_and_delete.py
Author: Jae Dillon
Date: July 27, 2023
Description: Program that inserts, updates, and deletes records from pysports database
"""

#import statements
import mysql.connector
from mysql.connector import errorcode

#database config object
config = {
    "user": "pysports_user",
    "password": "kijoro45",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_players(cursor, title):

    #execute inner join on player and team table
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #retrieves results from cursor object
    players = cursor.fetchall()

    print("\n -- {} --".format(title))

    #iterates over player data set
    for player in players:
        print("\n Player ID: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

#try/catch block to handle MySQL database errors
try:

    #connects to pysports db
    db = mysql.connector.connect(**config)

    #gets cursor object
    cursor = db.cursor()

    #inserts player query
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                  "VALUES(%s, %s, %s)") #incorporates a string within another string
    
    #player data fields
    player_data = ("Ivan", "Orlov", 1)

    #inserts a new player record
    cursor.execute(add_player, player_data)

    #commits insert to the db
    db.commit()

    #shows all records in player table
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    #updates the new record
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Steven', last_name = 'Yoo' WHERE first_name = 'Ivan'")

    #executes update query
    cursor.execute(update_player)

    #shows all records in player table
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    #deletes query
    delete_player = ("DELETE FROM player WHERE first_name = 'Steven'")

    cursor.execute(delete_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n Press any key to continue...")

except mysql.connector.Error as err:

    if err.errno = errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")

    else:
        print(err)

#closes MySQL connection
finally:

    db.close()
