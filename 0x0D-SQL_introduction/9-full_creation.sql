-- creates a table second_table
CREATE if not exists table second_table (id INT, name VARCHAR(256), score INT);
insert INTO second_table(id, name, score)
values("1", "John", "10");
values("2", "Alex", "3");
values("3", "Bob", "14");
values("4", "George", "8");