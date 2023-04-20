select p.name, f.name, c.name from products as p
inner join categories as c on c.id = p.id_categories
inner join providers as f on f.id = p.id_providers
where f.name = 'Sansul SA' and c.name = 'Imported'