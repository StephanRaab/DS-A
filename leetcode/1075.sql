-- 1075. Project Employees I

SELECT Project.project_id, ROUND(AVG(experience_years),2) as average_years
FROM PROJECT LEFT JOIN EMPLOYEE ON Project.employee_id = Employee.employee_id
GROUP BY project_id