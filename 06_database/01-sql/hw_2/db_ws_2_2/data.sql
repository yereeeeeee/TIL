-- 1
ALTER TABLE zoo
ADD COLUMN species2 TEXT;

-- 2
UPDATE zoo
SET species2 = 'Panthera leo'
WHERE name = 'Lion';

UPDATE zoo
SET species2 = 'Loxodonta africana'
WHERE name = 'Elephant';

UPDATE zoo
SET species2 = 'Giragga camelopardalis'
WHERE name = 'Giraffe';

UPDATE zoo
SET species2 = 'Cebus capucinus'
WHERE name = 'Monkey';

-- 3
UPDATE zoo
SET height = height * 2.54;

-- 4
SELECT * FROM zoo;