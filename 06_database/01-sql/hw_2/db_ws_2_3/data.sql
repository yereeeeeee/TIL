-- 1. 조회
SELECT * FROM hotels;

-- 2. 대문자로 수정
UPDATE hotels
SET grade = UPPER(grade);

-- 3. 테이블 생성
CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  name TEXT,
  email TEXT
);

CREATE TABLE reservations (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  room_num INTEGER,
  check_in TEXT,
  check_out TEXT,
  FOREIGN KEY(customer_id) REFERENCES customers(id),
  FOREIGN KEY(room_num) REFERENCES hotels(room_num)
);

-- 4. 데이터 삽입
INSERT INTO reservations (customer_id, room_num, check_in, check_out) VALUES
  (1, '101', '2024-03-20', '2024-03-25'),
  (2, '202', '2024-03-21', '2024-03-24'),
  (3, '303', '2024-03-22', '2024-03-26'),
  (4, '404', '2024-03-23', '2024-03-27');

INSERT INTO customers (id, name, email) VALUES
  (1, '홍길동', 'john@email.com'),
  (2, '박지영', 'jane@email.com'),
  (3, '김미영', 'alice@email.com'),
  (4, '이철수', 'bob@email.com');

-- 5. customers 조회
SELECT * FROM customers;

-- 6. reservations 조회
SELECT *
FROM reservations;