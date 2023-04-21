select l."name" as "name", l.customers_number as "customers_number"
from lawyers as l where l.customers_number = 
(select max(l2.customers_number) from lawyers l2)

union all

select l."name" as "name", l.customers_number as "customers_number"
from lawyers as l where l.customers_number = 
(select min(l2.customers_number) from lawyers l2)

union all

select 'Average' as "name", cast(avg(l.customers_number) as Integer) 
as "customers_number" from lawyers as l