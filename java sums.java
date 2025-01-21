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
