
### 1.Show first name, last name, and gender of patients whose gender is 'M':
```SQL
select first_name,last_name,gender from patients
wHere gender = 'M';
```

### 2.Show first name and last name of patients who does not have allergies. (null):
```SQL
select first_name,last_name from patients
where allergies is null;
```

### 3.Show first name of patients that start with the letter 'C':
```SQL
select first_name from patients
where first_name like 'c%';
```
