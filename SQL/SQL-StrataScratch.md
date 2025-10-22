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

### 6.Lyft Driver Wages:
```SQL
select * from lyft_drivers
where yearly_salary<=30000 or yearly_salary>=70000;
```

### 7.Artist Appearance Count:
```SQL
select artist,count(artist) as 'n_occurences' from spotify_worldwide_daily_song_ranking
group by artist
order by n_occurences desc;
```

### 8.Top Ranked Songs:
```SQL
select trackname,count(*) as 'times_top1' from spotify_worldwide_daily_song_ranking
where position = '1'
group by trackname
order by times_top1 desc;
```

### 9.Number Of Bathrooms And Bedrooms:
```SQL
select city,property_type,avg(bathrooms) as 'n_bathrooms_avg',avg(bedrooms) as 'n_bedrooms_avg' from airbnb_search_details
group by city,property_type;
```

### 10.Workers by Department Since April:
```SQL
select department,count(*) as 'num_workers' from worker
where joining_date>='2014-04-01'
group by department
order by num_workers desc;
```
