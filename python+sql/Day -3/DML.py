CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2) NOT NULL
);

INSERT INTO employees
(emp_id, name, age, department, salary)
VALUES
(101, 'Varun', 22, 'IT', 50000),
(102, 'Rahul', 25, 'HR', 45000),
(103, 'Priya', 26, 'Finance', 60000),
(104, 'Amit', 28, 'Sales', 55000),
(105, 'Neha', 24, NULL, 47000),
(106, 'Kiran', 27, 'IT', 62000),
(107, 'Anjali', 23, 'HR', 43000),
(108, 'Ravi', 29, 'Sales', 58000),
(109, 'Deepa', 30, NULL, 65000),
(110, 'Arjun', 26, 'Finance', 54000);

SELECT * FROM employees;


UPDATE employees
SET salary = salary + 5000
WHERE department = 'IT';


SELECT *
FROM employees
WHERE department = 'IT';

DELETE FROM employees
WHERE department IS NULL;

SELECT * FROM employees;