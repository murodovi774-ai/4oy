CREATE DATABASE library_booking_db;

USE library_booking_db;


CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    book_title VARCHAR(150) NOT NULL,
    days INT NOT NULL,
    daily_price DECIMAL(10,2) NOT NULL,
    borrow_date DATE NOT NULL,
    return_status VARCHAR(20) NOT NULL,
    books_count INT NOT NULL
);


INSERT INTO reservations
(user_name, book_title, days, daily_price, borrow_date, return_status, books_count)
VALUES
('Ali Valiyev', 'Python', 3, 20000, '2026-05-01', 'Qaytarilgan', 1),
('Nodira Karimova', 'SQL Basics', 5, 25000, '2026-05-02', 'Qaytarilmagan', 2),
('Bekzod Ismoilov', 'Java OOP', 2, 30000, '2026-05-03', 'Qaytarilgan', 1),
('Madina Ergasheva', 'Algorithms', 4, 22000, '2026-05-04', 'Qaytarilmagan', 3),
('Sardor Xasanov', 'Data Science', 6, 35000, '2026-05-05', 'Qaytarilgan', 2),
('Dilshod Qodirov', 'C++ Basics', 3, 18000, '2026-05-06', 'Qaytarilmagan', 1),
('Shahnoza Mirzayeva', 'Web Dev', 7, 40000, '2026-05-07', 'Qaytarilgan', 4),
('Umid Rustamov', 'DSA', 2, 28000, '2026-05-08', 'Qaytarilmagan', 2),
('Kamola Tursunova', 'AI Basics', 5, 50000, '2026-05-09', 'Qaytarilgan', 3),
('Javohir Sobirov', 'Networking', 1, 15000, '2026-05-10', 'Qaytarilmagan', 1),
('Azizbek Karimov', 'Django', 8, 32000, '2026-05-11', 'Qaytarilgan', 2),
('Malika Sobirova', 'Git', 2, 12000, '2026-05-12', 'Qaytarilmagan', 1);

--misol-1
SELECT *
FROM reservations
ORDER BY borrow_date DESC;

--misol-2
SELECT *
FROM reservations
ORDER BY daily_price DESC
LIMIT 3;


--misol-3
SELECT *
FROM reservations
WHERE return_status = 'Qaytarilmagan';


--misol-4
SELECT book_title, AVG(daily_price) AS average_price
FROM reservations
GROUP BY book_title;


--misol-5
SELECT *
FROM reservations
WHERE days > 3;


--misol-6
SELECT *
FROM reservations
ORDER BY days DESC
LIMIT 1;


--misol-7
SELECT return_status, COUNT(*) AS reservation_count
FROM reservations
GROUP BY return_status;


--misol-8
SELECT *
FROM reservations
WHERE books_count > 2;


--misol-9
SELECT SUM(books_count) AS total_books
FROM reservations;


--misol-10
SELECT *
FROM reservations
WHERE daily_price > 30000;