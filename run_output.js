// ============================================================================
// NaziharDB - Interactive Console Output Runner
// Run this directly with: node run_output.js
// No npm packages required! Pure Node.js.
// ============================================================================

const departments = [
  { dept_id: 1, dept_name: 'Information Technology', creation_date: '2015-01-15', dept_location: 'Dhaka' },
  { dept_id: 2, dept_name: 'Human Resources', creation_date: '2016-03-20', dept_location: 'Dhaka' },
  { dept_id: 3, dept_name: 'Finance', creation_date: '2017-02-10', dept_location: 'Chittagong' },
  { dept_id: 4, dept_name: 'Marketing', creation_date: '2018-05-18', dept_location: 'Dhaka' },
  { dept_id: 5, dept_name: 'Administration', creation_date: '2019-01-25', dept_location: 'Rajshahi' },
  { dept_id: 6, dept_name: 'Research and Development', creation_date: '2020-04-12', dept_location: 'Dhaka' }
];

const employees = [
  { emp_id: 1,  emp_name: 'Abir Hasan',        designation: 'Software Engineer',         dateofbirth: '1992-05-14', salary: 65000.00, dept_id: 1 },
  { emp_id: 2,  emp_name: 'Nusrat Jahan',      designation: 'Senior Software Engineer',  dateofbirth: '1989-08-22', salary: 85000.00, dept_id: 1 },
  { emp_id: 3,  emp_name: 'Tanvir Ahmed',      designation: 'System Analyst',            dateofbirth: '1991-03-10', salary: 72000.00, dept_id: 1 },
  { emp_id: 4,  emp_name: 'Sakib Khan',        designation: 'Database Administrator',    dateofbirth: '1988-01-15', salary: 78000.00, dept_id: 1 },
  { emp_id: 5,  emp_name: 'Mim Akter',         designation: 'Software Engineer',         dateofbirth: '1995-04-20', salary: 55000.00, dept_id: 1 },
  { emp_id: 6,  emp_name: 'Fahim Rahman',      designation: 'Network Engineer',          dateofbirth: '1993-09-19', salary: 60000.00, dept_id: 1 },
  { emp_id: 7,  emp_name: 'Rafiul Islam',      designation: 'Junior Developer',          dateofbirth: '1998-03-22', salary: 42000.00, dept_id: 1 },
  { emp_id: 8,  emp_name: 'Nusrat Sultana',    designation: 'HR Manager',                dateofbirth: '1987-06-12', salary: 75000.00, dept_id: 2 },
  { emp_id: 9,  emp_name: 'Jannatul Ferdous',  designation: 'HR Officer',                dateofbirth: '1993-06-30', salary: 48000.00, dept_id: 2 },
  { emp_id: 10, emp_name: 'Tania Akter',       designation: 'Recruitment Officer',       dateofbirth: '1995-10-17', salary: 45000.00, dept_id: 2 },
  { emp_id: 11, emp_name: 'Shamim Ahmed',      designation: 'HR Executive',              dateofbirth: '1996-08-11', salary: 40000.00, dept_id: 2 },
  { emp_id: 12, emp_name: 'Mehedi Hasan',      designation: 'Finance Manager',           dateofbirth: '1985-07-18', salary: 90000.00, dept_id: 3 },
  { emp_id: 13, emp_name: 'Ayesha Rahman',     designation: 'Senior Accountant',         dateofbirth: '1989-02-25', salary: 70000.00, dept_id: 3 },
  { emp_id: 14, emp_name: 'Rakib Hossain',     designation: 'Accountant',                dateofbirth: '1992-09-12', salary: 55000.00, dept_id: 3 },
  { emp_id: 15, emp_name: 'Sumaiya Islam',     designation: 'Financial Analyst',         dateofbirth: '1994-07-04', salary: 62000.00, dept_id: 3 },
  { emp_id: 16, emp_name: 'Imran Hossain',     designation: 'Junior Accountant',         dateofbirth: '1997-12-08', salary: 42000.00, dept_id: 3 },
  { emp_id: 17, emp_name: 'Sadia Rahman',      designation: 'Marketing Manager',         dateofbirth: '1988-11-05', salary: 80000.00, dept_id: 4 },
  { emp_id: 18, emp_name: 'Arif Rahman',       designation: 'Marketing Executive',       dateofbirth: '1992-05-23', salary: 52000.00, dept_id: 4 },
  { emp_id: 19, emp_name: 'Rima Chowdhury',    designation: 'Digital Marketing Officer', dateofbirth: '1994-11-29', salary: 48000.00, dept_id: 4 },
  { emp_id: 20, emp_name: 'Mahmudul Hasan',    designation: 'Sales Executive',           dateofbirth: '1991-03-16', salary: 45000.00, dept_id: 4 },
  { emp_id: 21, emp_name: 'Farhana Akter',     designation: 'Admin Manager',             dateofbirth: '1986-02-14', salary: 78000.00, dept_id: 5 },
  { emp_id: 22, emp_name: 'Morshed Alam',      designation: 'Administrative Officer',    dateofbirth: '1989-10-09', salary: 58000.00, dept_id: 5 },
  { emp_id: 23, emp_name: 'Sabrina Akter',     designation: 'Office Executive',          dateofbirth: '1993-12-21', salary: 45000.00, dept_id: 5 },
  { emp_id: 24, emp_name: 'Shakil Ahmed',      designation: 'Office Assistant',          dateofbirth: '1996-06-13', salary: 35000.00, dept_id: 5 },
  { emp_id: 25, emp_name: 'Priya Das',         designation: 'Administrative Officer',    dateofbirth: '1991-08-06', salary: 55000.00, dept_id: 5 },
  { emp_id: 26, emp_name: 'Afsana Yasmin',     designation: 'Research Manager',          dateofbirth: '1987-01-28', salary: 88000.00, dept_id: 6 },
  { emp_id: 27, emp_name: 'Nayeem Hasan',      designation: 'Research Scientist',        dateofbirth: '1990-09-26', salary: 75000.00, dept_id: 6 },
  { emp_id: 28, emp_name: 'Tasnim Jahan',      designation: 'Research Officer',          dateofbirth: '1993-05-31', salary: 60000.00, dept_id: 6 },
  { emp_id: 29, emp_name: 'Sohanur Rahman',    designation: 'Data Scientist',            dateofbirth: '1992-11-18', salary: 82000.00, dept_id: 6 },
  { emp_id: 30, emp_name: 'Sharmin Akter',     designation: 'Research Assistant',        dateofbirth: '1997-08-06', salary: 45000.00, dept_id: 6 }
];

const projects = [
  { project_id: 1,  project_name: 'Payroll Management System',       emp_id: 1,  project_manager: 2,  is_finished: 1 },
  { project_id: 2,  project_name: 'Network Infrastructure Upgrade',  emp_id: 6,  project_manager: 2,  is_finished: 0 },
  { project_id: 3,  project_name: 'Database Migration Project',      emp_id: 4,  project_manager: 3,  is_finished: 0 },
  { project_id: 4,  project_name: 'Recruitment Management System',   emp_id: 9,  project_manager: 8,  is_finished: 1 },
  { project_id: 5,  project_name: 'Employee Training Portal',        emp_id: 10, project_manager: 8,  is_finished: 0 },
  { project_id: 6,  project_name: 'Financial Reporting System',      emp_id: 12, project_manager: 12, is_finished: 1 },
  { project_id: 7,  project_name: 'Budget Management System',        emp_id: 13, project_manager: 12, is_finished: 0 },
  { project_id: 8,  project_name: 'Digital Marketing Campaign',      emp_id: 17, project_manager: 16, is_finished: 1 },
  { project_id: 9,  project_name: 'Company Website Redesign',        emp_id: 18, project_manager: 16, is_finished: 0 },
  { project_id: 10, project_name: 'Office Automation System',        emp_id: 21, project_manager: 21, is_finished: 1 },
  { project_id: 11, project_name: 'Research Data Management System', emp_id: 26, project_manager: 26, is_finished: 0 },
  { project_id: 12, project_name: 'AI Research Project',             emp_id: 27, project_manager: 26, is_finished: 0 }
];

const getDept = (id) => departments.find(d => d.dept_id === id);
const getEmp = (id) => employees.find(e => e.emp_id === id);

const queries = [
  {
    num: 1,
    title: "Departments located in Dhaka, ordered by department name",
    sql: "SELECT * FROM Departments WHERE dept_location = 'Dhaka' ORDER BY dept_name ASC;",
    exec: () => departments
      .filter(d => d.dept_location === 'Dhaka')
      .sort((a, b) => a.dept_name.localeCompare(b.dept_name))
  },
  {
    num: 2,
    title: "Employees with salary between 50,000 and 80,000",
    sql: "SELECT emp_name, designation, salary FROM Employees WHERE salary BETWEEN 50000 AND 80000 ORDER BY salary DESC;",
    exec: () => employees
      .filter(e => e.salary >= 50000 && e.salary <= 80000)
      .map(e => ({ emp_name: e.emp_name, designation: e.designation, salary: e.salary }))
      .sort((a, b) => b.salary - a.salary)
  },
  {
    num: 3,
    title: "Employees whose name starts with 'A' or contains 'Rahman'",
    sql: "SELECT * FROM Employees WHERE emp_name LIKE 'A%' OR emp_name LIKE '%Rahman%' ORDER BY emp_id ASC;",
    exec: () => employees
      .filter(e => e.emp_name.startsWith('A') || e.emp_name.includes('Rahman'))
      .sort((a, b) => a.emp_id - b.emp_id)
  },
  {
    num: 4,
    title: "Projects that are either completed or assigned to employee ID 1",
    sql: "SELECT * FROM Projects WHERE is_finished = 1 OR emp_id = 1 ORDER BY project_id ASC;",
    exec: () => projects
      .filter(p => p.is_finished === 1 || p.emp_id === 1)
      .sort((a, b) => a.project_id - b.project_id)
  },
  {
    num: 5,
    title: "5 highest-paid employees",
    sql: "SELECT * FROM Employees ORDER BY salary DESC LIMIT 5;",
    exec: () => [...employees].sort((a, b) => b.salary - a.salary).slice(0, 5)
  },
  {
    num: 6,
    title: "All unique locations from departments table",
    sql: "SELECT DISTINCT dept_location FROM Departments ORDER BY dept_location ASC;",
    exec: () => [...new Set(departments.map(d => d.dept_location))].sort().map(loc => ({ dept_location: loc }))
  },
  {
    num: 7,
    title: "3 most recently created departments",
    sql: "SELECT * FROM Departments ORDER BY creation_date DESC LIMIT 3;",
    exec: () => [...departments].sort((a, b) => b.creation_date.localeCompare(a.creation_date)).slice(0, 3)
  },
  {
    num: 8,
    title: "Total employees, total salary, average salary, highest & lowest salary",
    sql: "SELECT COUNT(*), SUM(salary), ROUND(AVG(salary),2), MAX(salary), MIN(salary) FROM Employees;",
    exec: () => {
      const total = employees.reduce((s, e) => s + e.salary, 0);
      const avg = Number((total / employees.length).toFixed(2));
      const max = Math.max(...employees.map(e => e.salary));
      const min = Math.min(...employees.map(e => e.salary));
      return [{
        total_employees: employees.length,
        total_salary: total,
        average_salary: avg,
        highest_salary: max,
        lowest_salary: min
      }];
    }
  },
  {
    num: 9,
    title: "Total number of completed and running projects separately",
    sql: "SELECT CASE WHEN is_finished=1 THEN 'Completed' ELSE 'Running' END, COUNT(*) FROM Projects GROUP BY is_finished;",
    exec: () => [
      { project_status: 'Completed', total_projects: projects.filter(p => p.is_finished === 1).length },
      { project_status: 'Running', total_projects: projects.filter(p => p.is_finished === 0).length }
    ]
  },
  {
    num: 10,
    title: "Each department's name, number of employees, and average salary",
    sql: "SELECT d.dept_name, COUNT(e.emp_id), ROUND(AVG(e.salary),2) FROM Departments d JOIN Employees e ON d.dept_id=e.dept_id GROUP BY d.dept_id, d.dept_name;",
    exec: () => departments.map(d => {
      const emps = employees.filter(e => e.dept_id === d.dept_id);
      const total = emps.reduce((s, e) => s + e.salary, 0);
      return {
        dept_name: d.dept_name,
        number_of_employees: emps.length,
        average_salary: emps.length ? Number((total / emps.length).toFixed(2)) : 0
      };
    })
  },
  {
    num: 11,
    title: "Departments having more than 4 employees",
    sql: "SELECT d.dept_name, COUNT(e.emp_id) FROM Departments d JOIN Employees e ON d.dept_id=e.dept_id GROUP BY d.dept_id, d.dept_name HAVING COUNT(e.emp_id) > 4;",
    exec: () => departments.map(d => ({
      dept_name: d.dept_name,
      number_of_employees: employees.filter(e => e.dept_id === d.dept_id).length
    })).filter(d => d.number_of_employees > 4)
  },
  {
    num: 12,
    title: "Departments whose total salary is greater than 300,000",
    sql: "SELECT d.dept_name, SUM(e.salary) FROM Departments d JOIN Employees e ON d.dept_id=e.dept_id GROUP BY d.dept_id, d.dept_name HAVING SUM(e.salary) > 300000;",
    exec: () => departments.map(d => ({
      dept_name: d.dept_name,
      total_salary: employees.filter(e => e.dept_id === d.dept_id).reduce((s, e) => s + e.salary, 0)
    })).filter(d => d.total_salary > 300000)
  },
  {
    num: 13,
    title: "Project managers managing more than 1 project",
    sql: "SELECT project_manager AS manager_emp_id, COUNT(*) FROM Projects GROUP BY project_manager HAVING COUNT(*) > 1;",
    exec: () => {
      const map = {};
      projects.forEach(p => map[p.project_manager] = (map[p.project_manager] || 0) + 1);
      return Object.entries(map)
        .filter(([_, count]) => count > 1)
        .map(([mgr, count]) => ({ manager_emp_id: Number(mgr), total_projects_managed: count }));
    }
  },
  {
    num: 14,
    title: "Employee name, designation, salary, and department name (INNER JOIN)",
    sql: "SELECT e.emp_name, e.designation, e.salary, d.dept_name FROM Employees e INNER JOIN Departments d ON e.dept_id=d.dept_id;",
    exec: () => employees.map(e => ({
      emp_name: e.emp_name,
      designation: e.designation,
      salary: e.salary,
      dept_name: getDept(e.dept_id)?.dept_name
    }))
  },
  {
    num: 15,
    title: "Project name, assigned employee name, and department name (INNER JOIN)",
    sql: "SELECT p.project_name, e.emp_name, d.dept_name FROM Projects p INNER JOIN Employees e ON p.emp_id=e.emp_id INNER JOIN Departments d ON e.dept_id=d.dept_id;",
    exec: () => projects.map(p => {
      const emp = getEmp(p.emp_id);
      return {
        project_name: p.project_name,
        assigned_employee_name: emp?.emp_name,
        dept_name: getDept(emp?.dept_id)?.dept_name
      };
    })
  },
  {
    num: 16,
    title: "Project name, assigned employee name, salary, dept name, status",
    sql: "SELECT p.project_name, e.emp_name, e.salary, d.dept_name, CASE WHEN p.is_finished=1 THEN 'Completed' ELSE 'Running' END FROM Projects p ...",
    exec: () => projects.map(p => {
      const emp = getEmp(p.emp_id);
      return {
        project_name: p.project_name,
        assigned_employee_name: emp?.emp_name,
        employee_salary: emp?.salary,
        dept_name: getDept(emp?.dept_id)?.dept_name,
        project_status: p.is_finished === 1 ? 'Completed' : 'Running'
      };
    })
  },
  {
    num: 17,
    title: "All employees and their project names (LEFT JOIN)",
    sql: "SELECT e.emp_name, p.project_name FROM Employees e LEFT JOIN Projects p ON e.emp_id=p.emp_id;",
    exec: () => employees.map(e => {
      const proj = projects.find(p => p.emp_id === e.emp_id);
      return { emp_name: e.emp_name, project_name: proj ? proj.project_name : null };
    })
  },
  {
    num: 18,
    title: "All departments and number of employees in each (LEFT JOIN)",
    sql: "SELECT d.dept_name, COUNT(e.emp_id) FROM Departments d LEFT JOIN Employees e ON d.dept_id=e.dept_id GROUP BY d.dept_id, d.dept_name;",
    exec: () => departments.map(d => ({
      dept_name: d.dept_name,
      number_of_employees: employees.filter(e => e.dept_id === d.dept_id).length
    }))
  },
  {
    num: 19,
    title: "Employees who are not assigned to any project",
    sql: "SELECT e.emp_id, e.emp_name, e.designation, e.salary FROM Employees e LEFT JOIN Projects p ON e.emp_id=p.emp_id WHERE p.project_id IS NULL;",
    exec: () => employees
      .filter(e => !projects.some(p => p.emp_id === e.emp_id))
      .map(e => ({ emp_id: e.emp_id, emp_name: e.emp_name, designation: e.designation, salary: e.salary }))
  },
  {
    num: 20,
    title: "Employee salary category using CASE (>=80k High, >=60k Medium, else Low)",
    sql: "SELECT emp_name, salary, CASE WHEN salary>=80000 THEN 'High' WHEN salary>=60000 THEN 'Medium' ELSE 'Low' END FROM Employees;",
    exec: () => employees.map(e => ({
      emp_name: e.emp_name,
      salary: e.salary,
      salary_category: e.salary >= 80000 ? 'High' : e.salary >= 60000 ? 'Medium' : 'Low'
    })).sort((a, b) => b.salary - a.salary)
  },
  {
    num: 21,
    title: "Project name and project status using CASE",
    sql: "SELECT project_name, CASE WHEN is_finished=1 THEN 'Completed' ELSE 'Running' END FROM Projects;",
    exec: () => projects.map(p => ({
      project_name: p.project_name,
      project_status: p.is_finished === 1 ? 'Completed' : 'Running'
    }))
  },
  {
    num: 22,
    title: "Employees whose salary is greater than the average salary of all employees",
    sql: "SELECT emp_id, emp_name, designation, salary FROM Employees WHERE salary > (SELECT AVG(salary) FROM Employees);",
    exec: () => {
      const avg = employees.reduce((s, e) => s + e.salary, 0) / employees.length;
      return employees
        .filter(e => e.salary > avg)
        .map(e => ({ emp_id: e.emp_id, emp_name: e.emp_name, designation: e.designation, salary: e.salary }))
        .sort((a, b) => b.salary - a.salary);
    }
  },
  {
    num: 23,
    title: "Highest-paid employee from each department along with department name",
    sql: "SELECT e.emp_name, e.salary, d.dept_name FROM Employees e JOIN Departments d ON e.dept_id=d.dept_id WHERE (e.dept_id, e.salary) IN (...);",
    exec: () => {
      return departments.map(d => {
        const emps = employees.filter(e => e.dept_id === d.dept_id);
        const top = emps.reduce((max, cur) => cur.salary > max.salary ? cur : max, emps[0]);
        return { emp_name: top.emp_name, salary: top.salary, dept_name: d.dept_name };
      }).sort((a, b) => b.salary - a.salary);
    }
  }
];

// CLI arguments support: e.g. "node run_output.js 5" to see just Query 5, or all
const arg = process.argv[2];

if (arg && !isNaN(arg)) {
  const qNum = parseInt(arg, 10);
  const q = queries.find(item => item.num === qNum);
  if (!q) {
    console.log(`Query ${qNum} not found. Available queries: 1 to 23.`);
    process.exit(1);
  }
  console.log(`\n================================================================================`);
  console.log(`  QUERY ${q.num}: ${q.title}`);
  console.log(`================================================================================`);
  console.log(`SQL: ${q.sql}\n`);
  console.table(q.exec());
} else {
  console.log(`\n================================================================================`);
  console.log(`                 NAZIHARDB - ALL 23 SQL QUERY OUTPUT RESULTS                     `);
  console.log(`================================================================================`);
  console.log(`Tip: To view a single query, run: node run_output.js <query_number> (e.g. node run_output.js 8)\n`);
  
  queries.forEach(q => {
    console.log(`\n--------------------------------------------------------------------------------`);
    console.log(`[QUERY ${q.num}] ${q.title}`);
    console.log(`SQL: ${q.sql}`);
    console.log(`--------------------------------------------------------------------------------`);
    console.table(q.exec());
  });
}
