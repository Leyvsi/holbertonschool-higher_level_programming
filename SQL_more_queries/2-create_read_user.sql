-- Creates the database hbtn_0d_2 and user_0d_2 in the MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant all privileges on your MySQL server to user_0d_2
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_'@'localhost' WITH GRANT OPTION;
