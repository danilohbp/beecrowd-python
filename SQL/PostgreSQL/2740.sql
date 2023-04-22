select
	lt."team"
from
	(
(
	select
		l."position",
		('Podium: ' || l."team") as "team"
	from
		league as l
	limit 3)
union all
(
select
	ld."position",
	('Demoted: ' || ld."team") as "team"
from
	league as ld
order by
	ld."position" desc
limit 2)

) lt
order by
	"position" asc