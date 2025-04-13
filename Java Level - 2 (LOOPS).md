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

### 12)Odd or Even numbers series:
```java
//Odd or even number series
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    if(n<=0)
    {
      System.out.println("Not a Positive integer");
    }
    else if(n%2==0)
    {
      for(int i = 1;i<=n;i++)
      {
        if(i%2==0)
        {
        System.out.print(i+" ");
        }
        }
    }
    else 
    {
     for(int i = 1;i<=n;i++)
      {
        if(i%2!=0)
        {
        System.out.print(i+" ");
        }
      } 
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/8e9c7137-6a05-4ad2-a3ca-1e209a03dfde)
![image](https://github.com/user-attachments/assets/32db1c63-e3f1-4c44-9637-3f7e243bfc95)

### 13)The Odd Factorial Quest:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int prod=1;
    if(n<1)
    {
      System.out.println("Invalid");
    }
    else if(n%2==0)
    {
      System.out.println("Please enter a valid odd number");
    }
    else
    {
      for(int i = 1;i<=n;i++)
      {
        if(i%2!=0)
        {
          prod = prod*i;
        }
      }
       System.out.println(prod);
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/695521ca-cefc-41ee-b5ad-6a1ab9c5a698)
![image](https://github.com/user-attachments/assets/360e3f84-3047-4e53-8e1e-ee4c4aba0e54)

### 14)Fibonacci Even Number Generator
```java
import java.util.*;
public class main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int a,b,c;
    a = 0;
    b = 1;
    c = 0;
    if(n<=0)
    {
      System.out.println("Invalid");
    }
    else
    {
    for(int i = 0;i<n;i++)
    {
      while(c<=n)
      {
      if(c%2==0  ){
      System.out.print(c+" ");
      }
        a = b;
        b = c;
        c = a+b;
      }
    }
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/12509cba-4396-4f60-92cb-c7f3459dffc4)

### 15)Check Second Even Number
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n1 = scanner.nextInt();
    int n2 = scanner.nextInt();
    int count = 0;
    if(n1%2==0 && n2%2==0)
    {
     for(int i = n1;i<=n2;i++)
     {
       if(i%2==0)
       {
         count++;
         if(count == 2)
         {
           System.out.println(i);
           break;
         }
       }
     }
    }
    else
    {
     System.out.println(n1+" and "+n2+" are not Even."); 
    }
    scanner.close();
  }
}
```
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n1 = scanner.nextInt();
    int n2 = scanner.nextInt();
    int next;
    if(n1%2==0 && n2%2==0)
    {
      next = n1+2;
      System.out.println(next);
    }
    else{
      System.out.println(n1+" and "+n2+" are not Even.");
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/b00e1696-4dd4-4597-b94c-cf06a945566d)

### 16)Sum of First and Last digit:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int num = scanner.nextInt();
    int firstdigit = num;
    int lastdigit = num%10;
    while(firstdigit>9)
    {
      firstdigit = firstdigit/10;
    }
    int sum = firstdigit+lastdigit;
    System.out.println(sum);
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/34ee0070-d18d-4c56-b2de-d72c52c27808)

### 17)Sum of Even Numbers:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int num = scanner.nextInt();
    int sum = 0;
    if(num<=0)
    {
      System.out.println(num+" is an Invalid number.");
    }
    else{
    for(int i = 1;i<=num;i++)
    {
      if(i%2==0)
      {
        sum = sum + i;
      }
    }
     System.out.println(sum);
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/3ec5c943-18f1-4d89-b57d-eb313f7b0821)

### 18)Prime Number in range:
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
    int n1 = scanner.nextInt();
    int n2 = scanner.nextInt();
    for(int i = n1;i<=n2;i++)
    {
      if(isPrime(i))
      {
        System.out.print(i+" ");
      }
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/b19a76da-a68c-44f2-bca1-925836452358)

### 19)Counted the number of leap and non-leap years
```java
import java.util.*;
public class Main{
  public static boolean isLeapYear(int n) {
       if(n%100 == 0)
      {
        if(n%400 == 0)
        {
          return true;
        }
        else{
          return false;
        }
      }
      else{
        if(n%4==0)
        {
          return true;
        }
        else{
          return false;
        }
      }  
    }
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int leapcount = 0;
    int nonleapcount = 0;
    for(int i = n+1;i<=n+10;i++)
    {
      if(isLeapYear(i))
      {
        leapcount++;
      }
      else
      {
        nonleapcount++;
      }
    }
    if(isLeapYear(n))
    {
      System.out.println(n+" is a Leap Year.");
    }
    else
    {
      System.out.println(n+" is not a Leap Year.");
    }
    System.out.println("Leap Years:"+leapcount);
    System.out.println("Non-Leap Years:"+nonleapcount);
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/c4429e42-9fde-427a-97da-77d69dd1fd15)

### 20)Digits Count:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    long n = scanner.nextLong();
    int count = 0;
    n = Math.abs(n);
    if(n==0)
    {
      count = 1;
    }
    while(n>0)
    {
      n = n/10;
      count++;
    }
    System.out.println(count);
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/6859f80b-f13d-4ffe-8224-8a3251f6730e)
![image](https://github.com/user-attachments/assets/8561c581-4279-4a5c-b4ad-209174da7da9)

### 21)Sum of the digits:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    long n = scanner.nextLong();
    long sum = 0;
    n = Math.abs(n);
    if(n==0)
    {
      sum = 0;
    }
    while(n>0)
    {
      sum = sum+n%10;
      n = n/10;
      
    }
    System.out.println(sum);
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/c767ccd0-3a21-4f91-b3eb-587a134d92a4)
![image](https://github.com/user-attachments/assets/386c14bb-151d-4ce5-8cd3-515dfa0151f8)
![image](https://github.com/user-attachments/assets/49f40ba2-1266-4b42-bc42-68c4c1ed5b35)

### 22)Digit Sum Calculator
```java
//Digit Sum Calculator:
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int odd = 0;
    int even = 0;
    while(n>0)
    {
      int digit = n%10;
      if(digit%2==0)
      {
        even = even+digit;
      }
      else{
        odd = odd+ digit; 
      }
      n = n/10;
    }
    System.out.println(even);
    System.out.println(odd);
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/21834d6d-e348-4a10-8ed6-c617a759bf24)

### 23.Product of N digits:
```java
import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int prod = 1;
    while(n>0)
    {
      prod = prod * (n%10);
      n = n/10;
    }
    if(prod==0)
    {
      System.out.println("Invalid Input.");
    }
    else{
    System.out.println(prod);
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/ac63e9c0-5963-4248-a9f4-af9563b96ac5)

### 24.LCM Finder
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n1 = scanner.nextInt();
    int n2 = scanner.nextInt();
    if(n1<0 || n2<0)
    {
      System.out.println("Negative Input");
    }
    else{
    int gcd = findGCD(n1,n2);
    int lcm = (n1 * n2)/gcd;
    System.out.println(lcm);
    }
    scanner.close();
  }
  public static int findGCD(int a,int b)
  {
    if(b==0)
    {
      return a;
    }
    return findGCD(b,a%b);
  }
}
```
![image](https://github.com/user-attachments/assets/7091df7e-0a8f-408a-97bb-6cb4811379e8)

### 25.Harshad Number:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int sum = 0;
    int original = n;
    while(n>0)
    {
      sum = sum+n%10;
      n = n/10;
    }
    if(original%sum==0)
    {
      System.out.println(original+" is Harshad number.");
    }
    else
    {
      System.out.println(original+" is Not Harshad number.");
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/916f291d-e4d2-49b1-ae83-34394d595995)
![image](https://github.com/user-attachments/assets/b469b8f2-1290-4c2d-b255-14ed3c579f65)

### 26.Digit Incrementer
```java
//Digit Incrementer
import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    int original = scanner.nextInt();
    int number = original;
    String result = "";
    while(number>0)
    {
      int digit = number%10;
      digit = (digit+1)%10;
      result = digit+result;
      number = number/10;
    }
    result = result.replaceFirst("^0+","");
    if(result.equals(""))
    {
      result = "0";
      System.out.println(result);
    }
    else{
      System.out.println(result);
    }
    scanner.close();
}
}
```
![image](https://github.com/user-attachments/assets/be664929-ac3b-4d7c-8df4-ea2cfa6baf85)

### 27.Palindrome Check:
```java
//Palindrome Check
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int a;
    int sum = 0;
    int original = n;
    while(n>0)
    {
      a = n%10;
      sum =sum*10+a;
      n = n/10;
    }
    if(sum == original)
    {
      System.out.println(original+" is a Palindrome.");
    }
    else{
      System.out.println(original+" is Not a Palindrome.");
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/c15e30ba-212a-4eab-bff5-a28e107c89da)

### 28) Reverse the Digits:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    float n = scanner.nextFloat();
    if(n<0)
    {
      System.out.println((int)n+" is not a Positive Number.");
    }
    else{
    int intpart = (int)n;
    int sum = 0;
    int a;
    while(intpart>0)
    {
      a = intpart%10;
      sum = sum * 10 + a;
      intpart = intpart/10;
    }
    System.out.println(sum);
    }
    
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/fbbdeb8b-2610-42ec-a583-87d35a4113e2)

### 29) Strong Number:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int original = n;
    int sum = 0;
    while(n!=0)
    {
      int factorial = 1;
      int digit = n%10;
      for(int i = 1;i<= digit;i++)
      {
        factorial = factorial * i;
      }
      sum = sum + factorial;
      n = n/10;
    }
    if(sum == original)
    {
      System.out.println(original+" is a Strong Number.");
    }
    else {
      System.out.println(original+" is Not a Strong Number.");
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/f33fab9b-bb44-4784-8338-3979726dad9d)

### 30)Perfect Square:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    float n = scanner.nextFloat();
    if(n<0)
    {
      System.out.println((int)n+" is Invalid Number.");
    }
    else {
      int intpart = (int)n;
      boolean found = false;
      for(int i = 0;i<=intpart;i++)
      {
        if(i*i == intpart){
        found = true;
        break;
        }
      }
      if(found)
      {
        System.out.println(intpart+" is a Perfect Square.");
      }
      else {
        System.out.println(intpart+" is not a Perfect Square.");
      }
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/761abe01-d7aa-4f5b-bad4-0b8231102056)

### 31)Sum of the Middle Digits:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int sum = 0;
    int a;
    a = a/10;
    for(int i = a;a>9;i++) 
    {
      int b = a%10;
      sum = sum + b;
      a = a/10;
    }
    System.out.println(sum);
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/8a51a1a3-6997-4d07-96e7-554a04a6f670)

### 32)Automorphic number:
```java
//Automorphic number:
import java.util.*;
public class Main{
  public static boolean isAutomorphic(int N)
  {
    int sq = N*N;
    while(N>0)
    {
      if(N%10!=sq%10)
      {
        return false;
      }
      N = N/10;
      sq = sq/10;
    }
    return true;
  }
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    if(isAutomorphic(n))
    {
      System.out.println(n+" is an Automorphic Number.");
    }
    else {
       System.out.println(n+" is not an Automorphic Number.");
    }
  }
}
```
![image](https://github.com/user-attachments/assets/e1756aea-f342-4fe9-8084-fcbdc63f89d3)

### 33)Exploring the Growth Series:
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n1 = scanner.nextInt();
    int n2 = scanner.nextInt();
    int term = n2;
    for(int i = 1;i<=n1;i++)
    {
      System.out.print(term+" ");
      term = term*2;
    }
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/e3e4c649-cdd3-44cd-9f9d-b7cf4184f7d5)

### 34)The Palindromic Sum:
```java
import java.util.*;
public class Main{
  public static boolean isPalindrome(int N)
  {
    int sum = 0;
    int original =  N;
    while(N!=0)
    {
      int a= N%10;
      sum = sum*10+a;
      N = N/10;
    }
    if(sum == original)
    {
      return true;
    }
    else {
        return false;
    }
  }
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int add = 0;
    for(int i = 1;i<=n;i++)
    {
      if(isPalindrome(i))
      {
        add = add+i; 
      }
    }
    System.out.println(add);
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/aa20e0b3-1c07-49fb-b307-8fb5fc600f16)

### 35)Finding the Next Palindrome:
```java
//MOST IMPORTANT
//FINDING THE NEXT PALINDROME
import java.util.*;
public class Main{
  public static boolean isPalindrome(int N)
  {
    int original = N;
    int sum = 0;
    int a;
    while(N!=0)
    {
      a = N%10;
      sum = sum*10+a;
      N = N/10;
    }
    if(sum == original)
    {
      return true;
    }
    else {
      return false;
    }
  }
  public static void main(String[] args)
  {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int count = 0;
    int num = n + 1;
    while(count < 1)
    {
      if(isPalindrome(num))
      {
         System.out.print(num);
         count++;
      }
      num++;
    }   
    scanner.close();
  }
}
```
![image](https://github.com/user-attachments/assets/3485de2b-2ddb-4631-80ed-79b8e0178044)

### 36)Finding Consecutive Palindromic Numbers:
```java







