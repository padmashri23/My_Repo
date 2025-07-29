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
