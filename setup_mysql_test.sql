-- Prepare a MySQL server for the project 
-- A database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user 'hbnb_test' in localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges on the database 'hbnb_test_db' to the user 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant select privileges on the database 'performance_schema' to the user 'hbnb_test'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Apply the privilege changes immediately
FLUSH PRIVILEGES;
