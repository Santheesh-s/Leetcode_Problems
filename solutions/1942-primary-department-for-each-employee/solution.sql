
-- select employee_id,department_id from Employee group by employee_id having count(*)=1 
-- select employee_id,department_id from Employee WHERE primary_flag="Y"

SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
GROUP BY employee_id
HAVING COUNT(*) = 1
UNION ALL
select employee_id,department_id from Employee group by employee_id having count(*)=1 
