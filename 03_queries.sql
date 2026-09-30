-- ============================================================================
-- Project: NaziharDB - SQL Queries (Part C)
-- DBMS: PostgreSQL (v12+)
-- Script: 03_queries.sql
-- ============================================================================

-- ============================================================================
-- SECTION 1: Basic SELECT, WHERE, LIKE, IN, BETWEEN
-- ============================================================================

-- Query 1: Display all departments located in Dhaka, ordered by department name.
SELECT 
    dept_id,
    dept_name,
    creation_date,
    dept_location
FROM Departments
WHERE dept_location = 'Dhaka'
ORDER BY dept_name ASC;


-- Query 2: Display the name, designation, and salary of employees whose salary is between 50,000 and 80,000.
SELECT 
    emp_name,
    designation,
    salary
FROM Employees
WHERE salary BETWEEN 50000 AND 80000
ORDER BY salary DESC;


-- Query 3: Display all employees whose name starts with A or contains Rahman.
SELECT 
    emp_id,
    emp_name,
    designation,
    salary,
    dept_id
FROM Employees
WHERE emp_name LIKE 'A%' 
   OR emp_name LIKE '%Rahman%'
ORDER BY emp_id ASC;


-- Query 4: Display all projects that are either completed or assigned to employee ID 1.
SELECT 
    project_id,
    project_name,
    emp_id,
    project_manager,
    is_finished
FROM Projects
WHERE is_finished = 1 
   OR emp_id = 1
ORDER BY project_id ASC;


-- ============================================================================
-- SECTION 2: ORDER BY, LIMIT, DISTINCT
-- ============================================================================

-- Query 5: Display the 5 highest-paid employees.
SELECT 
    emp_id,
    emp_name,
    designation,
    salary,
    dept_id
FROM Employees
ORDER BY salary DESC
LIMIT 5;


-- Query 6: Display all unique locations from the departments table.
SELECT DISTINCT 
    dept_location
FROM Departments
ORDER BY dept_location ASC;


-- Query 7: Display the 3 most recently created departments.
SELECT 
    dept_id,
    dept_name,
    creation_date,
    dept_location
FROM Departments
ORDER BY creation_date DESC
LIMIT 3;


-- ============================================================================
-- SECTION 3: Aggregate Functions
-- ============================================================================

-- Query 8: Find the total number of employees, total salary, average salary, highest salary, and lowest salary.
SELECT 
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary,
    ROUND(AVG(salary), 2) AS average_salary,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM Employees;


-- Query 9: Find the total number of completed and running projects separately.
-- Approach A: Using GROUP BY and CASE mapping for clear categorization
SELECT 
    CASE 
        WHEN is_finished = 1 THEN 'Completed'
        WHEN is_finished = 0 THEN 'Running'
    END AS project_status,
    COUNT(*) AS total_projects
FROM Projects
GROUP BY is_finished
ORDER BY is_finished DESC;

-- Approach B: Conditional aggregation into individual summary columns
-- SELECT 
--     COUNT(*) FILTER (WHERE is_finished = 1) AS completed_projects,
--     COUNT(*) FILTER (WHERE is_finished = 0) AS running_projects
-- FROM Projects;


-- ============================================================================
-- SECTION 4: GROUP BY and HAVING
-- ============================================================================

-- Query 10: Display each department's name, number of employees, and average salary.
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS number_of_employees,
    ROUND(AVG(e.salary), 2) AS average_salary
FROM Departments d
JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
ORDER BY d.dept_id ASC;


-- Query 11: Display departments having more than 4 employees.
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS number_of_employees
FROM Departments d
JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING COUNT(e.emp_id) > 4
ORDER BY number_of_employees DESC;


-- Query 12: Display each department's name and total salary, but show only departments whose total salary is greater than 300,000.
SELECT 
    d.dept_name,
    SUM(e.salary) AS total_salary
FROM Departments d
JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING SUM(e.salary) > 300000
ORDER BY total_salary DESC;


-- Query 13: Display each project manager's employee ID and the number of projects they manage. Show only managers who manage more than one project.
SELECT 
    project_manager AS manager_emp_id,
    COUNT(*) AS total_projects_managed
FROM Projects
GROUP BY project_manager
HAVING COUNT(*) > 1
ORDER BY total_projects_managed DESC, project_manager ASC;


-- ============================================================================
-- SECTION 5: INNER JOIN
-- ============================================================================

-- Query 14: Display employee name, designation, salary, and department name.
SELECT 
    e.emp_name,
    e.designation,
    e.salary,
    d.dept_name
FROM Employees e
INNER JOIN Departments d ON e.dept_id = d.dept_id
ORDER BY e.emp_id ASC;


-- Query 15: Display project name, assigned employee name, and department name.
SELECT 
    p.project_name,
    e.emp_name AS assigned_employee_name,
    d.dept_name
FROM Projects p
INNER JOIN Employees e ON p.emp_id = e.emp_id
INNER JOIN Departments d ON e.dept_id = d.dept_id
ORDER BY p.project_id ASC;


-- Query 16: Display project name, assigned employee name, employee salary, department name, and project status.
SELECT 
    p.project_name,
    e.emp_name AS assigned_employee_name,
    e.salary AS employee_salary,
    d.dept_name,
    CASE 
        WHEN p.is_finished = 1 THEN 'Completed'
        WHEN p.is_finished = 0 THEN 'Running'
    END AS project_status
FROM Projects p
INNER JOIN Employees e ON p.emp_id = e.emp_id
INNER JOIN Departments d ON e.dept_id = d.dept_id
ORDER BY p.project_id ASC;


-- ============================================================================
-- SECTION 6: LEFT JOIN
-- ============================================================================

-- Query 17: Display all employees and their project names, including employees who are not assigned to any project.
SELECT 
    e.emp_name,
    p.project_name
FROM Employees e
LEFT JOIN Projects p ON e.emp_id = p.emp_id
ORDER BY e.emp_id ASC;


-- Query 18: Display all departments and the number of employees in each department, including departments with zero employees.
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS number_of_employees
FROM Departments d
LEFT JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
ORDER BY d.dept_id ASC;


-- Query 19: Display employees who are not assigned to any project.
SELECT 
    e.emp_id,
    e.emp_name,
    e.designation,
    e.salary
FROM Employees e
LEFT JOIN Projects p ON e.emp_id = p.emp_id
WHERE p.project_id IS NULL
ORDER BY e.emp_id ASC;


-- ============================================================================
-- SECTION 7: CASE
-- ============================================================================

-- Query 20: Display employee name, salary, and salary category using CASE:
-- Salary >= 80,000 -> High
-- Salary >= 60,000 -> Medium
-- Otherwise        -> Low
SELECT 
    emp_name,
    salary,
    CASE 
        WHEN salary >= 80000 THEN 'High'
        WHEN salary >= 60000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM Employees
ORDER BY salary DESC, emp_name ASC;


-- Query 21: Display project name and project status using CASE:
-- is_finished = 1 -> Completed
-- is_finished = 0 -> Running
SELECT 
    project_name,
    CASE 
        WHEN is_finished = 1 THEN 'Completed'
        WHEN is_finished = 0 THEN 'Running'
        ELSE 'Unknown'
    END AS project_status
FROM Projects
ORDER BY project_id ASC;


-- ============================================================================
-- SECTION 8: Subqueries
-- ============================================================================

-- Query 22: Display employees whose salary is greater than the average salary of all employees.
SELECT 
    emp_id,
    emp_name,
    designation,
    salary
FROM Employees
WHERE salary > (
    SELECT AVG(salary) 
    FROM Employees
)
ORDER BY salary DESC;


-- Query 23: Display the highest-paid employee from each department along with the department name.
-- Method 1: Using IN Subquery with Row-Level comparison (Standard Subquery)
SELECT 
    e.emp_name,
    e.salary,
    d.dept_name
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id
WHERE (e.dept_id, e.salary) IN (
    SELECT dept_id, MAX(salary)
    FROM Employees
    GROUP BY dept_id
)
ORDER BY e.salary DESC;

-- Method 2 (Alternative): Using Correlated Subquery
-- SELECT 
--     e.emp_name,
--     e.salary,
--     d.dept_name
-- FROM Employees e
-- JOIN Departments d ON e.dept_id = d.dept_id
-- WHERE e.salary = (
--     SELECT MAX(e2.salary)
--     FROM Employees e2
--     WHERE e2.dept_id = e.dept_id
-- )
-- ORDER BY e.salary DESC;
