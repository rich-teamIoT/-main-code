DROP DATABASE IF EXISTS journallpnu;
CREATE DATABASE journallpnu;
USE journallpnu;
GRANT USAGE ON *.* TO 'root'@'localhost' IDENTIFIED BY '<richbeach>';
GRANT ALL PRIVILEGES ON journallpnu.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
