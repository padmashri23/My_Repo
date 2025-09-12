### 1)Revising the Select Query I:
```SQL
select * from City
where population > 100000 and CountryCode = 'USA';
```

### 2)Revising the Select Query II:
```SQL
select NAME from City
where POPULATION > 120000 and COUNTRYCODE = 'USA';
```

### 3)Select By ID:
```SQL
select * from City
where ID = '1661';
```

### 4)Japanese Cities' Attributes:
```SQL
select * from City
where COUNTRYCODE = 'JPN';
```

### 5)Japanese Cities' Names:
```SQL
select NAME from City
where COUNTRYCODE = 'JPN';
```

### 6)Weather Observation Station 1:
```SQL
select city,state from Station;
```

### 7)Weather Observation Station 3:
```SQL
select distinct city from station
where ID % 2 = 0;
```

### 8)Weather Observation Station 4:
```SQL
select count(CITY) - count(distinct city) from station;
```

### 9)Weather Observation Station 6:
```SQL
select distinct CITY from STATION
where CITY LIKE 'a%' or CITY LIKE 'e%' or  CITY LIKE 'i%' or
CITY LIKE 'o%' or CITY LIKE 'u%';
```

### 10)Weather Observation Station 7:
```SQL
select distinct CITY from STATION
where CITY like '%a' or CITY like '%e' or 
CITY like '%i' or 
CITY like '%o' or 
CITY like '%u'
```

### 11)Employee Names:
```SQL
select name from Employee
order by name asc;
```

### 12)Employee Salaries:
```SQL
select name from Employee
where months < 10 and salary > 2000;
```

### 13)Type of Triangle:
```SQL
select 
case when (A+B <= C) or (B+C <= A) or (C+A <= B) then 'Not A Triangle'
     when (A = B and B = C) then 'Equilateral'
     when (A = B) or (A = C) or (B = C) then 'Isosceles'
     else 'Scalene'
     end as 'Triangle_Type'
from TRIANGLES;
```

### 14)Revising Aggregations - The Count Function:
```SQL
select count(NAME) from CITY
where POPULATION > 100000;
```

### 15)Average Population:
```SQL
select floor(Avg(population)) from City;   
```
//FLOOR() → rounds down to the nearest integer.

### 16)Japan Population:
```SQL
select sum(population) from city
where COUNTRYCODE = 'JPN';
```

### 17)Population Density Difference:
```SQL
select max(population) - min(population) from City;
```

### 18)Select All:
```SQL
select * from CITY;
```

### 19)Weather Observation Station 14:
```SQL
select TRUNCATE (LAT_N,4) from STATION
where LAT_N < 137.2345
order by LAT_N desc
limit 1;
```
```SQL
select truncate (max(LAT_N),4) from STATION
where LAT_N < 137.2345;
```
```
