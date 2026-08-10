SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);


SELECT e1.name, e1.salary, e1.department_id
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);

WITH ranked_employees AS (
    SELECT
        name,
        department_id,
        salary,
        RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM employees
)
SELECT *
FROM ranked_employees;