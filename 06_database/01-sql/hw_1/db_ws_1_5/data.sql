SELECT * FROM users;

-- 1
SELECT *
FROM users
WHERE age >= 30 AND balance >= 1000;

-- 2
SELECT *
FROM users
WHERE balance <= 1000 AND age <= 20;

-- 3
SELECT *
FROM users
WHERE
  first_name LIKE '현%'
  AND country = '제주특별자치도'
ORDER BY age DESC
LIMIT 1;

-- 4
SELECT *
FROM users
WHERE
  last_name = '박' AND age >= 25
ORDER BY age
LIMIT 1;

-- 5
SELECT *
FROM users
WHERE
  first_name = '재은' OR first_name = '영일'
ORDER BY balance DESC
LIMIT 1;

-- 6
SELECT 
  first_name,
  last_name,
  age,
  country,
  phone,
  balance AS max_balance
FROM users
GROUP BY country
HAVING MAX(balance)
ORDER BY balance DESC;

-- 7
SELECT *
FROM users
WHERE
age >= 30 AND balance > (SELECT AVG(balance) FROM users WHERE age >= 30);