select
(
	select(
		select sum(o3.profit) as "lucro" from operations o3
		where o2.client_id = o3.client_id and o3."month" <= o2."month"
		having sum(o3.profit) >= c2.investment
	) as "t" from operations o2
	inner join clients c2 on c2.id = o2.client_id
	order by "t", o2.client_id
) as "teste" 
from operations o
inner join clients c on c.id = o.client_id
--order by "teste"
