select e1.name Employee
from Employee e1
         left join Employee e2 on e1.managerId = e2.id
where e1.salary > e2.salary;

-- second variant
select e2.name Employee
from Employee e1
         left join Employee e2 on e1.id = e2.managerId
where e2.salary > e1.salary;