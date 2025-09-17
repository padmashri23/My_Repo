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


