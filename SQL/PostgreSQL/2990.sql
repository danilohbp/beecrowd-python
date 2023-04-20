select e.cpf, e.enome, d.dnome from empregados as e
inner join departamentos as d on d.dnumero = e.dnumero
where e.cpf not in (select t.cpf_emp from trabalha as t)
order by e.cpf
