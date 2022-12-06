-- INSERT!
-- INSERT INTO table_name (column_name1, column_name2) 
-- VALUES('column1_value', 'column2_value');

INSERT INTO users (first_name, surname, email)
VALUES ('Spencer', 'Rauch', 'srauch@dojo.com');

INSERT INTO users (first_name, surname, email)
VALUES ('Max', 'Salzman', 'max@dojo.com'),
("Justin", "Lau","jlau@dojo.com");

INSERT INTO items (name, description)
VALUES ("apple","round red fruit"),
("back scratcher", "you scratch me I scratch u"),
("pickles","vinegar + cuke"),
("ps5", "game console");

INSERT INTO addresses (city, state, zip, user_id)
VALUES ("Welches","OR","97067", 1); 

INSERT INTO orders (cost, user_id)
VALUES (3.50,1);

INSERT INTO orders_has_items (order_id, item_id)
VALUES (1, 1), (1,2);

-- SELECT (what to grab) FROM (table to grab from) WHERE condition
SELECT first_name FROM users;

SELECT city, state FROM addresses;

sElEcT * FROM UsErS WHERE id > 1 ORDER BY first_name DESC;

-- UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition;
UPDATE users SET first_name = "Bob", surname = "Bobberts" WHERE id = 1;
SELECT * FROM users;

-- SET SQL_SAFE_UPDATES = 0 
-- DELETE FROM table_name WHERE condition;

DELETE FROM users WHERE id = 4;

SELECT CONCAT(first_name, " ", surname) AS full_name FROM users;