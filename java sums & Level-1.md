### 1.Implement stack using Stack class:
```java
import java.util.Stack;
class Main {
    public static void main(String[] args) {
        Stack<String> animals=new Stack<>();
        animals.push("Cat");
        animals.push("horse");
        animals.push("elephant");
        animals.push("dog");
        System.out.println("Stack: "+animals);
        animals.pop();
        System.out.println("Stack: "+animals);
        
    }
}
```
![image](https://github.com/user-attachments/assets/98de8989-3b73-4380-86f3-50249f553112)

###2.Using integers Stack implementation:
```java
import java.util.*;
public class Main
{
     public static void main(String[] args) {
         Stack<Integer> nums=new Stack<>();
         nums.push(10);
         nums.push(20);
         nums.push(30);
         System.out.println("Stack: " + nums);
         nums.pop();
         System.out.println("Stack: " + nums);
         nums.peek();
         nums.isEmpty();
         System.out.println("Stack: " + nums.peek());
         System.out.println("Stack: " + nums.isEmpty());
        
             
         }
}
```
![image](https://github.com/user-attachments/assets/dfbe1d80-2d58-4465-8c1e-508ee21e6271)

### 3.Recursion:
```java

public class Main
{
    	public static void printN(int n) {
    	    if(n==0)
    	    {
    	        return;
    	    }
    	    printN(n-1);
    	    	System.out.println(n);
    	}
	public static void main(String[] args) {
	printN(5);
	}
}
```

```java
public class Main
{
    	public static void printN(int n) {
    	    if(n==0)
    	    {
    	        return;
    	    }
    	    	System.out.println(n);
    	    	printN(n-1);
    	}
	public static void main(String[] args) {
	printN(5);
	}
}

```
![image](https://github.com/user-attachments/assets/0ccf8b81-3321-43e0-83c0-1e059e99464b)
![image](https://github.com/user-attachments/assets/957fe867-8c52-4e0f-b60c-6c3b4a8d22b7)


<h1 align="center"><u><strong>JAVA LEVEL - 1 </strong></u></h1>

### 1.The Grading Gauntlet:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        char grade = scanner.next().charAt(0);
        if(grade=='A')
        {
            System.out.println("Outstanding");
        }
        else if(grade=='B')
        {
            System.out.println("EXCELLENT");
        }
          else if(grade=='C')
        {
            System.out.println("GOOD");
        }
          else if(grade=='D')
        {
            System.out.println("JUST PASS");
        }
          else if(grade=='F')
        {
            System.out.println("FAIL");
        }
        else
        {
            System.out.println("Invalid");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/435682fe-b91b-48ca-ad97-a9e0e8e19148)
### 2.Student Grading Program:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int n1 = scanner.nextInt();
		int n2 = scanner.nextInt();
			int n3 = scanner.nextInt();
				int n4 = scanner.nextInt();
					int n5 = scanner.nextInt();
	int sum=n1+n2+n3+n4+n5;
	float per = (float) sum/5;
	System.out.printf("%.2f\n",per);
	if(per>=95)
	{
	    System.out.println("A");
	}
	else if(per>=85)
	{
	    System.out.println("B");
	}
	else if(per>=75)
	{
	    System.out.println("C");
	}
	else if(per>=65)
	{
	    System.out.println("D");
	}
	else if(per>=45)
	{
	    System.out.println("E");
	}
	else
	{
	    System.out.println("F");
	}
	scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/892bcecd-f18c-44b5-aa6e-f71b90f10821)
### 3.Month Days Counter:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n= scanner.nextInt();
		if (n==1){
		System.out.println("First");
	    System.out.println("31");}
	    else if (n==2){
	    System.out.println("First");
	    System.out.println("28 or 29");}
	    else if(n==3){
	    System.out.println("First");
	    System.out.println("31");}
	    else if(n==4){
	    System.out.println("Second");
	    System.out.println("30");}
	    else if(n==5){
	    System.out.println("Second");
	    System.out.println("31");}
	    else if(n==6){
	    System.out.println("Second");
	    System.out.println("30");}
	    else if(n==7){
	    System.out.println("Third");
	    System.out.println("31");}
	    else if(n==8){
	    System.out.println("Third");
	    System.out.println("31");}
	    else if(n==9){
	    System.out.println("Third");
	    System.out.println("30");}
	    else if(n==10){
	    System.out.println("Fourth");
	    System.out.println("31");}
	    else if(n==11){
	    System.out.println("Fourth");
	    System.out.println("30");}
	    else if(n==12){
	    System.out.println("Fourth");
	    System.out.println("31");}
	    else{
	    System.out.println("Invalid");}
	    scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/fc5e5d39-f5b4-4c94-8c9b-65f2534541ee)
### 4.Weekday Recognition:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n= scanner.nextInt();
		if (n==1){
		System.out.println("Monday");
	    System.out.println("Week day");}
	    else if (n==2){
	    System.out.println("Tuesday");
	    System.out.println("Week day");}
	    else if(n==3){
	    System.out.println("Wednesday");
	    System.out.println("Week day");}
	    else if(n==4){
	    System.out.println("Thursday");
	    System.out.println("Week day");}
	    else if(n==5){
	    System.out.println("Friday");
	    System.out.println("Week day");}
	    else if(n==6){
	    System.out.println("Saturday");
	    System.out.println("Holiday");}
	    else if(n==7){
	    System.out.println("Sunday");
	    System.out.println("Holiday");}
	    else{
	    System.out.println("Invalid input");}
	    scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/49a6b22b-a1bf-42b9-b553-ecfa2dfe6fe0)
### 5.Steps Calculator:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int steps = scanner.nextInt();
	int time = scanner.nextInt();
	float range = (float) steps/time;
	if (steps<5000)
	{
	    System.out.println("0");
	    System.out.printf("%.2f\n",range);
	}
    else if (steps>=5000 && steps<=9999)
	{
	    System.out.println("25");
	    System.out.printf("%.2f\n",range);
	}
    else if (steps>=10000 && steps<=14999)
	{
	    System.out.println("50");
	    System.out.printf("%.2f\n",range);
	}
	else if (steps>=15000)
	{
	    System.out.println("100");
	    System.out.printf("%.2f\n",range);
	}
	scanner.close();
	}
}
```
### 6.find absolute difference and satisfy the condition:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n1 = scanner.nextInt();
		int n2 = scanner.nextInt();
		int prod = n1*n2;
		int diff= Math.abs(n1 - n2);
		if(n1==n2)
		{
		    System.out.println(prod);
		}
		else
		{
		     System.out.println(diff);
		}
		scanner.close();
	}
}
```
### 7.Math Calculator:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int op = scanner.nextInt();
	int n1= scanner.nextInt();
	int n2 = scanner.nextInt();
	if(op==1)
	{
	    int mod = n1%n2;
	    System.out .println(mod);
	}
	else if(op==2)
	{
	    int pow = (int)Math.pow(n1,n2);
	    System.out .println(pow);
	}
	else if(op==3)
	{
	    int mul= n1*n2;
	    System.out .println(mul);
	}
	else if(op==4)
	{
	    int div=n1/n2;
	    System.out .println(div);
	}
	scanner.close();
	}
}
```
### 8.Hello and Name Printer:
```java
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String fname = scanner.next();
        String lname = scanner.next();
        System.out.println("Hello!");
        System.out.println(fname+" "+lname);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/7a517b6e-116b-4389-9999-016f6ce84926)
### 9.Sum of to numbers:
```java
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        int sum = num1+num2;
        System.out.println(sum);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/ed0cbbbf-491b-4407-8544-7c322421d740)
### 10.Divide two number:
```java
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        int div = num1/num2;
        System.out.println(div);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/a924ccc2-c754-40cb-bbbd-f9f54ca9db8f)
### 11.find last digit and print the pattern: Still not found the defined question.
```java
//find the last digit and the last digit is divided by 2 or 5 print the pattern:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int ld = n%10;
        if(ld%2==0)
        {
            System.out.println("*");
             System.out.println("**");
        }
        else if(ld%5==0)
        {
            System.out.println("*");
             System.out.println("**");
             System.out.println("***");
             System.out.println("****");
        }
        else
        {
            System.out.println("Cannot be divisible by 2 and 5");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/7f6d1106-e076-464d-821b-ade6327621f1)
### 12.Arithmetic operations:
```java
//Arithmetic operations
import java.util.*;
public class Main{
    public static void main(String[] args){
          Scanner scanner = new Scanner(System.in);
          int n1=scanner.nextInt();
          int n2=scanner.nextInt();
          int sum=n1+n2;
          int sub=Math.abs(n1-n2);
          int mul=n1*n2;
          int div=n1/n2;
          int mod=n1%n2;
          System.out.println(sum);
          System.out.println(sub);
          System.out.println(mul); 
          System.out.println(div);
          System.out.println(mod);
          scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/3f34b02a-f1c6-4432-b081-9763ced8e0d0)
### 13.leap year or not:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n= scanner.nextInt();
		if (n==1){
		System.out.println("First");
	    System.out.println("31");}
	    else if (n==2){
	    int n1=scanner.nextInt();
        if(n1%100==0)
        {
            if(n1%400==0)
            {
                System.out.println("It is a leap year!");
                System.out.println("29 days");
            }
            else
            {
                System.out.println("It is not a leap year!");
                System.out.println("28 days");
            }
        }
        else
        {
            if(n1%4==0)
            {
               System.out.println("It is a leap year!");
                System.out.println("29 days"); 
            }
            else
            {
                
                System.out.println("It is not a leap year!");
                System.out.println("28 days");
            }
        }
	    System.out.println("First");
	 }
	    else if(n==3){
	    System.out.println("First");
	    System.out.println("31");}
	    else if(n==4){
	    System.out.println("Second");
	    System.out.println("30");}
	    else if(n==5){
	    System.out.println("Second");
	    System.out.println("31");}
	    else if(n==6){
	    System.out.println("Second");
	    System.out.println("30");}
	    else if(n==7){
	    System.out.println("Third");
	    System.out.println("31");}
	    else if(n==8){
	    System.out.println("Third");
	    System.out.println("31");}
	    else if(n==9){
	    System.out.println("Third");
	    System.out.println("30");}
	    else if(n==10){
	    System.out.println("Fourth");
	    System.out.println("31");}
	    else if(n==11){
	    System.out.println("Fourth");
	    System.out.println("30");}
	    else if(n==12){
	    System.out.println("Fourth");
	    System.out.println("31");}
	    else{
	    System.out.println("Invalid");}
	    scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/c9c4c21f-d607-4b8c-baa3-b6b12c9ae4b9)
### 14.Month Number and Days Calculator:
```java

import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        if(n==1)
        {
            System.out.println("January");
            System.out.println("31 Days");
        }
        else if(n==2)
        {
            int year=scanner.nextInt();
            if(year%100==0)
            {
                if(year%400==0)
                {
                    System.out.println("February");
                    System.out.println("Leap year - 29 Days");
                }
                else
                {
                    System.out.println("February");
                System.out.println("Not a Leap year - 28 Days");
                }
            }
            else
            {
                 if(year%4==0)
                {
                    System.out.println("February");
                    System.out.println("Leap year - 29 Days");
                }
                else
                {
                    System.out.println("February");
                System.out.println("Not a Leap year - 28 Days");
            }
        }
    }
    else if(n==3)
    {
        System.out.println("March");
            System.out.println("31 Days"); 
    }
    else if(n==4)
    {
        System.out.println("April");
            System.out.println("30 Days"); 
    }
    else if(n==5)
    {
        System.out.println("May");
            System.out.println("31 Days"); 
    }
    else if(n==6)
    {
        System.out.println("June");
            System.out.println("30 Days"); 
    }else if(n==7)
    {
        System.out.println("July");
            System.out.println("31 Days"); 
    }
    else if(n==8)
    {
        System.out.println("August");
            System.out.println("31 Days"); 
    }
     else if(n==9)
    {
        System.out.println("September");
            System.out.println("30 Days"); 
    }
     else if(n==10)
    {
        System.out.println("October");
            System.out.println("31 Days"); 
    }
     else if(n==11)
    {
        System.out.println("November");
            System.out.println("30 Days"); 
    }
     else if(n==12)
    {
        System.out.println("December");
            System.out.println("31 Days"); 
    }
    else
    
    {
        System.out.println("Invalid month");
            
    }
    scanner.close();
}
}
```
![image](https://github.com/user-attachments/assets/d967a645-d030-4bfe-beda-87a6eccab5b2)
### 15.Positive or Negative:
```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        if(n>0)
        {
            int cube=n*n*n;
            System.out.println("P");
            System.out.println(cube);
        }
        else if(n==0)
        {
            System.out.println("0");
        }
        else
        {
            int sq=n*n;
            System.out.println("N");
            System.out.println(sq);
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/0401ce61-9a64-41a9-8c6f-65d9eb136434)
### 16.The Ticket Price Calculator:
```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        if(n>=0 && n<=12)
        {
            System.out.println("10");
        }
        else if(n>=13 && n<=17)
        {
            System.out.println("15");
        }
        else if(n>=18 && n<=60)
        {
            System.out.println("20");
        }
        else if(n>=61)
        {
            System.out.println("12");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/e2b3f9b3-af60-4496-be21-da60eebf6719)
### 17.The Chocolate Countdown:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int chocolates = scanner.nextInt();
        int chocconperday=scanner.nextInt();
        int days = scanner.nextInt();
        int actual_days = chocolates/chocconperday;
        if(actual_days>=days)
        {
            System.out.println("1");
        }
        else
        {
              System.out.println("0");
                System.out.println(actual_days);
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/1a38ec3f-96a3-4d8f-8c49-7b44a85f7044)
### 18.The Stationery Shopper:
```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n1=scanner.nextInt();
        int n2=scanner.nextInt();
        int n3=scanner.nextInt();
        int pen=n1*8;
        int note=n2*25;
        int pencil=n3*4;
        int sum=pen+note+pencil;
        System.out.println(sum);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/bd73a618-67dd-4ce2-8fdc-9701ab7b6a28)
### 19.Employee Gross Salry Calculation:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        float bs = scanner.nextFloat();
        float salary,hra,da;
        if(bs<=10000)
        {
            hra=0.20f*bs;
            da=0.80f*bs;
        }
        else if(bs>=10001 && bs<=20000)
        {
            hra=0.25f*bs;
            da=0.90f*bs;
        }
        else
        {
            hra=0.3f*bs;
            da=0.95f*bs;
        }
        salary=hra+da+bs;
        if(salary==Math.floor(salary))
        {
            System.out.printf("%.0f\n",salary);
        }
        else
        {
            System.out.printf("%.2f\n",salary);
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/127c11b5-64e0-49ca-a9c9-1698bf3f7dae)
### 20.Direction Finder:
```java
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        if(a>=0 && a<=89)
        {
            System.out.println("East");
        }
        else if(a>=90 && a<=179)
        {
           System.out.println("North"); 
        }
        else if(a>=180 && a<=269)
        {
            System.out.println("West");
        }
        else if(a>=270 && a<=360)
        {
            System.out.println("South");
        }
        else
        {
            System.out.println("Invalid");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/923e5912-4342-439e-9882-70b68747fdcb)


