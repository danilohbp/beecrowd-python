select p.name, trunc((p.salary)/10, 2) as "salary" from people as p
where p.salary > 3000
