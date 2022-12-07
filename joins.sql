-- SELECT * FROM table_1 JOIN table_2 ON pk = fk;

SELECT * FROM addresses JOIN users ON addresses.user_id = users.id;

SELECT * FROM users JOIN orders ON users.id = orders.user_id;

SELECT orders.id as orders_pk, orders.user_id as orders_user, 
orders_has_items.order_id as join_table_order_id, 
orders_has_items.item_id as join_table_item_id,
items.id as items_pk, items.name, COUNT(items.id) as item_count
FROM orders JOIN orders_has_items 
ON orders.id = orders_has_items.order_id
JOIN items ON orders_has_items.item_id = items.id GROUP BY orders.id;


-- LEFT JOIN vs JOIN
SELECT users.first_name, orders.cost FROM users
LEFT JOIN orders on users.id = orders.user_id;