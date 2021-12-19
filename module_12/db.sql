
/* create whatabook database, user, and book table */
CREATE DATABASE whatabook;

CREATE USER 'whatabook_user'@'127.0.0.1' IDENTIFIED WITH mysql_native_password BY 'schoolsql';

create table store (store_id INT NOT NULL AUTO_Increment, location, VARCHAR(500) NOT NULL, PRIMARY KEY(store_id));

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'127.0.0.1';

create table book (book_id int not null auto_increment, book_name varchar(200) not null, author varchar(200) not null, details varchar(500), primary key(book_id));

/* create table wishlist and insert address*/
CREATE TABLE wishlist ( wishlist_id INT NOT NULL AUTO_INCREMENT, user_id INT NOT NULL,  book_id INT NOT NULL, PRIMARY KEY (wishlist_id), CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES book(book_id), CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES user(user_Id));
INSERT INTO store(locale) VALUES('1000 Galvin Rd S, Bellevue, NE 68005');

/* Insert book values */

INSERT INTO book(book_name, author, details) VALUES('The Return of the King', 'J.R.Tolkien', 'The third part of The Lord of the Rings');

INSERT INTO book(book_name, author, details) VALUES('The Fellowship of the Ring', 'J.R.Tolkien', 'The first part of The Lord of the Rings');

INSERT INTO book(book_name, author, details) VALUES('The Two Towers', 'J.R.Tolkien', "The second part of The Lord of The Rings");

INSERT INTO book(book_name, author) VALUES('The Hobbit or There and Back Again', 'J.R.Tolkien');

INSERT INTO book(book_name, author) VALUES('Dune: Deluxe Edition', 'Frank Herbert');

INSERT INTO book(book_name, author) VALUES("Charlotee's Web", 'E.B. White');

INSERT INTO book(book_name, author) VALUES('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book(book_name, author) VALUES('The Lion, the Witch, and the Wardrobe', 'C.S. Lewis');

INSERT INTO book(book_name, author) VALUES('The Catcher and the Rye', 'J.D. Salinger');
  
    
  /* insert user */ 
INSERT INTO user(first_name, last_name) VALUES('Thorin', 'Oakenshield');

INSERT INTO user(first_name, last_name) VALUES('Bilbo', 'Baggins');

INSERT INTO user(first_name, last_name) VALUES('Frodo', 'Baggins');

/* insert wishlist records */
INSERT INTO wishlist(user_id, book_id) VALUES ((SELECT user_id FROM user WHERE first_name = 'Thorin'), (SELECT book_id FROM book WHERE book_name = 'The Hobbit or There and Back Again'));

INSERT INTO wishlist(user_id, book_id) VALUES ((SELECT user_id FROM user WHERE first_name = 'Bilbo'), (SELECT book_id FROM book WHERE book_name = 'The Fellowship of the Ring'));

INSERT INTO wishlist(user_id, book_id) VALUES ((SELECT user_id FROM user WHERE first_name = 'Frodo'), (SELECT book_id FROM book WHERE book_name = 'The Return of the King'));

