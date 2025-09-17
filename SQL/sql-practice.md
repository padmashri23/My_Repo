
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
