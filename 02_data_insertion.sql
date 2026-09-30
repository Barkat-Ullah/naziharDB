-- ============================================================================
-- Project: NaziharDB - Data Insertion
-- DBMS: PostgreSQL (v12+)
-- Script: 02_data_insertion.sql
-- ============================================================================

-- Ensure target tables exist before inserting data

-- ============================================================================
-- 1. Insert Data into Departments Table (6 rows)
-- ============================================================================
INSERT INTO Departments (dept_id, dept_name, creation_date, dept_location) VALUES
(1, 'Information Technology', '2015-01-15', 'Dhaka'),
(2, 'Human Resources', '2016-03-20', 'Dhaka'),
(3, 'Finance', '2017-02-10', 'Chittagong'),
(4, 'Marketing', '2018-05-18', 'Dhaka'),
(5, 'Administration', '2019-01-25', 'Rajshahi'),
(6, 'Research and Development', '2020-04-12', 'Dhaka');

-- ============================================================================
-- 2. Insert Data into Employees Table (30 rows)
-- ============================================================================
INSERT INTO Employees (emp_id, emp_name, designation, dateofbirth, salary, dept_id) VALUES
(1,  'Abir Hasan',        'Software Engineer',         '1992-05-14', 65000.00, 1),
(2,  'Nusrat Jahan',      'Senior Software Engineer',  '1989-08-22', 85000.00, 1),
(3,  'Tanvir Ahmed',      'System Analyst',            '1991-03-10', 72000.00, 1),
(4,  'Sakib Khan',        'Database Administrator',    '1988-01-15', 78000.00, 1),
(5,  'Mim Akter',         'Software Engineer',         '1995-04-20', 55000.00, 1),
(6,  'Fahim Rahman',      'Network Engineer',          '1993-09-19', 60000.00, 1),
(7,  'Rafiul Islam',      'Junior Developer',          '1998-03-22', 42000.00, 1),
(8,  'Nusrat Sultana',    'HR Manager',                '1987-06-12', 75000.00, 2),
(9,  'Jannatul Ferdous',  'HR Officer',                '1993-06-30', 48000.00, 2),
(10, 'Tania Akter',       'Recruitment Officer',       '1995-10-17', 45000.00, 2),
(11, 'Shamim Ahmed',      'HR Executive',              '1996-08-11', 40000.00, 2),
(12, 'Mehedi Hasan',      'Finance Manager',           '1985-07-18', 90000.00, 3),
(13, 'Ayesha Rahman',     'Senior Accountant',         '1989-02-25', 70000.00, 3),
(14, 'Rakib Hossain',     'Accountant',                '1992-09-12', 55000.00, 3),
(15, 'Sumaiya Islam',     'Financial Analyst',         '1994-07-04', 62000.00, 3),
(16, 'Imran Hossain',     'Junior Accountant',         '1997-12-08', 42000.00, 3),
(17, 'Sadia Rahman',      'Marketing Manager',         '1988-11-05', 80000.00, 4),
(18, 'Arif Rahman',       'Marketing Executive',       '1992-05-23', 52000.00, 4),
(19, 'Rima Chowdhury',    'Digital Marketing Officer', '1994-11-29', 48000.00, 4),
(20, 'Mahmudul Hasan',    'Sales Executive',           '1991-03-16', 45000.00, 4),
(21, 'Farhana Akter',     'Admin Manager',             '1986-02-14', 78000.00, 5),
(22, 'Morshed Alam',      'Administrative Officer',    '1989-10-09', 58000.00, 5),
(23, 'Sabrina Akter',     'Office Executive',          '1993-12-21', 45000.00, 5),
(24, 'Shakil Ahmed',      'Office Assistant',          '1996-06-13', 35000.00, 5),
(25, 'Priya Das',         'Administrative Officer',    '1991-08-06', 55000.00, 5),
(26, 'Afsana Yasmin',     'Research Manager',          '1987-01-28', 88000.00, 6),
(27, 'Nayeem Hasan',      'Research Scientist',        '1990-09-26', 75000.00, 6),
(28, 'Tasnim Jahan',      'Research Officer',          '1993-05-31', 60000.00, 6),
(29, 'Sohanur Rahman',    'Data Scientist',            '1992-11-18', 82000.00, 6),
(30, 'Sharmin Akter',     'Research Assistant',        '1997-08-06', 45000.00, 6);

-- ============================================================================
-- 3. Insert Data into Projects Table (12 rows)
-- ============================================================================
INSERT INTO Projects (project_id, project_name, emp_id, project_manager, is_finished) VALUES
(1,  'Payroll Management System',         1,  2,  1),
(2,  'Network Infrastructure Upgrade',    6,  2,  0),
(3,  'Database Migration Project',        4,  3,  0),
(4,  'Recruitment Management System',     9,  8,  1),
(5,  'Employee Training Portal',          10, 8,  0),
(6,  'Financial Reporting System',        12, 12, 1),
(7,  'Budget Management System',          13, 12, 0),
(8,  'Digital Marketing Campaign',        17, 16, 1),
(9,  'Company Website Redesign',          18, 16, 0),
(10, 'Office Automation System',          21, 21, 1),
(11, 'Research Data Management System',   26, 26, 0),
(12, 'AI Research Project',               27, 26, 0);

-- ============================================================================
-- 4. Synchronize PostgreSQL Auto-Increment Identity Sequences
-- Because explicit primary keys were inserted, we align the sequences so that
-- subsequent INSERTs without an ID will seamlessly continue from the next highest ID.
-- ============================================================================
SELECT setval(pg_get_serial_sequence('Departments', 'dept_id'), COALESCE(MAX(dept_id), 1)) FROM Departments;
SELECT setval(pg_get_serial_sequence('Employees', 'emp_id'), COALESCE(MAX(emp_id), 1)) FROM Employees;
SELECT setval(pg_get_serial_sequence('Projects', 'project_id'), COALESCE(MAX(project_id), 1)) FROM Projects;
