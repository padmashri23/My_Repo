### 1)All Products:
```SQL
select * from Products;
```
<img width="888" height="724" alt="image" src="https://github.com/user-attachments/assets/b21c0877-2795-497d-bc8d-a2734011666d" />

### 2)High Price of Products:
```SQL
select product_name,category from Products
where price > 100;
```
<img width="906" height="221" alt="image" src="https://github.com/user-attachments/assets/877a5971-9bbb-4b06-90f6-6ba6a71cb628" />
<img width="416" height="339" alt="image" src="https://github.com/user-attachments/assets/f95fb6a2-7905-4d0b-9c18-26992c45794d" />

### 3)Average Salary:
```SQL
select avg(salary) as 'avg_salary' from Works;
```
<img width="311" height="225" alt="image" src="https://github.com/user-attachments/assets/9bbc722c-9926-4f1a-bc56-80fb56e5b2cf" />

### 4)Locate People:
```SQL
select department_name,location from departments
where location like 'S%';
```
<img width="546" height="281" alt="image" src="https://github.com/user-attachments/assets/2ac6e9fe-32b1-454f-a31a-61f4ea17b3e3" />

### 5)Distinct Companies:
```SQL
select distinct company_name from Works;
```
<img width="237" height="330" alt="image" src="https://github.com/user-attachments/assets/92a3458d-ddfb-4f7e-a9fd-8c51e54216db" />

