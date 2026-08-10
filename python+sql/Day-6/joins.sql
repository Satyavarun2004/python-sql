CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

INSERT INTO departments (department_id, department_name)
VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance'),
(4, 'Sales');

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department_id INT,
    salary DECIMAL(10,2) NOT NULL
);

INSERT INTO employees
(emp_id, name, age, department_id, salary)
VALUES
(101, 'Varun', 22, 1, 50000),
(102, 'Rahul', 25, 2, 45000),
(103, 'Priya', 26, 3, 60000),
(104, 'Amit', 28, 4, 55000),
(105, 'Neha', 24, NULL, 47000),
(106, 'Kiran', 27, 1, 62000);


SELECT
    e.emp_id,
    e.name,
    d.department_name,
    e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;

SELECT
    e.emp_id,
    e.name,
    d.department_name,
    e.salary
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;

