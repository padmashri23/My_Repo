
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

### 4.Show first name and last name of patients that weight within the range of 100 to 120 (inclusive):
```SQL
select first_name,last_name from patients
where weight between 100 and 120;
```

### 5.Update the patients table for the allergies column. If the patient's allergies is null then replace it with 'NKA':
```SQL
update patients
set allergies = 'NKA'
where allergies is null;
```

### 6.Show how many patients have a birth_date with 2010 as the birth year.:
```SQL
select count(birth_date) as 'total_patients' from patients
where year(birth_date) =  2010 ;
```

### 7.Show the first_name, last_name, and height of the patient with the greatest height.:
```SQL
select first_name,last_name,height from patients
order by height desc
limit 1;
```

### 8.Show all columns for patients who have one of the following patient_ids:1,45,534,879,1000
```SQL
select * from patients
where patient_id in (1,45,534,879,1000);
```

### 9.Show the total number of admissions:
```SQL
select count(*) as 'total_admissions' from admissions;
```

### 10.Show all the columns from admissions where the patient was admitted and discharged on the same day:
```SQL
select * from admissions
where admission_date = discharge_date;
```

### 11.Show the patient id and the total number of admissions for patient_id 579:
```SQL
select patient_id,count(patient_id) as 'total_admissions' from admissions
where patient_id = 579;
```

### 12)Based on the cities that our patients live in, show unique cities that are in province_id 'NS':
```SQL
select distinct city as 'unique_cities' from patients
where province_id = 'NS';
```

### 13)Write a query to find the first_name, last name and birth date of patients who has height greater than 160 and weight greater than 70:
```SQL
select first_name,last_name,birth_date from patients
where height > 160 and weight > 70;
```

### 14)Write a query to find list of patients first_name, last_name, and allergies where allergies are not null and are from the city of 'Hamilton':
```SQL
select first_name,last_name,allergies from patients
where allergies is not null and city = 'Hamilton';
```

### 15)Show unique birth years from patients and order them by ascending:
```SQL
select distinct year(birth_date) as 'birth_year' from patients
order by birth_year;
```

### 16)Show first and last name, allergies from patients which have allergies to either 'Penicillin' or 'Morphine'. Show results ordered ascending by allergies then by first_name then by last_name:
```SQL
select first_name,last_name,allergies from patients
where allergies = 'Penicillin' or allergies = 'Morphine'
order by allergies, first_name,last_name;
```

### 17)Show the difference between the largest weight and smallest weight for patients with the last name 'Maroni':
```SQL
select (max(weight) - min(weight)) as 'weight_delta' from patients
where last_name = 'Maroni';
```

### 18)Show the city and the total number of patients in the city.Order from most to least patients and then by city name ascending.
```SQL
select city,count(patient_id) as 'num_patients' from patients
group by city
order by num_patients desc , city asc;
```

### 19)Show all patient's first_name, last_name, and birth_date who were born in the 1970s decade. Sort the list starting from the earliest birth_date:
```SQL
select first_name,last_name,birth_date from patients
where year(birth_date) >= 1970 and year(birth_date) <= 1979
order by birth_date asc;
```

### 20)Show all columns for patient_id 542's most recent admission_date:
```SQL
select * from admissions
where patient_id = 542
order by admission_date desc
limit 1;
```

### 21)Show the category_name and description from the categories table sorted by category_name:
```SQL
select category_name,description from categories;
```

### 22)Show all the contact_name, address, city of all customers which are not from 'Germany', 'Mexico', 'Spain':
```SQL
select contact_name,address,city from customers
where country not in ('Germany' , 'Mexico' , 'Spain');
```

### 23)Show order_date, shipped_date, customer_id, Freight of all orders placed on 2018 Feb 26:
```SQL
select order_date,shipped_date,customer_id,freight from orders
where order_date = '2018-02-26';
```

### 24)Show the employee_id, order_id, customer_id, required_date, shipped_date from all orders shipped later than the required date:
```SQL
select employee_id,order_id,customer_id,required_date,shipped_date  
from orders
where shipped_date > required_date;
```

### 25)Show all the even numbered Order_id from the orders table:
```SQL
select order_id from orders
where order_id % 2 = 0;
```

### 26)Show the company_name, contact_name, fax number of all customers that has a fax number. (not null):
```SQL
select company_name,contact_name,fax from customers
where fax is not null;
```

### 27)Show the city, company_name, contact_name of all customers from cities which contains the letter 'L' in the city name, sorted by contact_name:
```SQL
select city,company_name,contact_name from customers
where city like '%l%'
order by contact_name asc;
```

### 28)Show the first_name, last_name. hire_date of the most recently hired employee.
```SQL
select first_name,last_name,hire_date from employees
order by hire_date desc
limit 1;
```

### 29)Show patient_id and first_name from patients where their first_name start and ends with 's' and is at least 6 characters long.:
```SQL
select patient_id,first_name from patients
where first_name like 's%' and first_name like '%s'
and Length(first_name) >= 6;
```

### 30)Display every patient's first_name.Order the list by the length of each name and then by alphabetically:
```SQL
select first_name from patients
order by length(first_name),first_name asc;
```

### 31)Show all allergies ordered by popularity. Remove NULL values from query:
```SQL
select allergies,count(allergies) as 'total_diagnosis' from patients
where allergies is not null
group by allergies
order by total_diagnosis desc;
```
