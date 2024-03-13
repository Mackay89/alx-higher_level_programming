-- task: Script to create database hbtn_0d_usa and table cities on MySQL server.
-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
-- use a database
USE hbtn_0d_usa;
-- creates a table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL, state_id INT NOT NULL, name VARCHAR(2256) NOT NULL, PRIMARY KEY(id), FOREIGN KEY(state_id) references states(id));

