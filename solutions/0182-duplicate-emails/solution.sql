select distinct e.email as Email from Person p join Person e on p.email=e.email where e.id!=p.id;
