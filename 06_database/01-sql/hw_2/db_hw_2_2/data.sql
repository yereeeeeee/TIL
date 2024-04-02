-- 1. order
-- SELECT * FROM orders;
-- DROP TABLE orders;

CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE NOT NULL,
  total_amount REAL NOT NULL
);

INSERT INTO
  orders(order_date, total_amount)
VALUES
  ('2023-07-15', 50.99),
  ('2023-07-16', 75.50),
  ('2023-07-17', 30.25);

-- 2. customers
-- SELECT * FROM customers;
-- DROP TABLE customers;

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL
);

INSERT INTO
  customers(name, email, phone)
VALUES
  ('허균', 'hong.gildong@example.com', '010-1234-5678'),
  ('김영희', 'kim.younghee@example.com', '010-9876-5432'),
  ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');

-- 3. 데이터 수정
-- 3-1.
DELETE FROM orders
WHERE order_id = 3;

-- 3-2.
UPDATE customers
SET name = '홍길동'
WHERE customer_id = 1;

-- 4. 조회
SELECT * FROM orders;
SELECT * FROM customers;