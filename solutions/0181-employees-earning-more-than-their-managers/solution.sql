select m.name as Employee from Employee e join Employee m on m.managerId=e.id where m.salary>e.salary;
