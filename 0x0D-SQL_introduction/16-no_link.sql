-- lists all records of the table second_table

SELECT score, name FROM second_table WHERE name exists ORDER BY score DESC; 