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

### 3.Order Details:
```SQL
select c.first_name,o.order_date,o.order_details,o.total_order_cost from orders as o
left join customers as c on o.cust_id = c.id
where c.first_name in ('Jill','Eva')
order by o.cust_id asc ;
```

### 4.Number of violations:
```SQL
select year(inspection_date) as 'inspection_year',count(violation_id) as 'n_violations'
from sf_restaurant_health_violations
where business_name = 'Roxanne Cafe'
group by inspection_year
order by inspection_year;
```

### 5.MacBookPro User Event Count:
```SQL
select event_name,count(device) as 'event_count' from playbook_events
where device = 'macbook pro'
group by event_name
order by event_count desc;
```
