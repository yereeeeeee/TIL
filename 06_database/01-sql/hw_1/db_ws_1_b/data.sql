-- 1. 데이터 조회
SELECT * FROM songs;

-- 2. 데이터 정렬
SELECT * FROM songs ORDER BY title DESC;

-- 3. 데이터 필터링
SELECT * FROM songs WHERE genre = 'Pop';

-- 4. 조건부 조회
SELECT * FROM songs WHERE duration >= 180;