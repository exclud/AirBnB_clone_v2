 -- Task: Set up MySQL development environment
 -- Create the database if it does not exist
 CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
 -- Create the user if it does not exist and set the password
 CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
 -- Grant all privileges on the database to the user
 GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
 -- Grant select privileges on the performance schema to the user
 GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
 -- Apply the privilege changes immediately
 FLUSH PRIVILEGES;
