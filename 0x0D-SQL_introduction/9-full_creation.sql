-- creates a table second_table
CREATE if not exists table second_table (id INT, name VARCHAR(256), score INT);
insert INTO second_table(id, name, score)
VALUES("1", "John", "10");
VALUES("2", "Alex", "3");
VALUES("3", "Bob", "14");
VALUES("4", "George", "8");