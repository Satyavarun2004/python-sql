SELECT emp_id, name, salary
FROM employees
WHERE emp_id = 101;


START TRANSACTION;

UPDATE employees
SET salary = salary + 10000
WHERE emp_id = 101;

SELECT emp_id, name, salary
FROM employees
WHERE emp_id = 101;

ROLLBACK;

SELECT emp_id, name, salary
FROM employees
WHERE emp_id = 101;


START TRANSACTION;

UPDATE employees
SET salary = salary + 5000
WHERE emp_id = 101;

SAVEPOINT first_update;

UPDATE employees
SET salary = salary + 5000
WHERE emp_id = 102;

ROLLBACK TO first_update;

COMMIT;