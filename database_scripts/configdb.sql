DROP DATABASE IF EXISTS journallpnu;
CREATE DATABASE journallpnu;
USE journallpnu;
GRANT USAGE ON *.* TO 'rich'@'localhost' IDENTIFIED BY '<richrich1234>';
GRANT ALL PRIVILEGES ON journallpnu.* TO 'rich'@'localhost';
FLUSH PRIVILEGES;
USE journallpnu;
DROP TABLE IF EXISTS users;
CREATE TABLE users (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, login VARCHAR(100), user_name VARCHAR(100), email VARCHAR(100), password VARCHAR(100));
