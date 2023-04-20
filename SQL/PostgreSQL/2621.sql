select p.name from products as p
inner join providers as f on f.id = p.id_providers
where p.amount > 10 and p.amount < 20 and f.name like 'P%'
