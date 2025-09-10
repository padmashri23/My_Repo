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
