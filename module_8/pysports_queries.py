"""
Title: pysports_queries.py
Author: Jae Dillon
Date July 21, 2023
Description: Execute queries against pysports database
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
    #connect to pysports db
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    #selects query from team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    teams = cursor.fetchall()
    print("\n -- DISPLAYING TEAM RECORDS --")

    #iterate over teams data set
    for team in teams:
        print("\n Team ID: {}\n Team Name {}\n Mascot: {}\n".format(team[0], team[1], team[2]))

    #selects query from player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    players = cursor.fetchall()

    print("\n -- DISPLAYING PLAYER RECORDS --")

    #iterate over player data set
    for player in players:
        print("\n Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))
    
    input("\n Press any key to continue...")

except mysql.connector.Error as err:
    #error handling

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")

    else:
        print(err)

#closes MySQL connection
finally:
    db.close()
