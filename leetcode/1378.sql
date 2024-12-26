-- 1378. Replace Employee ID With The Unique Identifier
SELECT EmployeeUNI.unique_id, Employees.Name
FROM Employees
LEFT JOIN EmployeeUNI ON EmployeeUni.id = Employees.id

-- simplifying the names
SELECT eu.unique_id, e.Name
FROM Employees e
LEFT JOIN EmployeeUNI eu ON eu.id = e.id