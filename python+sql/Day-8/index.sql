EXPLAIN
SELECT *
FROM employees
WHERE salary > 50000;

CREATE INDEX idx_salary
ON employees(salary);

EXPLAIN
SELECT *
FROM employees
WHERE salary > 50000;

SHOW INDEX FROM employees;