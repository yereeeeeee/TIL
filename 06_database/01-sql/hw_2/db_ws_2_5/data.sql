-- INSERT INTO employees (name, age, salary, departmentId) VALUES ('이규보', 77,  1700, 1);      
-- INSERT INTO employees (name, age, salary, departmentId) VALUES ('김구', 21,  126000, 2);
-- INSERT INTO employees (name, age, salary, departmentId) VALUES ('안중근', 37,  23000, 3);
-- INSERT INTO employees (name, age, salary, departmentId) VALUES ('유관순', 41,  82000, 4);  

-- 1
SELECT 
  departments.name AS department,
  employees.name AS oldest_employee,
  MAX(age) AS max_age,
  AVG(age) AS avg_age
FROM employees
JOIN departments ON employees.departmentId = departments.id
GROUP BY departmentId;

-- 2
SELECT 
  departments.name AS department,
  employees.name AS highest_paid_employee,
  MAX(salary) AS max_salary
FROM employees
JOIN departments ON employees.departmentId = departments.id
GROUP BY departmentId;

-- 3
SELECT 
  departments.name AS department,
  age_group,
  COUNT(employees) AS num_employees
FROM employees
JOIN departments ON employees.departmentId = departments.id
GROUP BY (