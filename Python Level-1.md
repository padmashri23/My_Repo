### 1.Returning the string using \n and \t:
```python
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
```
![image](https://github.com/user-attachments/assets/1fe91ac7-1dc1-490c-8a13-bde3e7bc0559)

### 2.python program to find eligible for voting or not:
```python
age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible!")
else:
    print("You are not eligible!")
```
![image](https://github.com/user-attachments/assets/069a959b-d787-4c98-80cc-7a422b758166)

### 3.program to check whether a number entered by user is even or odd:
```python
num=int(input("Enter the number:"))
if num%2==0:
    print("even")
else:
    print("odd")
```

![image](https://github.com/user-attachments/assets/e0d67334-ecce-4567-b889-37219737b191)

### 4.program to check whether a number is divisible by 7 or not:
```python
num=int(input())
if num%7==0:
    print("Yes!divisible")
else:
    print("not divisible")
```

![image](https://github.com/user-attachments/assets/8cb50135-d491-4521-a7ee-a37932f57868)

### 5.program to display "Hello" if num is multiple by 5 or else "Bye":
```python
num=int(input("Enter the number:"))
if num%5==0:
    print("Hello")
else:
    print("Bye")
```
![image](https://github.com/user-attachments/assets/92e67691-0b0c-454b-8a6b-e44d35b9b602)

### 6.program to dispaly last digit of a number:
```python
num=int(input("enter the number:"))
ld=num%10
print("The last digit is:"+str(ld))
```
![image](https://github.com/user-attachments/assets/de42e677-ccfd-4789-8ab0-2b0b7a34aa0a)
### 7.program to check whether the last digit of a number is divisible by 3 or not
```python
num=int(input("Enter the number:"))
ld=num%3
if num%3==0:
    print("yes!")
else:
    print("no!")
```
### Another method:
```python
num=int(input("Enter the number:"))
ld=num%10
if ld in [3,6,9,0]:
    print("Yes!")
else:
    print("no!")
```
![image](https://github.com/user-attachments/assets/135ecd89-2f1a-47a1-b1bb-b29f898e8fa2)
### 8.Program to accept percentage from the user and dispaly the grade:
```python
marks=int(input("Enter the marks:"))
if marks>90 and marks<=100:
    print("Grade A")
if marks>80 and marks<=90:
    print("Grade B")
if marks>=60 and marks<=80:
    print("Grade C")
if marks<60 and marks>=0:
    print("Grade D")
if marks<0 or marks>100:
    print("Enter marks between 0 to 100")
```
![image](https://github.com/user-attachments/assets/d75f8b0a-eb80-421d-8428-6aa273c7d2cf)
### 9.program to calculate the tax of the bike by the give cost price
```python
tax=0
price=int(input("Enter the Cost price(in Rs):"))
if price>100000:
    tax=15/100*price
    print("The tax is:"+str(round(tax,2)))
if price>50000 and price<=100000:
    tax=10/100*price
    print("The tax is:"+str(round(tax,2)))
if price<=50000 and price>0:
    tax=5/100*price
    print("The tax is:"+str(round(tax,2)))
if price<=0:
    print("Invalid amount")
```
![image](https://github.com/user-attachments/assets/92efeffd-1492-4144-b934-0668732e3cf3)
### 10.Program to check whether an year is leap year or not:
```python
year=int(input('Enter the year:'))
if year%100==0:
    if year%400==0:
        print("It is a leap year!")
    else:
        print("It is not a leap year!")
else:
    if year%4==0:
        print("It is a leap year!")
    else:
        print("It is not a leap year!")
```
![image](https://github.com/user-attachments/assets/1e3bffe2-49be-478c-bf37-2277ff46ce61)
### 11.Program to accept a number from 1 t0 7 and display the name of the day
```python
num=int(input("Please enter a number between 1 to 7:"))
if num==1:
    print("Sunday")
elif num==2:
    print("Monday")
elif num==3:
    print("Tuesday")
elif num==4:
    print("Wednesday")
elif num==5:
    print("Thursday")
elif num==6:
    print("Friday")
elif num==7:
    print("Saturday")
else:
    print("Invalid number!")
```
![image](https://github.com/user-attachments/assets/5b73092d-1511-4ac8-b786-46d0c910eddc)
### 12.Program to accept a number from 1 to 12 to display the month and number of days in the month:
```python
num=int(input("Enter the number:"))
if num==2:
    year=int(input("Enter the year:"))
    if year%100==0:
        if year%400==0:
            print("February,29 Days")
        else:
            print("February,28 Days")
    else:
        if year%4==0:
            print("February,29 Days")
        else:
            print("February,28 Days")
elif num==1:
    print("January,31 Days")
elif num==3:
    print("March,31 Days")
elif num==4:
    print("April,30 Days")
elif num==5:
    print("May,31 Days")
elif num==6:
    print("June,30 Days")
elif num==7:
    print("July,31 Days")
elif num==8:
    print("August,31 Days")
elif num==9:
    print("September,30 Days")
elif num==10:
    print("October,31 Days")
elif num==11:
    print("November,30 Days")
elif num==12:
    print("December,31 Days")
else:
    print("Invalid number!")
```
![image](https://github.com/user-attachments/assets/7890b646-e49f-4f1d-b56c-99101006baf3)
### 13.Accept city from the user and display monument of that city:
```python
city=input("Enter the city name:")
if city.lower()=="delhi":
    print("Red Fort")
elif city.lower()=="agra":
    print("Taj Mahal")
elif city.lower()=="jaipur":
    print("Jal Mahal")
else:
    print("Enter the valid city name")
```
![image](https://github.com/user-attachments/assets/406a33eb-e470-43fc-8bf7-fdf8f9f5bf52)
### 14.print "Hello" if the given number is greater than 5 and lesser than or equal to 10:
```python
num=int(input("Enter the number:"))
if num>5 and num<=10:
    print("Hello")
else:
    print("Bye")
```
![image](https://github.com/user-attachments/assets/5e877285-6d64-41c1-a16a-f9ba2101cc83)
### 15.program to check whether a person is senior citizen or not-senior citizen:>=60:
```python
age=int(input('Enter the age:'))
if age>=60:
    print("Senior citizen!")
else:
    print("Not a senior citizen!")
```
![image](https://github.com/user-attachments/assets/782866bb-3dd6-413b-9020-5425e0c95f35)
### 16.Program to check whether a number is 3 digit or not and its middle number:
```python
num=input("Enter the number:")
l=len(num)
if l!=3:
    print("The entered number is not a three digit number!")
else:
    print("It is a three digit number!")
    print("The middle number is:"+str(int(num)%100//10))
```
![image](https://github.com/user-attachments/assets/daff9c98-8b25-44d1-85d3-f3724adc43c2)
### 17.Program to find the lowest number out of two number:
```python
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
if num1>num2:
    print("Lowest number:"+str(num2))
else:
    print("Lowest number:"+str(num1))
```
![image](https://github.com/user-attachments/assets/ae2543df-d4f5-4936-90a0-e4389cce74e5)

### 18.Program to find the largest number out of two number:
```python
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
if num1>num2:
    print("Greatest number:"+str(num1))
else:
    print("Greatest number:"+str(num2))
```
![image](https://github.com/user-attachments/assets/eba9d39e-716a-441c-8fba-0809437491a5)
### 19.Program to check positive or negative number:
```python
num=int(input())
if num>0:
    print("Positive number")
else:
    print("negative number")
```
![image](https://github.com/user-attachments/assets/468bada3-f232-4219-bea7-32b9d795c238)
### 20.Program to chech a number is divisible by 2 or 3 or by both
```python
num=int(input("Enter the number:"))
if num%2==0 and num%3==0:
    print("The number is divisible by both 2 and 3")
elif num%2==0:
    print("The number is divisible by 2")
elif num%3==0:
    print("The number is diviisible by 3")
else:
    print("The number is not divisible by both 2 and 3")
```
![image](https://github.com/user-attachments/assets/26145d4c-bd83-4ab0-bc5d-c025b1f70e4f)
### 21.Program to find the largest of 3 numbers:
```python
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
num3=int(input("Enter the number3:"))
if num1>num2 and num1>num3:
    print("greatest number is:"+str(num1))
elif num2>num1 and num2>num3:
    print("greatest number is:"+str(num2))
elif num3>num1 and num3>num2:
    print("greatest number is:"+str(num3))
elif num1==num2==num3:
    print("All numbers are eqaul and the greatest number is:"+str(num1))
elif num1==num2:
    print("Two numbers are equal and the greatest number is:"+str(num1))
elif num2==num3:
    print("Two numbers are equal and the greatest number is:"+str(num2))
elif num1==num3:
    print("Two numbers are equal and the greatest number is:"+str(num1))
```
![image](https://github.com/user-attachments/assets/db0cf3e1-51d4-4a09-8b0e-2ecac3c0b1ab)
### 22.Grade Calculator:
```python
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
add=num1+num2+num3+num4+num5
div=int(add/5)
if div>=91 and div<=100:
    print((div),"A")
elif div>=81 and div<=90:
    print((div),"B")
elif div>=71 and div<=80:
    print((div),"C")
elif div>=61 and div<=70:
    print((div),"D")
elif div>=51 and div<=60:
    print((div),"F")
```
![image](https://github.com/user-attachments/assets/9233a7c4-e5b0-4d3b-9a08-8edd5e8222fd)
### 23.Fitness tracking application:
```python
km=int(input())
mul=km*0.621371
print(round(mul,3))
```
![image](https://github.com/user-attachments/assets/9e8c4519-04b5-49ea-a92a-1e125a8355bd)
### 24.The Perfect Gift Price:
```python
num1,num2,num3=map(int,input().split())
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)
```
![image](https://github.com/user-attachments/assets/5109e4c9-c36d-447e-bedb-d967878bfa9c)
### 25.Python Calculator:
```python
num1=int(input())
num2=int(input())
char=input()
if char=="+":
    print(int(num1+num2))
elif char=="-":
    print(int(num1-num2))
elif char=="*":
    print(int(num1*num2))
elif char=="/":
    if num2!=0:
        print(int(num1/num2))
    else:
        print("the number is not divisible by 0")
elif char=="%":
    print(int(num1%num2))
else:
    print("Invalid Operator")
```
![image](https://github.com/user-attachments/assets/4c24f37c-b433-4135-997d-98f5fe5b85b7)
### 26.Simple Interest Program:
```python
p=int(input())
n=float(input())
r=float(input())
SI=(p*n*r)/100
print(SI)
```
![image](https://github.com/user-attachments/assets/a4213fa8-7fd3-4cb4-932b-3a534edef2f7)
### 27.Promotion Program:
```python
num=int(input())
if num>0 and num<=4:
    print("AP I")
elif num>0 and num<=7:
    print("AP II")
elif num>0 and num<=10:
    print("AP III")
elif num>0 and num<=13:
    print("ASP")
elif num>0 and num<=20:
    print("Professor")
elif num>0 and num>20:
    print("Head")
```
![image](https://github.com/user-attachments/assets/d1b8dc5e-8897-4048-abb5-6861ea7324a3)
### 28.Temperature Conversion:
```python
temp=int(input())
char=input()
F=(9/5*temp)+32
C=(temp-32)*5/9
if char=="C":
    print(str(round(F,1))+"F")
elif char=="F":
    print(str(round(C,1))+"C")
else:
    print("Invalid Character")
```
![image](https://github.com/user-attachments/assets/88eb57a8-e0b8-4562-9e01-253e36d49523)
### 29.Shapes Area Calculator:
```python
import math
shape=input()
if shape=="rectangle":
    l=float(input())
    w=float(input())
    area=l*w
    print(int(area))
elif shape=="circle":
    r=float(input())
    area=math.pi*r*r
    print(round(area,2))
elif shape=="triangle":
    b=float(input())
    h=float(input())
    area=1/2*b*h
    print(int(area))
elif shape=="parallelogram":
    b=float(input())
    h=float(input())
    area=b*h
    print(int(area))
elif shape=="trapezoid":
    b1=float(input())
    b2=float(input())
    h=float(input())
    area=1/2*(b1+b2)*h
    print(int(area))
else:
    print("Invalid shape")
```   
![image](https://github.com/user-attachments/assets/8ca41a11-b467-4794-bdb9-4a40702e9d88)
### 30.BMI Calculator:
```python
wt=int(input())
ht=int(input())
BMI=wt/float(ht*ht)*100
if BMI<18.5:
    print("UnderWeight")
elif BMI>=18.5 and BMI<25:
    print("Normal")
elif BMI>=25 and BMI<30:
    print("OverWeight")
else:
    print("Obese")
```
![image](https://github.com/user-attachments/assets/bbd64ff6-12df-4a13-9918-7e15337888cb)



























































    







