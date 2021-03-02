-- creates the database hbtn_0d_usa and the table cities.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    state_id INT NOT NULL FOREIGN KEY(state_id), name VARCHAR(256) NOT NULL);