-- 1378. Replace Employee ID With The Unique Identifier
SELECT EmployeeUNI.unique_id, Employees.Name
FROM Employees
LEFT JOIN EmployeeUNI ON EmployeeUni.id = Employees.id