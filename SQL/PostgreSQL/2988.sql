select
	t.name,
	count(m.id) as "matches",
	(
	select
		count(m2.id)
	from
		matches as m2
	where
		(t.id = m2.team_1
			and m2.team_1_goals > m2.team_2_goals)
		or (t.id = m2.team_2
			and m2.team_2_goals > m2.team_1_goals)
) as "victories",
	(
	select
		count(m2.id)
	from
		matches as m2
	where
		(t.id = m2.team_1
			and m2.team_1_goals < m2.team_2_goals)
		or (t.id = m2.team_2
			and m2.team_2_goals < m2.team_1_goals)
)
as "defeats",
	(
	select
		count(m2.id)
	from
		matches as m2
	where
		(t.id = m2.team_1
			and m2.team_1_goals = m2.team_2_goals)
		or (t.id = m2.team_2
			and m2.team_2_goals = m2.team_1_goals)
)
as "draws",
		(
(
		select
			count(m2.id)
		from
			matches as m2
		where
			(t.id = m2.team_1
				and m2.team_1_goals > m2.team_2_goals)
			or (t.id = m2.team_2
				and m2.team_2_goals > m2.team_1_goals)
) * 3
+
(
		select
			count(m2.id)
		from
			matches as m2
		where
			(t.id = m2.team_1
				and m2.team_1_goals = m2.team_2_goals)
			or (t.id = m2.team_2
				and m2.team_2_goals = m2.team_1_goals)
)
) as "score"
from
	matches m
inner join teams t on
	t.id = m.team_1
	or t.id = m.team_2
group by
	t.id 
order by "score" desc, "name" asc