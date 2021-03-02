-- creates the database hbtn_0d_2 and the user user_0d_2

CREATE IF NOT EXISTS hbtn_0d_2;
CREATE IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';