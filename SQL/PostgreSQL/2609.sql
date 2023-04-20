select c.name, sum(p.amount) from categories as c
inner join products as p on p.id_categories = c.id
group by c.id