select p.name, length(p.name) as "length" from people as p
order by "length" desc