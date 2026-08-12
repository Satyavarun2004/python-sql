CREATE VIEW high_salary_employees AS
SELECT
    emp_id,
    name,
    department_id,
    salary
FROM employees
WHERE salary > 50000;


SELECT *
FROM high_salary_employees;


SHOW CREATE VIEW high_salary_employees;


CREATE TABLE salary_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


DELIMITER //

CREATE TRIGGER salary_change_log
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF OLD.salary <> NEW.salary THEN
        INSERT INTO salary_log
        (emp_id, old_salary, new_salary)
        VALUES
        (OLD.emp_id, OLD.salary, NEW.salary);
    END IF;
END //

DELIMITER ;


SELECT *
FROM employees
WHERE emp_id = 101;


UPDATE employees
SET salary = 55000
WHERE emp_id = 101;


