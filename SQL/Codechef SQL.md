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

### 6)List of Movies with Ratings:
```SQL   
select Movie_name from Cinema
where Rating > 7 and Rating < 9;
```
<img width="253" height="348" alt="image" src="https://github.com/user-attachments/assets/774f3079-74f8-4209-b229-299c24fe7f16" />

### 7)Salary of Employees:
```SQL
select employee_name,company,salary from Employees
where category = 'Full-Time'   
order by salary desc;
```
<img width="874" height="225" alt="image" src="https://github.com/user-attachments/assets/bda9f015-a7e6-47cc-a044-4ba179430e93" />
<img width="563" height="340" alt="image" src="https://github.com/user-attachments/assets/f96c8555-9929-4f7a-87d4-daa4e1b52323" />

### 8)Article views:
```SQL
select author_id,author_name,publication_name from Views
where view_count = 0
order by author_id ;   
```
<img width="887" height="246" alt="image" src="https://github.com/user-attachments/assets/cd51d7ff-6f8b-430c-aeec-fafa8fe58e78" />
<img width="612" height="302" alt="image" src="https://github.com/user-attachments/assets/aa3fa466-f54b-4a6d-a2a1-2cd075e4f030" />

### 9)Fiction Collection Size:
```SQL
select count(*) as 'fiction_count' from Books
where genre = 'Fiction';    
```
<img width="1908" height="752" alt="image" src="https://github.com/user-attachments/assets/a510a8bd-1f77-4532-a0f2-55dc2bcf884a" />
<img width="671" height="768" alt="image" src="https://github.com/user-attachments/assets/ac3cbbf4-37ce-4d81-b069-5970477b91eb" />  

