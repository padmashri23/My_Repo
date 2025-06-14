### Introduction:
![image](https://github.com/user-attachments/assets/dd0452c6-af91-4acf-99c7-ec2e6df2d90b)
![image](https://github.com/user-attachments/assets/923fa5f4-20cf-44e4-8b15-22a81bd7f6b3)

### MY FIRST PROGRAM IN JAVA ARRAYS:
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

### Getting the input - reading it and printing it:
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
