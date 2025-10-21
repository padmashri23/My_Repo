### 1. Top store for movie sales:
```SQL
select store,manager from sales_by_store
order by total_sales desc
limit 1;  
```

### 2.Top 5 shortest movies:
```SQL
select title from film
order by length asc   
limit 5;
```
