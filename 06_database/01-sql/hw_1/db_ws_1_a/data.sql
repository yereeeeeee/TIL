-- 0
DROP TABLE songs;

SELECT * FROM songs;

-- 1. 
CREATE TABLE songs(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  artists TEXT NOT NULL,
  album TEXT NOT NULL,
  genre TEXT NOT NULL,
  duration INTEGER NOT NULL
);

-- 2. 
INSERT INTO
  songs(title, artists, album, genre, duration)
VALUES
  ('Song 1', 'Artist 1', 'Album 1', 'pop', 200),
  ('Song 2', 'Artist 2', 'Album 2', 'Rock', 300),
  ('Song 3', 'Artist 3', 'Album 3', 'Hip Hop', 250),
  ('Song 4', 'Artist 4', 'Album 4', 'Electronic', 180),
  ('Song 5', 'Artist 5', 'Album 5', 'R&B', 320);

-- 3
UPDATE songs
SET title = 'New Title'
WHERE title = 'Song 1';