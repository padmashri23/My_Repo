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


<h1 align="center"><u><strong>JAVA LEVEL - 1 </strong></u></h1>

### 1.The Grading Gauntlet:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        char grade = scanner.next().charAt(0);
        if(grade=='A')
        {
            System.out.println("Outstanding");
        }
        else if(grade=='B')
        {
            System.out.println("EXCELLENT");
        }
          else if(grade=='C')
        {
            System.out.println("GOOD");
        }
          else if(grade=='D')
        {
            System.out.println("JUST PASS");
        }
          else if(grade=='F')
        {
            System.out.println("FAIL");
        }
        else
        {
            System.out.println("Invalid");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/435682fe-b91b-48ca-ad97-a9e0e8e19148)
### 2.Student Grading Program:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int n1 = scanner.nextInt();
		int n2 = scanner.nextInt();
			int n3 = scanner.nextInt();
				int n4 = scanner.nextInt();
					int n5 = scanner.nextInt();
	int sum=n1+n2+n3+n4+n5;
	float per = (float) sum/5;
	System.out.printf("%.2f\n",per);
	if(per>=95)
	{
	    System.out.println("A");
	}
	else if(per>=85)
	{
	    System.out.println("B");
	}
	else if(per>=75)
	{
	    System.out.println("C");
	}
	else if(per>=65)
	{
	    System.out.println("D");
	}
	else if(per>=45)
	{
	    System.out.println("E");
	}
	else
	{
	    System.out.println("F");
	}
	scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/892bcecd-f18c-44b5-aa6e-f71b90f10821)
### 3.Month Days Counter:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n= scanner.nextInt();
		if (n==1){
		System.out.println("First");
	    System.out.println("31");}
	    else if (n==2){
	    System.out.println("First");
	    System.out.println("28 or 29");}
	    else if(n==3){
	    System.out.println("First");
	    System.out.println("31");}
	    else if(n==4){
	    System.out.println("Second");
	    System.out.println("30");}
	    else if(n==5){
	    System.out.println("Second");
	    System.out.println("31");}
	    else if(n==6){
	    System.out.println("Second");
	    System.out.println("30");}
	    else if(n==7){
	    System.out.println("Third");
	    System.out.println("31");}
	    else if(n==8){
	    System.out.println("Third");
	    System.out.println("31");}
	    else if(n==9){
	    System.out.println("Third");
	    System.out.println("30");}
	    else if(n==10){
	    System.out.println("Fourth");
	    System.out.println("31");}
	    else if(n==11){
	    System.out.println("Fourth");
	    System.out.println("30");}
	    else if(n==12){
	    System.out.println("Fourth");
	    System.out.println("31");}
	    else{
	    System.out.println("Invalid");}
	    scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/fc5e5d39-f5b4-4c94-8c9b-65f2534541ee)






