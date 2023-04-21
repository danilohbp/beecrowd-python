select l.name, CAST(EXTRACT('Day' from l.payday) as INTEGER) 
as "day" from loan as l
