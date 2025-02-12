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

<h6 style="text-align: center; text-decoration: underline; font-weight: bold;">JAVA LEVEL - 1 </h6>






