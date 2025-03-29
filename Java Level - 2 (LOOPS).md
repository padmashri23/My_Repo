<h1 align="center"><u><strong>JAVA LEVEL - 2 </strong></u></h1>

### For every problem's Iterations refer to the note:
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


