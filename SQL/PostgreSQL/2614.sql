select c.name, r.rentals_date from customers as c
inner join rentals as r on r.id_customers = c.id 
where DATE_PART('MONTH',r.rentals_date) = '09'
