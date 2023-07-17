""" Attributions
Title: mysql_test.py
Author: Jae Dillon
Date: July 17, 2023
Description: Connects to the pysports database
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

try:
  #connects to pysports db
  db = mysql.connector.connect(**config)
  #connection status output
  print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

  input("\n Press any key to continue...")

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("The supplied username or password are invalid.")

  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("The specified database does not exist.")

  else:
    print(err)

finally:
  #close MySQL connection
  db.close()
