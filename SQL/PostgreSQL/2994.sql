select d."name", round(sum((150.0 * a.hours) * (1 + (ws.bonus/100))), 1) as "salary" from attendances as a
inner join doctors as d on d.id = a.id_doctor
inner join work_shifts as ws on ws.id = a.id_work_shift
group by d."name", d.id 
order by "salary" desc