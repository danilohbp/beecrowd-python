select p.name, f.name, p.price from products as p
inner join categories as c on c.id = p.id_categories 
inner join providers as f on f.id = p.id_providers
where p.price > 1000 and c.name = 'Super Luxury'