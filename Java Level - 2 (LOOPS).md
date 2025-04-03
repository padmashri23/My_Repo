<h1 align="center"><u><strong>JAVA LEVEL - 2 </strong></u></h1>

### FOR EVERY PROBLEM'S ITERATIONS REFER TO THE NOTE

### 1)Fibonacci series:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int a,b,c;
        a = 0;
        b = 1;
        c = 0;
        if(n<0)
        {
            System.out.println("Invalid Input");
        }
        else
        {
        for(int i = 0;i<n;i++)
        {
            System.out.print(c+",");
            a = b;
            b = c;
            c = a+b;
        }
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/c2f32cf8-01a5-4817-bdfc-2c85709e4fcf)
![image](https://github.com/user-attachments/assets/b7ce3170-a299-40a0-852d-40fac77f9dc8)

### 2)Smallest Prime Number
```java
import java.util.*;
public class Main{
    public static boolean isPrime(int num)
    {
        if(num<2)
        {
            return false;
        }
        for(int i =2;i*i <= num;i++) 
        {
            if(num%i==0)
            {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int userInput = scanner.nextInt();
        int count = 0;
        int num = userInput+1;
        while(count<5)
        {
            if(isPrime(num))
            {
                System.out.println(num);
                count++;;
            }
            num++;
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/c523e7e2-c02a-46e2-b132-a53fb4ba0621)

![image](https://github.com/user-attachments/assets/c815eee9-2fbe-47bd-a52d-0282acdce3ad)

### 3)Prime or Composite Number:
```java
import java.util.*;
public class Main{
  public static boolean isPrime(int num)
  {
    if(num<2)
    {
      return false;
    }
    for(int i = 2;i*i<=num;i++)
    {
       if(num%i == 0)
       {
         return false;
       }
    }
    return true;
  }
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int num = scanner.nextInt();
    if(num == 1 || num == 0)
    {
      System.out.println(num+" is neither a prime nor a composite number");
    }
    else if(num<0)
    {
      System.out.println(num+" is a Invalid Input");
    }
    else if(isPrime(num))
    {
      System.out.println(num+" is a prime number");
    }
    else
    {
      System.out.println(num+" is a composite number");
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/43ef04cd-fde9-4d01-98ea-bc78af205a56)
![image](https://github.com/user-attachments/assets/64a7a569-77c9-4f8b-9f2b-14739bdfbe52)

### 4)Series Sum Calculator:
```java
//Series Sum Calculator
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int nextTerm = scanner.nextInt();
        int numTerms = scanner.nextInt();
        int sum = 0;
        int term = 0;
        StringBuilder series = new StringBuilder();
        for(int i = 0;i<numTerms;i++)
        {
            term = term*10 + nextTerm;
            sum = sum + term;
            if(i>0)
            {
                series.append(" + ");
            }
            series.append(term);
        }
        System.out.println(series);
        System.out.println(sum);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/95deec1a-fe26-48f5-a106-03e6c472488d)
![image](https://github.com/user-attachments/assets/ce44f9bd-d26f-4184-813f-69def9f55d7f)

### 5)Sum of Squares of N Natural Numbers:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int sum = 0;
    if(n<0)
    {
      System.out.println("Invalid Input");
    }
    else
    {
    for(int i = 1;i<=n;i++)
    {
      int sq = i*i;
      sum = sum+sq;
    }
    System.out.println(sum);
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/a2e07280-5c61-428c-bcff-2dfbceeec903)
![image](https://github.com/user-attachments/assets/59cda454-2cb1-478e-8789-45e7da41d1a7)

### 6)Divisor Sum and Equality Checker:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int sum = 0;
    for(int i = 1;i<n;i++)
    {
      if(n%i==0){
      System.out.print(i+" ");
      sum = sum + i;
      }
      
    }
     System.out.println("\n"+sum);
     if(sum == n)
     {
        System.out.println(n+" is an equal number");
     }
     else
     {
        System.out.println(n+" is not an equal number");
     }
  }
}
```
![image](https://github.com/user-attachments/assets/4ed008cc-cef8-4245-88e9-6d920af91d78)
![image](https://github.com/user-attachments/assets/5f5f75f3-c1ec-4a3b-924d-b22fa9f1f125)

### 7)Abundant Number:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int sum = 0;
    for(int i = 1 ;i<n;i++)
    {
      if(n%i==0)
      {
        sum = sum+i;
      }
    }
    if(sum>n)
    {
      System.out.println(n+" is an Abundant number");
    }
    else
    {
       System.out.println(n+" is not an Abundant number");
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/c62bfa28-26ee-41f2-b117-d20bc80c5c38)
![image](https://github.com/user-attachments/assets/fe9e808f-9dd2-4a19-9e08-0733e6262c05)

### 8)Perfect Cubes:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    if(n<0 || n == 0)
    {
      System.out.println("Invalid");
    }
    else
    {
    for(int i = n;i<=n+2;i++)
    {
      int c = i*i*i;
      System.out.println(c);
    }
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/fdfdb8e3-d477-4f23-912b-948f1e9bf404)
![image](https://github.com/user-attachments/assets/15afb4c0-2c5b-4428-a26e-c6a7412f2da6)

### 9)Squares of Even Numbers & odd number Series:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    if(n%2==0)
    {
      for(int i = 1 ; i <= n ;i++)
      {
        if(i%2==0)
        {
          int sq = i*i;
          System.out.print(sq+" ");
        }
      }
    }
    else
    {
      for(int i = 1;i<=n;i++)
      {
        if(i%2!=0)
        {
          int c = i*i;
          System.out.print(c+" ");
        }
      }
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/4f5d2f9e-f330-49d1-afc0-87465a7f0c3a)
![image](https://github.com/user-attachments/assets/59303acd-b2ae-4ab0-a3d2-16c1587ab2bb)

### 10)The Perfect Number Detective:
```java
import java.util.*;
public class Main{
  public static void main(String[] args){
  Scanner scanner = new Scanner(System.in);
  int n = scanner.nextInt();
  int sum = 0;
  for(int i = 1;i < n;i++)
  {
    if(n%i==0)
    {
      sum = sum + i; 
    }
  }
  if(sum == n)
  {
    int nw = sum/2;
    System.out.println(nw);
  }
  else  
  {
    System.out.println(n);
  }
  scanner.close();
}
}
```
![image](https://github.com/user-attachments/assets/c93c7ee7-94dd-4ea2-a63c-ba42978d2d6f)
![image](https://github.com/user-attachments/assets/f061e8f4-076c-40e1-8d13-97d8016aae2e)

### 11)Handshake Simulation Program:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int sum = 0;
    for(int i = n-1;i>=1;i--)
    {
      sum =sum+i;
    }
    System.out.println(sum);
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/37b25bfb-e49b-46a8-971a-0fd7e365a381)
![image](https://github.com/user-attachments/assets/2cb496e2-4e15-4c66-9cfa-a2f629711517)
