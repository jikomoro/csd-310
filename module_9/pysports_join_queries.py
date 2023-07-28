"""
Title: pysports_join_queries.py
Author: Jae Dillon
Date: July 27, 2023
Description: Program that joins player and team tables
"""

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

#try/catch block to handle MySQL database errors
try:
    #connects to pysports database
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    #inner join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #retrieves result from cursor object
    players = cursor.fetchall()

    print("\n -- DISPLAYING PLAYER RECORDS --")

    #iterates over player data set
    for player in players:
        print("\n Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
    input("\n Press any key to continue...")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")

    else:
        print(err)

#closes MySQL connection
finally:
    
    db.close()
