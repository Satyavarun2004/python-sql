SELECT *
FROM employees
WHERE salary BETWEEN 45000 AND 60000;

SELECT *
FROM employees
WHERE name LIKE 'A%';


SELECT *
FROM employees
WHERE name LIKE '%ar%';


SELECT *
FROM employees
WHERE department IN ('IT', 'HR');


SELECT *
FROM employees
WHERE department IS NULL;


SELECT *
FROM employees
WHERE salary > 50000
AND age < 30;


SELECT
name AS Employee_Name,
salary AS Monthly_Salary
FROM employees;


SELECT
name,
salary,
CASE
    WHEN salary >= 60000 THEN 'High Salary'
    WHEN salary >= 50000 THEN 'Medium Salary'
    ELSE 'Low Salary'
END AS Salary_Category
FROM employees;