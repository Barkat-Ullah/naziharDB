-- ============================================================================
-- Project: NaziharDB - Views, Procedures, and Functions (Part D)
-- DBMS: PostgreSQL (v12+)
-- Script: 04_views_procedures_functions.sql
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. Create a view named VIEW_EmployeeProjectDetails
-- Displays employee ID, employee name, designation, salary, department name, 
-- project name, project manager name, and project completion status.
-- ----------------------------------------------------------------------------
CREATE OR REPLACE VIEW VIEW_EmployeeProjectDetails AS
SELECT 
    e.emp_id,
    e.emp_name,
    e.designation,
    e.salary,
    d.dept_name,
    p.project_name,
    pm.emp_name AS project_manager_name,
    CASE 
        WHEN p.is_finished = 1 THEN 'Completed'
        WHEN p.is_finished = 0 THEN 'Running'
        ELSE 'Unknown'
    END AS project_completion_status
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id
LEFT JOIN Projects p ON e.emp_id = p.emp_id
LEFT JOIN Employees pm ON p.project_manager = pm.emp_id;


-- ----------------------------------------------------------------------------
-- 2. Create a stored procedure named SP_AddEmployee
-- Accepts employee name, designation, date of birth, salary, and department ID 
-- as parameters and inserts a new employee record into the Employees table.
-- ----------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE SP_AddEmployee(
    p_emp_name VARCHAR(100),
    p_designation VARCHAR(100),
    p_dateofbirth DATE,
    p_salary NUMERIC(10, 2),
    p_dept_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Employees (emp_name, designation, dateofbirth, salary, dept_id)
    VALUES (p_emp_name, p_designation, p_dateofbirth, p_salary, p_dept_id);
END;
$$;


-- ----------------------------------------------------------------------------
-- 3. Create a stored procedure named SP_UpdateEmployeeSalary
-- Accepts an employee ID and a new salary and updates the employee's salary.
-- ----------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE SP_UpdateEmployeeSalary(
    p_emp_id INT,
    p_new_salary NUMERIC(10, 2)
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Employees
    SET salary = p_new_salary
    WHERE emp_id = p_emp_id;
END;
$$;


-- ----------------------------------------------------------------------------
-- 4. Create a scalar-valued function named FUN_GetEmployeeAnnualSalary
-- Accepts an employee ID and returns the employee's annual salary. 
-- ----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION FUN_GetEmployeeAnnualSalary(
    f_emp_id INT
)
RETURNS NUMERIC(10, 2)
LANGUAGE plpgsql
AS $$
DECLARE
    annual_salary NUMERIC(10, 2);
BEGIN
    SELECT salary * 12 INTO annual_salary
    FROM Employees
    WHERE emp_id = f_emp_id;
    
    RETURN annual_salary;
END;
$$;

-- Use the function in a query that displays employee name, department name, 
-- project name, and annual salary.
-- (This is just a SELECT query using the function as requested)
/*
SELECT 
    e.emp_name,
    d.dept_name,
    p.project_name,
    FUN_GetEmployeeAnnualSalary(e.emp_id) AS annual_salary
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id
LEFT JOIN Projects p ON e.emp_id = p.emp_id;
*/


-- ----------------------------------------------------------------------------
-- 5. Create a table-valued function named FUN_GetEmployeesByDepartment
-- Accepts a department ID and returns all employees belonging to that department.
-- ----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION FUN_GetEmployeesByDepartment(
    f_dept_id INT
)
RETURNS SETOF Employees
LANGUAGE sql
AS $$
    SELECT *
    FROM Employees
    WHERE dept_id = f_dept_id;
$$;
