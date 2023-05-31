# Write your MySQL query statement below
select Department.name Department, Employee.name Employee, salary
from Employee
         left join Department on Employee.departmentId = Department.id
where (Employee.departmentId, salary) in (select departmentId, max(salary)
                                          from Employee
                                          group by departmentId)