### 1.Returning the string using \n and \t
```python
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
```
![image](https://github.com/user-attachments/assets/1fe91ac7-1dc1-490c-8a13-bde3e7bc0559)

### 2.python program to find eligible for voting or not
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

### 4.program to check whether a number is divisible by 7 or not
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

### 6.program to dispaly last digit of a number
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




















    







