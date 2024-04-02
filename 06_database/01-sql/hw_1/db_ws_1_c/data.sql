-- 1. 데이터 그룹화
SELECT 
  genre,
  COUNT(*) AS count
FROM songs
GROUP BY genre;

-- 2. 집계 함수
SELECT 
  genre,
  COUNT(*) AS count,
  AVG(duration) AS average_duration
FROM songs
GROUP BY genre;
