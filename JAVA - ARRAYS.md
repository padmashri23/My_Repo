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

