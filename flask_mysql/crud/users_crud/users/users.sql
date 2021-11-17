INSERT INTO users (first_name, last_name, email) VALUES ("Shawna","Hightower","sh@gmail.com");
SELECT * FROM users ORDER BY first_name DESC;
SELECT * FROM users WHERE id = 3;
UPDATE users SET last_name= "Pancakes" WHERE id=3;
DELETE from users WHERE id = 2;