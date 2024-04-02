-- 1. 테이블 생성
CREATE TABLE transactions (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  amount TEXT,
  transaction_date DATE,
  FOREIGN KEY(user_id) REFERENCES users(id)
);

-- 2. data 삽입
INSERT INTO transactions (id, user_id, amount, transaction_date) VALUES
  (1, 1, 500, '2024-03-15'),
  (2, 2, 700, '2024-03-16'),
  (3, 1, 200, '2024-03-17'),
  (4, 3, 1000, '2024-03-18');

SELECT * FROM transactions;

-- 3. 조회
SELECT first_name, last_name, amount, transaction_date
FROM users
JOIN transactions ON users.id = transactions.user_id;

-- 4
SELECT first_name, last_name, amount, transaction_date
FROM users
JOIN transactions ON users.id = transactions.user_id
WHERE transaction_date > '2024-03-16';

-- 5
SELECT first_name, last_name, SUM(amount) AS total_amount
FROM users
JOIN transactions ON users.id = transactions.user_id
GROUP BY user_id;