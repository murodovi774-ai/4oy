CREATE TABLE janr(id int AUTO_INCREMENT primary key, name VARCHAR(50) NOT NULL);
CREATE TABLE author(id int AUTO_INCREMENT primary key, name VARCHAR(50) NOT NULL);
CREATE TABLE book(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL,price REAL,amount INT,j_id INT,a_id INT,FOREIGN KEY (j_id) REFERENCES janr(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (a_id) REFERENCES author(id) ON DELETE CASCADE ON UPDATE CASCADE);


SELECT * FROM book as b INNER JOIN janr as j ON b.j_id=j.id INNER JOIN author as a ON b.a_id=a.id;  
+----+------------------+--------+--------+------+------+----+--------+----+-----------------+
| id | name             | price  | amount | j_id | a_id | id | name   | id | name            |
+----+------------------+--------+--------+------+------+----+--------+----+-----------------+
| 16 | Xamsa            | 150000 |     10 |    1 |    1 |  1 | Roman  |  1 | Alisher Navoiy  |
| 17 | Lison ut-Tayr    | 120000 |      8 |    1 |    1 |  1 | Roman  |  1 | Alisher Navoiy  |
| 18 | Mahbub ul-Qulub  |  95000 |      6 |    1 |    1 |  1 | Roman  |  1 | Alisher Navoiy  |
| 19 | Otkan kunlar     |  90000 |     12 |    1 |    2 |  1 | Roman  |  2 | Abdulla Qodiriy |
| 20 | Mehrobdan chayon |  85000 |      9 |    1 |    2 |  1 | Roman  |  2 | Abdulla Qodiriy |
| 23 | Qutlug qon       |  92000 |     11 |    1 |    4 |  1 | Roman  |  4 | Oybek           |
| 26 | Hayrat ul-Abror  | 130000 |      6 |    1 |    1 |  1 | Roman  |  1 | Alisher Navoiy  |
| 27 | Farhod va Shirin | 140000 |      8 |    1 |    1 |  1 | Roman  |  1 | Alisher Navoiy  |
| 28 | Layli va Majnun  | 145000 |      7 |    1 |    1 |  1 | Roman  |  1 | Alisher Navoiy  |
| 29 | Sabai Sayyor     | 135000 |      5 |    1 |    1 |  1 | Roman  |  1 | Alisher Navoiy  |
| 30 | Saddi Iskandariy | 150000 |      4 |    1 |    1 |  1 | Roman  |  1 | Alisher Navoiy  |
| 21 | Kecha va Kunduz  |  80000 |     10 |    4 |    3 |  4 | Hikoya |  3 | Cholpon         |
| 22 | Navoiy           | 100000 |      7 |    4 |    4 |  4 | Hikoya |  4 | Oybek           |
| 24 | Songgi bahor     |  70000 |      5 |    5 |    5 |  5 | Drama  |  5 | Erkin Vohidov   |
| 25 | Yoshlik devoni   |  75000 |      9 |    5 |    5 |  5 | Drama  |  5 | Erkin Vohidov   |
+----+------------------+--------+--------+------+------+----+--------+----+-----------------+

SELECT * FROM book as b INNER JOIN janr as j ON b.j_id=j.id INNER JOIN author as a ON b.a_id=a.id HAVING a.name="Alisher Navoiy";  
+----+------------------+--------+--------+------+------+----+-------+----+----------------+
| id | name             | price  | amount | j_id | a_id | id | name  | id | name           |
+----+------------------+--------+--------+------+------+----+-------+----+----------------+
| 16 | Xamsa            | 150000 |     10 |    1 |    1 |  1 | Roman |  1 | Alisher Navoiy |
| 17 | Lison ut-Tayr    | 120000 |      8 |    1 |    1 |  1 | Roman |  1 | Alisher Navoiy |
| 18 | Mahbub ul-Qulub  |  95000 |      6 |    1 |    1 |  1 | Roman |  1 | Alisher Navoiy |
| 26 | Hayrat ul-Abror  | 130000 |      6 |    1 |    1 |  1 | Roman |  1 | Alisher Navoiy |
| 27 | Farhod va Shirin | 140000 |      8 |    1 |    1 |  1 | Roman |  1 | Alisher Navoiy |
| 28 | Layli va Majnun  | 145000 |      7 |    1 |    1 |  1 | Roman |  1 | Alisher Navoiy |
| 29 | Sabai Sayyor     | 135000 |      5 |    1 |    1 |  1 | Roman |  1 | Alisher Navoiy |
| 30 | Saddi Iskandariy | 150000 |      4 |    1 |    1 |  1 | Roman |  1 | Alisher Navoiy |
+----+------------------+--------+--------+------+------+----+-------+----+----------------+

SELECT a.name,JSON_ARRAYAGG(j.name) as Jarnirlari FROM book as b INNER JOIN janr as j ON b.j_id=j.id INNER JOIN author as a ON b.a_id=a.id GROUP BY a.name;  
+-----------------+--------------------------------------------------------------------------+
| name            | Jarnirlari                                                               |
+-----------------+--------------------------------------------------------------------------+
| Abdulla Qodiriy | ["Roman", "Roman"]                                                       |
| Alisher Navoiy  | ["Roman", "Roman", "Roman", "Roman", "Roman", "Roman", "Roman", "Roman"] |
| Cholpon         | ["Hikoya"]                                                               |
| Erkin Vohidov   | ["Drama", "Drama"]                                                       |
| Oybek           | ["Roman", "Hikoya"]                                                      |
+-----------------+--------------------------------------------------------------------------+

SELECT a.name,count(j.name) as Jarnirlari_soni FROM book as b INNER JOIN janr as j ON b.j_id=j.id INNER JOIN author as a ON b.a_id=a.id GROUP BY a.name;  
+-----------------+-----------------+
| name            | Jarnirlari_soni |
+-----------------+-----------------+
| Alisher Navoiy  |               8 |
| Abdulla Qodiriy |               2 |
| Oybek           |               2 |
| Cholpon         |               1 |
| Erkin Vohidov   |               2 |
+-----------------+-----------------+

SELECT j.name, COUNT(*) AS Janrlari_soni FROM book AS b INNER JOIN janr AS j ON b.j_id = j.id GROUP BY j.name ORDER BY Janrlari_soni DESC LIMIT 1;
+-------+---------------+
| name  | Janrlari_soni |
+-------+---------------+
| Roman |            11 |
+-------+---------------+

SELECT a.name,
       j.name AS janr,
       COUNT(*) AS soni
FROM book AS b
INNER JOIN author AS a ON b.a_id = a.id
INNER JOIN janr AS j ON b.j_id = j.id
GROUP BY a.name, j.name
ORDER BY soni DESC;
+-----------------+--------+------+
| name            | janr   | soni |
+-----------------+--------+------+
| Alisher Navoiy  | Roman  |    8 |
| Abdulla Qodiriy | Roman  |    2 |
| Erkin Vohidov   | Drama  |    2 |
| Cholpon         | Hikoya |    1 |
| Oybek           | Hikoya |    1 |
| Oybek           | Roman  |    1 |
+-----------------+--------+------+

select * from book as b inner join author as a on b.a_id=a.id inner join janr as j on b.j_id=j.id order by amount desc limit 1;
+----+---------------+-------+--------+------+------+----+-----------------+----+-------+
| id | name          | price | amount | j_id | a_id | id | name            | id | name  |
+----+---------------+-------+--------+------+------+----+-----------------+----+-------+
| 19 | Otkan kunlar  | 90000 |     12 |    1 |    2 |  2 | Abdulla Qodiriy |  1 | Roman |
+----+---------------+-------+--------+------+------+----+-----------------+----+-------+

