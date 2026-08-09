SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;

SELECT department, MAX(salary) AS highest_salary
FROM employees
GROUP BY department;

SELECT department, MIN(salary) AS lowest_salary
FROM employees
GROUP BY department;

SELECT 
    department,
    COUNT(*) AS total_employees,
    AVG(salary) AS average_salary,
    SUM(salary) AS total_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM employees
GROUP BY department;
