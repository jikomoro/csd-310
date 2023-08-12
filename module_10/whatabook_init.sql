/*
Title: whatabook_init.sql
Author: Jae Dillon
Date August 2023
Description: WhatABook script
*/

-- creating database
CREATE DATABASE whatabook;

USE whatabook;

-- creating new user with all privileges
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- creating tables
CREATE TABLE user (
  user_id      INT          NOT NULL  AUTO_INCREMENT  PRIMARY KEY,
  first_name   VARCHAR(75)  NOT NULL,
  last_name    VARCHAR(75)  NOT NULL
  );

CREATE TABLE wishlist (
  wishlist_id INT NOT NULL AUTO_INCREMENT,
  user_id     INT NOT NULL,
  book_id     INT NOT NULL,
  PRIMARY KEY (wishlist_id),
  CONSTRAINT fk_book
  FOREIGN KEY (book_id) REFERENCES book(book_id),
  CONSTRAINT fk_user
  FOREIGN KEY (user_id) REFERENCES user(user_id)
  );

CREATE TABLE book (
  book_id   INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
  book_name VARCHAR(200) NOT NULL,
  details   VARCHAR(500),
  author    VARCHAR(200) NOT NULL
  );

CREATE TABLE store (
  store_id INT          NOT NULL PRIMARY KEY,
  locale   VARCHAR(500) NOT NULL
  );

-- creating store
INSERT INTO store(locale)
  VALUES('123 Book St., Orange, CA 92000');

-- populating book list
INSERT INTO book(book_name, author)
  VALUES('A Game of Thrones', 'George R.R. Martin');

INSERT INTO book(book_name, author)
  VALUES('A Clash of Kings', 'George R.R. Martin');

INSERT INTO book(book_name, author)
  VALUES('The Magicians Nephew', 'C.S. Lewis');

INSERT INTO book(book_name, author)
  VALUES('The Horse and His Boy', 'C.S. Lewis');

INSERT INTO book(book_name, author)
  VALUES('Prince Caspian', 'C.S. Lewis');

INSERT INTO book(book_name, author)
  VALUES('Revolution', 'Jennifer Donnelly');

INSERT INTO book(book_name, author)
  VALUES('The Tea Rose', 'Jennifer Donnelly');

INSERT INTO book(book_name, author)
  VALUES('A Thousand Splendid Suns', 'Khaled Hosseini');

INSERT INTO book(book_name, author)
  VALUES('And the Mountains Echoed', 'Khaled Hosseini');

-- creating application users
INSERT INTO user(first_name, last_name)
  VALUES('Eustace', 'Scrubb');

INSERT INTO user(first_name, last_name)
  VALUES('Ned', 'Stark');

INSERT INTO user(first_name, last_name)
  VALUES('Theon', 'Greyjoy');

-- Insert wishlist items
INSERT INTO wishlist(user_id, book_id)
  VALUES(
  (SELECT user_id FROM user WHERE first_name = 'Eustace'),
  (SELECT book_id FROM book WHERE book_name = 'Prince Caspian')
  );

INSERT INTO wishlist(user_id, book_id)
  VALUES(
  (SELECT user_id FROM user WHERE first_name = 'Ned'),
  (SELECT book_id FROM book WHERE book_name = 'A Game of Thrones')
  );

INSERT INTO wishlist(user_id, book_id)
  VALUES(
  (SELECT user_id FROM user WHERE first_name = 'Theon'),
  (SELECT book_id FROM book WHERE book_name = 'A Thousand Splendid Suns')
  );
