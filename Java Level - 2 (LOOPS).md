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




