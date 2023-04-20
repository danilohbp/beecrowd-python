select regexp_replace(np.cpf,'(\d{3})(\d{3})(\d{3})(\d{2})', '\1.\2.\3-\4') 
as CPF from customers as c
inner join natural_person as np on np.id_customers = c.id