CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2) NOT NULL
);


ALTER table employees
ADD email VaRCHAR(100) UNIQUE;

ALTER table employees
ADD department VARCHAR(50) DEFAULT 'IT';

DROP Column email;