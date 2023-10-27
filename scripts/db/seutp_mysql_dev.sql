-- script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS esset_dev_db;

CREATE USER IF NOT EXISTS 'esset_dev'@'localhost' IDENTIFIED BY 'esset_dev_pwd';

GRANT ALL PRIVILEGES ON `esset_dev_db`.* TO 'esset_dev'@'localhost';

GRANT SELECT ON `performance_schema`.* TO 'esset_dev'@'localhost';

FLUSH PRIVILEGES;
