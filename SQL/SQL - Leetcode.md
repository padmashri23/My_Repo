### Refer to Notes for Better Understanding:

### 1)595. Big Countries:

```SQL
Select name,population,area from World
where area>=3000000 or population>=25000000;
```

<img width="794" height="590" alt="image" src="https://github.com/user-attachments/assets/b92c6ac1-3c0a-4896-a9f9-7397f9b433d3" />

### 2)175. Combine Two Tables
```SQL
select p.firstName,p.lastName,a.city,a.state
from Person as p    
Left join Address as a on a.personId = p.personId;          
```
<img width="702" height="593" alt="image" src="https://github.com/user-attachments/assets/11467dd9-7604-4243-bc57-9db093ade5b9" />

### 3)182. Duplicate Emails:
```SQL
select email from Person  
group by email
Having count(id)>1;
```
<img width="591" height="538" alt="image" src="https://github.com/user-attachments/assets/4bcb215d-2b82-49dd-b569-805ef8d663b2" />

### 4)596. Classes With at Least 5 Students:
```SQL
select class from Courses
group by class
having count(student)>=5
```
<img width="747" height="700" alt="image" src="https://github.com/user-attachments/assets/1924893a-71fa-4522-a171-462fe59e1061" />

### 5)1729. Find Followers Count:
```SQL
select user_id,count(follower_id) as 'followers_count' from Followers
group by user_id
order by user_id;   
```
<img width="537" height="657" alt="image" src="https://github.com/user-attachments/assets/3456f44d-678e-4ac1-9a3c-761d830ba81e" />

### 6)890. The Latest Login in 2020:
```SQL
select user_id,max(time_stamp) as 'last_stamp' from Logins   
where year(time_stamp) = 2020
group by user_id;
```
<img width="448" height="618" alt="image" src="https://github.com/user-attachments/assets/ad105614-ac42-4723-a632-10ba66767eb1" />

### 7)584. Find Customer Referee:
```SQL
select name from Customer
where referee_id is null or referee_id != 2;
```
<img width="403" height="628" alt="image" src="https://github.com/user-attachments/assets/8fdbc665-2eda-45ad-bc84-6815cc459e49" />

### 8)511. Game Play Analysis I:
```SQL
select player_id,min(event_date) as 'first_login' from Activity
group by player_id
```
<img width="712" height="570" alt="image" src="https://github.com/user-attachments/assets/41202f42-c727-4f86-a58b-09798fb8e4dc" />

### 9)2356. Number of Unique Subjects Taught by Each Teacher:
```SQL
select teacher_id,count(distinct subject_id) as 'cnt' from Teacher
group by teacher_id;
```
<img width="499" height="658" alt="image" src="https://github.com/user-attachments/assets/b691b034-f788-4ee5-bdf0-81f8ef15aedc" />

### 10)1148. Article Views I:
```SQL
select author_id as 'id' from Views
where author_id = viewer_id   
group by author_id 
order by author_id;
```
<img width="745" height="613" alt="image" src="https://github.com/user-attachments/assets/9fab8fef-606d-4140-92b6-3db3998ac5c5" />

### 11)1757. Recyclable and Low Fat Products:
```SQL
select product_id from Products
where low_fats = 'Y' and recyclable = 'Y';   
```
<img width="830" height="577" alt="image" src="https://github.com/user-attachments/assets/cde43717-b865-43b9-817e-f65889dc80a9" />

### 12)620. Not Boring Movies:
```SQL
select id,movie,description,rating from Cinema
where id%2<>0 and description <> 'boring'
order by rating desc;
```
<img width="904" height="652" alt="image" src="https://github.com/user-attachments/assets/cdcfa29b-e3db-43e4-8a74-f47063486d87" />

### 13)610. Triangle Judgement:
```SQL
select x,y,z,
case when (x+y>z) and (y+z>x) and (z+x>y) then 'Yes'
else 'No'
end as 'triangle'
from Triangle;
```
<img width="500" height="471" alt="image" src="https://github.com/user-attachments/assets/da366f9d-2a1e-4715-9e6a-5a599751b186" />

### 14)1683. Invalid Tweets:
```SQL
select tweet_id  from Tweets    
where length(content) > 15;      
```
<img width="710" height="537" alt="image" src="https://github.com/user-attachments/assets/888aa5d2-b350-4cb2-a7a7-8b297a1fe36a" />

### 15)577. Employee Bonus:
```SQL
select e.name,b.bonus from employee as e
left join Bonus as b on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null;
```
<img width="653" height="703" alt="image" src="https://github.com/user-attachments/assets/dd3b3eeb-adb7-41bf-8454-e71b69f4fde0" />

### 16)1075. Project Employees I:
```SQL
select project_id ,round(avg(e.experience_years),2) as 'average_years' from Project as p
left join Employee as e on p.employee_id = e.employee_id
group by p.project_id;
```
<img width="756" height="682" alt="image" src="https://github.com/user-attachments/assets/16b3c59a-0704-4e91-a29f-7ce8265b9dfc" />

### 17)181. Employees Earning More Than Their Managers:
```SQL
select e.name as Employee from Employee as e
join Employee as m on e.managerId = m.id
where e.salary> m.salary;
```
<img width="831" height="551" alt="image" src="https://github.com/user-attachments/assets/bd67a955-7299-46ca-9aec-a4c167514ce0" />

### 18)183. Customers Who Never Order:
```SQL
select c.name as Customers from Customers as c
left join Orders as o on c.id = o.customerId
where o.customerId is null;
```
<img width="289" height="675" alt="image" src="https://github.com/user-attachments/assets/1b394b3a-e7b9-4361-9d5f-2c60b7b7382f" />

### 19)1068. Product Sales Analysis I:
```SQL
select p.product_name,s.year,s.price from Sales as s
left join Product as p on s.product_id = p.product_id;
```
<img width="804" height="652" alt="image" src="https://github.com/user-attachments/assets/8ae42461-8ab7-49a8-88e1-7a530a0ac828" />

### 20)196. Delete Duplicate Emails:
```SQL
Delete p1 from Person as p1
join Person as p2 on p1.email = p2.email
and p1.id>p2.id;
```
<img width="836" height="558" alt="image" src="https://github.com/user-attachments/assets/e46bd3ac-cff0-49cb-a7f1-00fd417f05d0" />


### 21)1407. Top Travellers:
```SQL
select u.name,coalesce(sum(r.distance),0) as 'travelled_distance'
from Users as u
left join Rides as r on u.id = r.user_id
group by r.user_id
order by travelled_distance desc,name;
```
<img width="835" height="769" alt="image" src="https://github.com/user-attachments/assets/a62d7fda-19a6-4e98-946b-c0bacc95b99e" />

### 22)1327. List the Products Ordered in a Period:
```SQL
select p.product_name,sum(o.unit) as 'unit' from Products as p
left join Orders as o on p.product_id = o.product_id
where o.order_date between '2020-02-01' and '2020-02-29'
group by o.product_id
having unit>=100;
```
<img width="797" height="770" alt="image" src="https://github.com/user-attachments/assets/7fc8d0ab-3ed6-4b5c-a00c-9d0b41071212" />

