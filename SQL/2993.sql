select mode() WITHIN GROUP (ORDER BY vt.amount) 
as "most_frequent_value" from value_table vt