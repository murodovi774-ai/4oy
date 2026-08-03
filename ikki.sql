CREATE TABLE transport(id int AUTO_INCREMENT primary key,route_number VARCHAR(10) NOT NULL,start_point VARCHAR(50) NOT NULL,end_point VARCHAR(50) NOT NULL,duration_min INT NOT NULL,distance_km DECIMAL(5,1) NOT NULL,ticket_price DECIMAL(5,2) NOT NULL,bus_type VARCHAR(20) NOT NULL);

INSERT INTO transport
(route_number, start_point, end_point, duration_min, distance_km, ticket_price, bus_type)
VALUES
('12', 'Chorsu', 'Yunusobod', 35, 14.5, 300.00, 'Shahar'),
('21A', 'Sergeli', 'Chilonzor', 40, 18.2, 350.00, 'Shahar'),
('75', 'Olmazor', 'Qo''yliq', 50, 22.4, 400.00, 'Shahar'),
('5', 'Bektemir', 'Markaz', 60, 28.7, 500.00, 'Tezyurar'),
('18', 'Yakkasaroy', 'TTZ', 45, 20.3, 350.00, 'Shahar'),
('33', 'Qorasuv', 'Do''stlik', 55, 25.8, 450.00, 'Tezyurar'),
('8', 'Paxtakor', 'Beruniy', 25, 10.6, 250.00, 'Elektr'),
('41', 'Chorsu', 'Qo''yliq', 48, 21.1, 400.00, 'Shahar'),
('60', 'Sergeli', 'Beruniy', 65, 30.5, 550.00, 'Tezyurar'),
('14', 'Yunusobod', 'Olmazor', 38, 16.9, 300.00, 'Elektr'),
('90', 'TTZ', 'Bektemir', 70, 33.2, 600.00, 'Tezyurar'),
('27', 'Chilonzor', 'Paxtakor', 30, 12.8, 280.00, 'Shahar');

+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+
| id | route_number | start_point | end_point | duration_min | distance_km | ticket_price | bus_type |
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+
|  1 | 12           | Chorsu      | Yunusobod |           35 |        14.5 |       300.00 | Shahar   |
|  2 | 21A          | Sergeli     | Chilonzor |           40 |        18.2 |       350.00 | Shahar   |
|  3 | 75           | Olmazor     | Qoyliq    |           50 |        22.4 |       400.00 | Shahar   |
|  4 | 5            | Bektemir    | Markaz    |           60 |        28.7 |       500.00 | Tezyurar |
|  5 | 18           | Yakkasaroy  | TTZ       |           45 |        20.3 |       350.00 | Shahar   |
|  6 | 33           | Qorasuv     | Dostlik   |           55 |        25.8 |       450.00 | Tezyurar |
|  7 | 8            | Paxtakor    | Beruniy   |           25 |        10.6 |       250.00 | Elektr   |
|  8 | 41           | Chorsu      | Qoyliq    |           48 |        21.1 |       400.00 | Shahar   |
|  9 | 60           | Sergeli     | Beruniy   |           65 |        30.5 |       550.00 | Tezyurar |
| 10 | 14           | Yunusobod   | Olmazor   |           38 |        16.9 |       300.00 | Elektr   |
| 11 | 90           | TTZ         | Bektemir  |           70 |        33.2 |       600.00 | Tezyurar |
| 12 | 27           | Chilonzor   | Paxtakor  |           30 |        12.8 |       280.00 | Shahar   |
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+

SELECT * FROM transport ORDER BY ticket_price;
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+
| id | route_number | start_point | end_point | duration_min | distance_km | ticket_price | bus_type |
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+
|  7 | 8            | Paxtakor    | Beruniy   |           25 |        10.6 |       250.00 | Elektr   |
| 12 | 27           | Chilonzor   | Paxtakor  |           30 |        12.8 |       280.00 | Shahar   |
|  1 | 12           | Chorsu      | Yunusobod |           35 |        14.5 |       300.00 | Shahar   |
| 10 | 14           | Yunusobod   | Olmazor   |           38 |        16.9 |       300.00 | Elektr   |
|  2 | 21A          | Sergeli     | Chilonzor |           40 |        18.2 |       350.00 | Shahar   |
|  5 | 18           | Yakkasaroy  | TTZ       |           45 |        20.3 |       350.00 | Shahar   |
|  3 | 75           | Olmazor     | Qoyliq    |           50 |        22.4 |       400.00 | Shahar   |
|  8 | 41           | Chorsu      | Qoyliq    |           48 |        21.1 |       400.00 | Shahar   |
|  6 | 33           | Qorasuv     | Dostlik   |           55 |        25.8 |       450.00 | Tezyurar |
|  4 | 5            | Bektemir    | Markaz    |           60 |        28.7 |       500.00 | Tezyurar |
|  9 | 60           | Sergeli     | Beruniy   |           65 |        30.5 |       550.00 | Tezyurar |
| 11 | 90           | TTZ         | Bektemir  |           70 |        33.2 |       600.00 | Tezyurar |
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+

SELECT * FROM transport ORDER BY distance_km DESC LIMIT 3;
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+
| id | route_number | start_point | end_point | duration_min | distance_km | ticket_price | bus_type |
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+
| 11 | 90           | TTZ         | Bektemir  |           70 |        33.2 |       600.00 | Tezyurar |
|  9 | 60           | Sergeli     | Beruniy   |           65 |        30.5 |       550.00 | Tezyurar |
|  4 | 5            | Bektemir    | Markaz    |           60 |        28.7 |       500.00 | Tezyurar |
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+

SELECT * FROM transport WHERE duration_min > 30 AND bus_type = "shahar";
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+
| id | route_number | start_point | end_point | duration_min | distance_km | ticket_price | bus_type |
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+
|  1 | 12           | Chorsu      | Yunusobod |           35 |        14.5 |       300.00 | Shahar   |
|  2 | 21A          | Sergeli     | Chilonzor |           40 |        18.2 |       350.00 | Shahar   |
|  3 | 75           | Olmazor     | Qoyliq    |           50 |        22.4 |       400.00 | Shahar   |
|  5 | 18           | Yakkasaroy  | TTZ       |           45 |        20.3 |       350.00 | Shahar   |
|  8 | 41           | Chorsu      | Qoyliq    |           48 |        21.1 |       400.00 | Shahar   |
+----+--------------+-------------+-----------+--------------+-------------+--------------+----------+

SELECT bus_type,AVG(ticket_price) AS CHIPTA_NARXI FROM transport GROUP BY bus_type;
+----------+--------------+
| bus_type | CHIPTA_NARXI |
+----------+--------------+
| Shahar   |   346.666667 |
| Tezyurar |   525.000000 |
| Elektr   |   275.000000 |
+----------+--------------+