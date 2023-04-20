select p.name, f.name from products as p
inner join providers as f on f.id = p.id_providers
inner join categories as c on c.id = p.id_categories
where p.id_categories = 6