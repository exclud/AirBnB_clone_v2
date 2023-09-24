-- Establish a database named hbnb_dev_db in the existing MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Generate a new MySQL server user named hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Provide all permissions to the user hbnb_dev for the database hbnb_dev_db
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- Grant SELECT permission on the database 'performance_schema' to the user hbnb_dev
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
