-- Write your PostgreSQL query statement below

    
    WITH ordered_salaries as (select salary, departmentId, row_number() OVER (partition by departmentId order by salary desc) as rn
    from (select distinct departmentId, salary from Employee) a )

    select d.name as Department, e.name as Employee, e.salary as Salary
    from Employee e
    left join Department d on d.id = e.departmentId
     join ordered_salaries os on os.departmentId = e.departmentId and os.salary = e.salary and os.rn between 1 and 3

