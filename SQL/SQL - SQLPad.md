### 1. Top store for movie sales:
```SQL
select store,manager from sales_by_store
order by total_sales desc
limit 1;
```
