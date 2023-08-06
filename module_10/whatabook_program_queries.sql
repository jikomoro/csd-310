/*
Title: whatabook_program_queries.sql
Author: Jae Dillon
Date: August 2023
Description: WhatABook program queries
*/

/* Select query to view wishlist items for a user */
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
  INNER JOIN user ON wishlist.user_id = user.user_id
  INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

/* Select query to view location of store */
SELECT store_id, locale from store;

/* Select query to view the whole WhatABook book listing */

SELECT book_id, book_name, author, book_details from book;

/* Select query to view books that are not in any user wishlist */
SELECT book_id, book_name, author, book_details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 1);

/* Insert statement that adds a book to a user wishlist */
INSERT INTO wishlist(user_id, book_id)
  VALUES()

/* Delete statement to remove a book from a user wishlist */
DELETE FROM wishlist WHERE user_id = 1 AND book_id = 2;
