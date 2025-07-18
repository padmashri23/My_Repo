### Introduction:
![image](https://github.com/user-attachments/assets/dd0452c6-af91-4acf-99c7-ec2e6df2d90b)
![image](https://github.com/user-attachments/assets/923fa5f4-20cf-44e4-8b15-22a81bd7f6b3)
    
### 1.MY FIRST PROGRAM IN JAVA ARRAYS:   
```java
import java.util.*;
public class Main{
  public static void main(String[] args)
  {    
     int[] arr = new int[3];
     arr[0] = 101;
     arr[1] = 102;    
     arr[2] = 103;
     System.out.println(arr[0]);
     System.out.println(arr[1]);
     System.out.println(arr[2]);
  }
}
```
![image](https://github.com/user-attachments/assets/bd149ee7-ad72-4edd-af71-d239263ea238)       

### 2.Getting the input - reading it and printing it:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
      Scanner scanner = new Scanner(System.in);
      System.out.print("Enter the number:");
      int n = scanner.nextInt();
      int[] arr = new int[n];
      System.out.println("Enter the "+n+" numbers:");
      for(int i = 0;i<n;i++)
      {
          arr[i]  = scanner.nextInt();
      }
      System.out.println("The entered numbers are:");
      for(int i = 0;i<n;i++)
      {
          System.out.println(arr[i]);
      }
      scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/92c96449-d7a1-4a44-9955-d1372c237d6c)

### 3.program to print all negative and positive elements in an array:
```java
//pprogram to print all negative and positive elements in an array:
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        int poscount = 0;
        int negcount = 0;
        int zcount = 0;
        System.out.print("Enter the elements:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        System.out.print("The positive elements are:");
        for(int i = 0;i<n;i++){
        if(arr[i]>0)
        {
            System.out.print(arr[i]+" ");
            poscount++;
        }
        }
        System.out.print("\n"+"The pos elements count are:"+poscount);
        System.out.print("\n"+"The negative elements are:");
        for(int i = 0;i<n;i++){
        if(arr[i]<0)
        {
            System.out.print(arr[i]+" ");
            negcount++;
        }
        }
        System.out.print("\n"+"The neg elements count are:"+negcount);
        System.out.print("\n"+"the zero elements are:");
        for(int i = 0;i<n;i++){
        if(arr[i]==0)
        {
            System.out.print(arr[i]+" ");
            zcount++;
        }
        }
        System.out.print("\n"+"The zero elements count are:"+zcount);   
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/0fee0254-bf3a-4f0a-ad90-18a8dacad768)

### 4.Find the sum of all array elements:
```java
//Java program to find the sum of all array elements:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        int sum = 0;
        System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        for(int i = 0;i<n;i++)
        {
            sum = sum + arr[i];
        }
        System.out.print("The sum is:"+sum);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/f3cdcc7b-2a65-42c2-a0f5-2ef1336f75fe)

### 5.Find maximum and minimum element in an array:
```java
//Find maximum and minimum element in array:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int max = arr[0];
        int min = arr[0];
        for(int i = 0;i<n;i++)
        {
            if(arr[i]>max)
            {
                max = arr[i];
            }
            if(arr[i]<min)
            {
                min = arr[i];
            }
        }
        System.out.println("The maximum element is:"+max);
        System.out.println("The minimum element is:"+min);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/5daf9852-0858-4719-9040-7baf9bbbf59d)

### 6.Program to count even and odd elements in an array:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int even = 0;
        int odd = 0;
        for(int i = 0;i<n;i++)
        {
            if(arr[i]%2==0)
            {
                even++;
            }
            else{
                odd++;  
            }
        }
        System.out.println("The no of even elements:"+even);
        System.out.println("The no of odd elements"+odd);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/917c78a0-b986-4f83-9cd4-c71e27d57dda)

### 7.Reverse of the array:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        System.out.print("The reverse of the array is:");
        for(int i = n - 1;i>=0;i--)
        {
            System.out.print(arr[i]+" ");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/9652495c-46e1-4e55-9483-1c13e400e3cc)

### 8.Program to search element in an array:
```java
//program to search element in an array:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int search = scanner.nextInt();
        boolean found = false;
        for(int i = 0;i<n;i++)
        {
            if(arr[i]==search)
            {
                found = true;
                break;
            }
        }
        if(found)
        {
            System.out.println(search+" is found");
        }
        else {
            System.out.println(search+" is not found");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/1754b5d3-b8cd-4d36-b3d4-084f6051f988)

### 9.Number of occurrences of an number:
```java
 //Number of occurrences of a number
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int oc = scanner.nextInt();
        int count = 0;
        for(int i = 0;i<n;i++)
        {
            if(arr[i] == oc)
            {
                count++;
            }
        }
        System.out.println(count);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/53713b6f-64cb-4034-ba05-c3a6d5417be4)

### 10.Print the square of the elements in an array:
```java
//Print the square of the elements in an array
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        for(int i = 0;i<n;i++)
        {
            int sq = arr[i]*arr[i];
            System.out.print(sq+" ");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/49ead057-a10e-43b6-82d7-14fc200504c0)

### 11.Program to count duplicate elements in array:
```java
//program to count duplicate elements in array:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int count = 0;
        for(int i = 0;i<n;i++)
        {
            for(int j = i + 1;j<n;j++)
            {
                if(arr[i] == arr[j])
                {
                    count++;
                    break;
                }
            }
        }
        System.out.println("The duplicate count are:"+count);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/ad0cbc78-06fc-4f34-a3c1-f1321ed02537)

### 12.Difference between maximum and minimum element of an array:
```java
//Difference between maximum and minimum element of an array:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int max = arr[0];
        int min = arr[0];
        for(int i = 0;i<n;i++)
        {
            if(arr[i]>max)
            {
                max = arr[i];
            }
            if(arr[i]<min)
            {
                min = arr[i];
            }
        }
        System.out.println(max);
        System.out.println(min);
        int diff = max - min;
        System.out.println(diff);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/3249167c-7676-4d1b-97ed-a761fbd3a3d4)

### 13).Program to copy array elements to another array:
```java
//Program to copy array elements to another array:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] src = new int[n];
        int[] dest = new int[n];
        for(int i = 0;i<n;i++)
        {
            src[i] = scanner.nextInt();
        }
        for(int i = 0 ;i<n;i++)
        {
            dest[i] = src[i];
        }
        System.out.print("The source elements are:");
        for(int i = 0;i<n;i++)
        {
            System.out.print(src[i]+" ");
        }
        System.out.print("\n"+"The copied elements are:");
        for(int i = 0;i<n;i++)
        {
            System.out.print(dest[i]+" ");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/53169fef-2854-4743-9799-93454a0afe19)

### 14)Insert an element into an array at a specified position:
```java
//Insert an element into an array at a specified position
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        System.out.print("Enter the elements of the array:");
        int[] arr = new int[n];
        for(int i = 0 ;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        System.out.print("Enter the element to be inserted:");
        int num = scanner.nextInt();
        System.out.print("Enter the element inserted position:");
        int pos = scanner.nextInt();
        int[] temp = new int[n + 1];
        int position = pos - 1;
        for(int i = 0;i<=n;i++)
        {
            if(i<position)
            {
                temp[i] = arr[i];
            }
            if(i>position)
            {
                temp[i] = arr[i - 1];
            }
            if(i == position)
            {
                temp[i] = num;
            }
        }
        System.out.print("The element "+num+" is inserted in the position "+pos+":");
        for(int i = 0;i<=n;i++)
        {
            System.out.print(temp[i]+" ");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/b3228edb-250e-41a2-b4f5-e18597a7f7a7)

### 15)Program to find sum of negative and positive integers:
```java
//Program to find sum of negative and positive integers:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int pos = 0;
        int neg = 0;
        for(int i = 0;i<n;i++)
        {
            if(arr[i]>0)
            {
                pos = pos + arr[i];
            }
            else{
                neg = neg + arr[i];
            }
        }
        System.out.println(pos);
        System.out.println(neg);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/a10ce7b3-5dd9-434a-9dae-a9f4df75b48e)

### 16)Removing even number from an array:
```java
//Removing even number from an array:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        for(int i = 0;i<n;i++)
        {
            if(arr[i]%2!=0)
            {
                System.out.print(arr[i]+" ");
            }
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/121d381e-b8d9-434d-9a84-b175104cca93)

### 17)Print the unique elements in an array:
```java
//Print the unique elements in an array:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        System.out.print("The unique elements are:");
        for(int i = 0;i<n;i++)
        {
            int count = 1;
            for(int j = 0;j<n;j++)
            {
                if(arr[i] == arr[j])
                {
                    count++;
                }
            }
            if(count == 2)
            {
                System.out.print(arr[i]+" ");
            }
        }
        scanner.close();
    }
}
```
```java
//print the unique elements if no unique elements found print accordingly:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        System.out.print("The unique elements are:");
        boolean unique = false;
        for(int i = 0;i<n;i++)
        {
            int count = 0;
            for(int j = 0;j<n;j++)
            {
                if(arr[i] == arr[j])
                {
                    count++;
                }
            }
            if(count == 1)
            {
                System.out.print(arr[i]+" ");
                unique = true;
            }
        }
        if(!unique)
        {
            System.out.print("0");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/3f6f4df4-a32a-4499-a6e1-e7812b6d3dc7)
![image](https://github.com/user-attachments/assets/b0f9e605-ae4a-4339-ae39-6d2e1f8bcf15)

### 18)Sum the array after removing duplicate elements:
```java
//Sum the array after removing duplicate elements
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int sum = 0;
        for(int i = 0;i<n;i++)
        {
            boolean isDuplicate = false;
            for(int j = i + 1;j<n;j++)
            {
                if(arr[i] == arr[j])
                {
                    isDuplicate = true;
                    break;
                }
            }
            if(!isDuplicate)
            {
                sum = sum + arr[i];
            }
        }
        System.out.print("The sum after removing duplicates are:"+sum);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/fd01c03a-161f-4037-9d3d-07608cbabb74)

### 19)Middle numbers of the given array:
```java
//Find the middle numbers of the given array:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the array size:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        if(n%2==0)
        {
            System.out.print("The middle numbers are:"+arr[n/2 - 1]+" "+arr[n/2]);
        }
        else{
            System.out.print("The middle number is:"+arr[n/2]);
        }
        scanner.close();
    }
}
```
<img width="617" height="233" alt="image" src="https://github.com/user-attachments/assets/148b3e74-652d-4daf-b374-4dc81176e653" />

### 20)Print the second largest in an array:
```java
//Second largest element in an array
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
       int max = arr[0];
       int second = -1;
       for(int i = 0;i<n;i++)
       {
           if(arr[i]>max)
           {
               second = max;
               max = arr[i];
           }
           else if(arr[i]>second && arr[i]<max)
           {
               second = arr[i];
           }
       }
       if(second == -1){
           System.out.println("There is no second largest");
       }
       else{
           System.out.print("The second largest element is:"+second);
       }
       scanner.close();
    }
}
```
<img width="484" height="140" alt="image" src="https://github.com/user-attachments/assets/518a50b0-fcc0-4a6c-90ab-1f1507e78fb5" />
<img width="534" height="145" alt="image" src="https://github.com/user-attachments/assets/4a526119-045b-40b5-a684-968810a648f3" />
<img width="553" height="205" alt="image" src="https://github.com/user-attachments/assets/894479b1-6441-445a-9ee5-e9b2526c15cc" />

### 21)Print the average of the array:
```java
//Print the average of the array
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
         System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int sum = 0;
        for(int i = 0;i<n;i++)
        {
            sum = sum + arr[i];
        }
        double avg = (double)sum/n;
        System.out.printf("The average is:"+avg);
        scanner.close();
    }
}
```
<img width="485" height="210" alt="image" src="https://github.com/user-attachments/assets/90a622b5-5803-4662-9971-3a67fdc58b9e" />

### 22)Count of array elements divisible by specific number:
```java
//Count of array elements divisible by specific number
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of elements:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        System.out.print("Enter the specific number:");
        int k = scanner.nextInt();
        int count = 0;
        for(int i = 0;i<n;i++)
        {
            if(arr[i]%k == 0)
            {
                count++;
            }
        }
        System.out.print("The count is:"+count);
        scanner.close();
    }
}
```
<img width="612" height="206" alt="image" src="https://github.com/user-attachments/assets/b975a291-62ba-4712-94ba-49559c4e3e59" />

### 23)Frequency of a number:
```java
//Frequency of a number
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array:");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        boolean[] counted = new boolean[n];
        for(int i = 0;i<n;i++)
        {
            if(counted[i])
            {
                continue;
            }
            int count = 1;
            for(int j = i + 1;j<n;j++)
            {
                if(arr[i] == arr[j])
                {
                    count++;
                    counted[j] = true;
                }
            }
            System.out.println("The frequency of "+arr[i]+" is "+count);
        }
        scanner.close();
    }
}
```
<img width="530" height="187" alt="image" src="https://github.com/user-attachments/assets/ba7fb1d2-e249-4db9-ab31-7c4499499d8b" />

### 24)Find the missing element:
```java
//find the missing number:
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the array size:");
        int n = scanner.nextInt();
        int[] arr = new int[n - 1];
        System.out.print("Enter the elements:");
        for(int i = 0;i<n - 1;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int sum = 0;
        int total = n *(n + 1)/2;
        for(int i = 0;i<n - 1;i++)
        {
            sum = sum + arr[i];
        }
        int missing = total - sum;
        System.out.print("The missing element is:"+missing);
        scanner.close();
    }
}
```
<img width="531" height="256" alt="image" src="https://github.com/user-attachments/assets/653eb0e0-f3e8-4f39-9d40-1e5bc5bf0499" />
