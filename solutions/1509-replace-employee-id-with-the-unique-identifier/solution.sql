select EmployeeUNI.unique_id,Employees.name from Employees left JOIN EmployeeUNI on Employees.id=EmployeeUNI.id
