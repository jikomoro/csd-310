"""
Title: whatabook_program.py
Author: Jae Dillon
Date: August 2023
Description: WhatABook program
"""

#import statements
import sys
import mysql.connector
from mysql.connector import errorcode

#database config object
config = {
  "user": "whatabook_user",
  "password": "MySQL8IsGreat!",
  "host": "127.0.0.1",
  "database": "whatabook",
  "raise_on_warnings": True
}

#create methods
def show_menu():
  print("\n MAIN MENU")
  print("\n 1. View Books\n  2. View Store Locations\n  3. My Account\n  4. Exit")

#user input to navigate the program
  try:
    choice = int(input('Enter your selection: '))
    
    return choice
  except ValueError:
    print("\n Invalid number. Terminating program.\n")
    
    sys.exit(0)

def show_books(_cursor):
  #queries the db for book list
  _cursor.execute("SELECT book_id, book_name, author, book_details FROM book")
  
  books = _cursor.fetchall()
  
  print("Book List")
  for book in books:
    print("Book Name: {}\n Author: {}\n Book Details: {}\n".format(book[0], book[1], book[2]))

def show_locations(_cursor):
  #queries the db for store locations
  _cursor.execute("SELECT store_id, locale FROM store")
  
  locations = _cursor.fetchall()
  
  print("Store Locations")
  
  for location in locations:
    print("Locale: {}\n".format(location[1]))

def validate_user():
  #validates user ID
  try:
    user_id = int(input('\n Enter a customer ID: '))
    
    if user_id < 0 or user_id > 3:
      print("\n Invalid customer ID. Terminating program.\n")
      sys.exit(0)

    return user_id
  
  except ValueError:
    print("\n Invalid option. Terminating program.")
    
    sys.exit(0)

def show_account_menu():
  #displays user account menu
  try:
    print("\n Customer Menu")
    print("  1. Wishlist\n  2. Add Book\n  3. Main Menu")
    account_option = int(input(' Enter your selection: '))
    
    return account_option
  except ValueError:
    print("Invalid number. Terminating program.\n")
    
    sys.exit(0)

def show_wishlist(_cursor, _user_id):
  #queries db for books added to the user wishlist
  #two inner joins to combine user and book tables
  _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                  "FROM wishlist " +
                  "INNER JOIN user ON wishlist.user_id = user.user_id " +
                  "INNER JOIN book ON wishlist.book_id = book.book_id " +
                  "WHERE user.user_id = {}".format(_user_id))
  
  wishlist = _cursor.fetchall()

  print("\n Displaying Wishlist Items")

  for book in wishlist:
    print("\n Book Name: {}\n Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
  #queries db for books not in user wishlist with NOT IN
  query = ("SELECT book_id, book_name, author, book_details "
           "FROM book "
           "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
  
  print(query)

  _cursor.execute(query)

  books_to_add = _cursor.fetchall()
  
  print("\n Available Books")

  for book in books_to_add:
    print("\n Book ID: {}\n  Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
  _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
  #handles errors when connecting to db
  db = mysql.connector.connect(**config)
  
  cursor = db.cursor()
  
  print("Welcome to the WhatABook App!")
  
  user_selection = show_menu()
  
  while user_selection != 4:
    
    if user_selection == 1:
      show_books(cursor) #displays books

    if user_selection == 2:
      show_locations(cursor) #displays location

    if user_selection == 3:
      my_user_id = validate_user()
      account_option = show_account_menu() #displays account menu

      #shows wishlist and adds items to wishlist
      while account_option != 3:
        
        if account_option == 1:
          show_wishlist(cursor, my_user_id)
          
        if account_option == 2:
          
          show_books_to_add(cursor, my_user_id)
          
          book_id = int(input("\n Enter the ID of the book you want to add to the wishlist: "))
          
          add_book_to_wishlist(cursor, my_user_id, book_id)

          db.commit()
          
          print("\n Book ID: {} was added to the wishlist.".format(book_id))

          #if input is invalid
          if account_option < 0 or account_option > 3:
            print("\n Invalid option. Please input a valid option.")

          account_option = show_account_menu()

      if user_selection < 0 or user_selection > 4:
        print("\n Invalid option. Please input a valid option.")

      user_selection = show_menu()

#handles errors
except mysql.connector.Error as err:
  
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("The username or password is invalid.")

  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("The database does not exist.")

  else:
    print(err)

#closes db connection
finally:
  
  db.close()
