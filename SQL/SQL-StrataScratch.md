### 1.Churro Activity Date:
```SQL
select activity_date,pe_description from los_angeles_restaurant_health_inspections
where facility_name = 'STREET CHURROS' and score<95;
```

### 2.Most Profitable Financial Company:
```SQL
select company,continent from forbes_global_2010_2014
where sector = 'Financials' 
having max(profits);
```
