select t.name, sum(m.id), (select sum(m.id) matches as m2
where m2.id = m.id and m2.team_1_goals > m2.team_2_goals), 
(select sum(m.id) matches as m2
where m2.id = m.id and m2.team_1_goals < m2.team_2_goals),
(select sum(m.id) matches as m2
where m2.id = m.id and m2.team_1_goals = m2.team_2_goals),

from teams as t
inner join matches as m on m.team_1 = t.id
group by t.id

