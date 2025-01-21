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


