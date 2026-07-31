CREATE DATABASE oy4;

USE oy4;

CREATE TABLE komp(brand TEXT, model TEXT, cpu TEXT, frequency REAL, ram INT, os TEXT, price INT);

INSERT INTO komp (brand, model, cpu, frequency, ram, os, price) VALUES
('Apple', 'MacBook Air M1', 'Apple M1', 3.2, 8, 'macOS Monterey', 999),
('Apple', 'MacBook Pro 13', 'Apple M1', 3.2, 16, 'macOS Ventura', 1299),
('ASUS', 'ZenBook 14', 'Intel Core i7', 2.8, 16, 'Windows 11', 1150),
('ASUS', 'ROG Zephyrus', 'AMD Ryzen 7', 3.2, 16, 'Windows 11', 1450),
('ASUS', 'TUF Gaming', 'Intel Core i5', 2.5, 8, 'Windows 10', 850),
('Lenovo', 'IdeaPad 3', 'Intel Core i3', 3.0, 8, 'Windows 11', 500),
('Lenovo', 'ThinkPad X1', 'Intel Core i7', 2.8, 16, 'Windows 11', 1600),
('Lenovo', 'Legion 5', 'AMD Ryzen 7', 3.2, 16, 'Windows 11', 1200),
('HP', 'Pavilion 15', 'AMD Ryzen 5', 2.1, 8, 'Windows 10', 650),
('HP', 'Envy x360', 'AMD Ryzen 5', 2.1, 16, 'Windows 11', 890),
('HP', 'Spectre x360', 'Intel Core i7', 2.8, 16, 'Windows 11', 1500),
('Dell', 'XPS 13', 'Intel Core i7', 2.8, 16, 'Windows 11', 1400),
('Dell', 'Inspiron 15', 'Intel Core i5', 2.5, 8, 'Windows 10', 600),
('Dell', 'G15 Gaming', 'AMD Ryzen 7', 3.2, 16, 'Windows 11', 1100),
('Acer', 'Aspire 5', 'Intel Core i3', 3.0, 8, 'Windows 11', 450),
('Acer', 'Swift 3', 'AMD Ryzen 5', 2.1, 8, 'Ubuntu 20.04', 580),
('Acer', 'Nitro 5', 'Intel Core i5', 2.5, 16, 'Windows 11', 950),
('MSI', 'Modern 14', 'Intel Core i3', 3.0, 8, 'Ubuntu 20.04', 520),
('MSI', 'GF63 Thin', 'Intel Core i5', 2.5, 16, 'Windows 10', 880),
('MSI', 'Stealth 15', 'Intel Core i7', 2.8, 32, 'Windows 11', 2100);

SELECT * FROM KOMP;
+--------+----------------+---------------+-----------+------+----------------+-------+
| brand  | model          | cpu           | frequency | ram  | os             | price |
+--------+----------------+---------------+-----------+------+----------------+-------+
| Apple  | MacBook Air M1 | Apple M1      |       3.2 |    8 | macOS Monterey |   999 |
| Apple  | MacBook Pro 13 | Apple M1      |       3.2 |   16 | macOS Ventura  |  1299 |
| ASUS   | ZenBook 14     | Intel Core i7 |       2.8 |   16 | Windows 11     |  1150 |
| ASUS   | ROG Zephyrus   | AMD Ryzen 7   |       3.2 |   16 | Windows 11     |  1450 |
| ASUS   | TUF Gaming     | Intel Core i5 |       2.5 |    8 | Windows 10     |   850 |
| Lenovo | IdeaPad 3      | Intel Core i3 |         3 |    8 | Windows 11     |   500 |
| Lenovo | ThinkPad X1    | Intel Core i7 |       2.8 |   16 | Windows 11     |  1600 |
| Lenovo | Legion 5       | AMD Ryzen 7   |       3.2 |   16 | Windows 11     |  1200 |
| HP     | Pavilion 15    | AMD Ryzen 5   |       2.1 |    8 | Windows 10     |   650 |
| HP     | Envy x360      | AMD Ryzen 5   |       2.1 |   16 | Windows 11     |   890 |
| HP     | Spectre x360   | Intel Core i7 |       2.8 |   16 | Windows 11     |  1500 |
| Dell   | XPS 13         | Intel Core i7 |       2.8 |   16 | Windows 11     |  1400 |
| Dell   | Inspiron 15    | Intel Core i5 |       2.5 |    8 | Windows 10     |   600 |
| Dell   | G15 Gaming     | AMD Ryzen 7   |       3.2 |   16 | Windows 11     |  1100 |
| Acer   | Aspire 5       | Intel Core i3 |         3 |    8 | Windows 11     |   450 |
| Acer   | Swift 3        | AMD Ryzen 5   |       2.1 |    8 | Ubuntu 20.04   |   580 |
| Acer   | Nitro 5        | Intel Core i5 |       2.5 |   16 | Windows 11     |   950 |
| MSI    | Modern 14      | Intel Core i3 |         3 |    8 | Ubuntu 20.04   |   520 |
| MSI    | GF63 Thin      | Intel Core i5 |       2.5 |   16 | Windows 10     |   880 |
| MSI    | Stealth 15     | Intel Core i7 |       2.8 |   32 | Windows 11     |  2100 |
+--------+----------------+---------------+-----------+------+----------------+-------+

----------------------------------------------MISOLAR-1----------------------

SELECT * FROM KOMP ORDER BY price DESC LIMIT 1;
+-------+------------+---------------+-----------+------+------------+-------+
| brand | model      | cpu           | frequency | ram  | os         | price |
+-------+------------+---------------+-----------+------+------------+-------+
| MSI   | Stealth 15 | Intel Core i7 |       2.8 |   32 | Windows 11 |  2100 |
+-------+------------+---------------+-----------+------+------------+-------+

----------------------------------------------MISOL-2-------------------------
SELECT * FROM KOMP ORDER BY price LIMIT 1;
+-------+----------+---------------+-----------+------+------------+-------+
| brand | model    | cpu           | frequency | ram  | os         | price |
+-------+----------+---------------+-----------+------+------------+-------+
| Acer  | Aspire 5 | Intel Core i3 |         3 |    8 | Windows 11 |   450 |
+-------+----------+---------------+-----------+------+------------+-------+

---------------------------------------------MISOL-3-------------------------
SELECT frequency FROM KOMP WHERE cpu LIKE "%INTEL%" AND price BETWEEN 400 AND 1000;
+-----------+
| frequency |
+-----------+
|       2.5 |
|         3 |
|       2.5 |
|         3 |
|       2.5 |
|         3 |
|       2.5 |
+-----------+

--------------------------------------------MISOL-4-------------------------------
SELECT COUNT(*) AS APPLE_BRENDLAR_SON FROM KOMP WHERE brand LIKE "%APPLE%";
+--------------------+
| APPLE_BRENDLAR_SON |
+--------------------+
|                  2 |
+--------------------+

--------------------------------------------MISOL-5-------------------------------
SELECT * FROM KOMP WHERE OS LIKE "%Windows%" AND RAM =8 AND brand LIKE "%ASUS" ORDER BY price;
+-------+------------+---------------+-----------+------+------------+-------+
| brand | model      | cpu           | frequency | ram  | os         | price |
+-------+------------+---------------+-----------+------+------------+-------+
| ASUS  | TUF Gaming | Intel Core i5 |       2.5 |    8 | Windows 10 |   850 |
+-------+------------+---------------+-----------+------+------------+-------+