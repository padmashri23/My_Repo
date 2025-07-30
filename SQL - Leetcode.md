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
