create employee_table(
    emp_id  INT primary key,
    name  CHAR(100),
    age  INT,
    department  CHAR(100),
    salary  INT not null
)

INSERT INTO employees VALUES
(101,'Varun',22,'IT',50000),
(102,'Rahul',24,'HR',45000),
(103,'Priya',26,'Finance',60000);


select * from employees;
