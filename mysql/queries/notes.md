# Querying the DB

## CRUD

1. add information
2. delete info
3. change info
4. get the info
---
```
1. Create -> INSERT INTO 
    INSERT INTO table (columns1, column2, etc) VALUES (value1, value2,etc);

    * don't need created_at and updated_at does by default
    INSERT INTO users (first_name, last_name, email, password) VALUES("Tyler", "Tbo", "tt@email.com", "Thibault"):
    
2. Read / Retrieve -> SELECT
    SELECT * FROM nov_test_db.users;
    SELECT * FROM nov_test_db.users WHERE id = 1;
    
    # Functions
    SELECT *, CONCAT_WS(" ", first_name, last_name) AS fullname from nov_test_db.users;

3. Update -> UPDATE
    UPDATE table SET column1=value1
    UPDATE users SET last_name="Thibault" WHERE id=1;

4. Delete / Destroy -> DELETE
    DELETE from users() WHERE id = 2;

## Change database table
    USE [database];





