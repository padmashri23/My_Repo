### 1.A. Is your horseshoe on the other hoof?:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner=new Scanner(System.in);
	    int s1=scanner.nextInt();
	    int s2=scanner.nextInt();
	    int s3=scanner.nextInt();
	    int s4=scanner.nextInt();
	    Set<Integer> uniquecolours = new HashSet<>();
	    uniquecolours.add(s1);
	    uniquecolours.add(s2);
	    uniquecolours.add(s3);
	    uniquecolours.add(s4);
	    int required=4-uniquecolours.size();
		System.out.println(required);
		scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/931d69d0-4a36-49ba-ae84-c62e4d29ac45)
### 2.Boy or Girl:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner=new Scanner(System.in);
	    String username =scanner.nextLine();
	    Set<Character> distchar = new HashSet<>();
	    for(char c:username.toCharArray())
	    {
	        distchar.add(c);
	    }
	    if(distchar.size()%2==0)
	    System.out.println("CHAT WITH HER!");
	    else
		System.out.println("IGNORE HIM!");
	}
}
```
![image](https://github.com/user-attachments/assets/87eb6ffc-24a1-4cdf-a4d5-636e9e16be42)
### 3.A-Team
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    int n=scanner.nextInt();
	    int count=0;
	    for(int i=0;i<n;i++)
	    {
	        int petya=scanner.nextInt();
	        int vasya=scanner.nextInt();
	        int tonya=scanner.nextInt();
	        if(petya+vasya+tonya>=2)
	        {
	            count++;
	        }
	    }
		System.out.println(count);
		scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/19030ae8-2940-41be-91a6-2368713eba29)
### 4.A-Perfect Permutations:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    int n= scanner.nextInt();
	    if(n%2!=0)
	    {
	     System.out.println(-1);   
	    }
	    else
	    {
	        for(int i=0;i<n;i+=2)
	        {
	          System.out.print((i+2)+" "+(i+1)+" ");      
	        }
	    }
	    scanner.close();
		
	}
}
```
![image](https://github.com/user-attachments/assets/c2f60469-7169-4fd9-a03a-12b0082bac49)
### 5.(A) System of Equations:
```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n=scanner.nextInt();
        int m=scanner.nextInt();
        int count=0;
        for(int a=0;a<=1000;a++)
        {
            for(int b=0;b<=1000;b++)
            {
                if(a*a+b==n && a+b*b==m)
                {
                    count++;
                }
            }
        }
        System.out.println(count);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/bb766af5-4bad-4c39-9757-e53a137e901b)
### 6.A.LLPS
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    String s =scanner.next();
	    String result ="";
	    for(char ch='z';ch>='a';ch--)
	    {
	        StringBuilder sb = new StringBuilder();
	        for(int i=0;i<s.length();i++)
	        {
	            if(s.charAt(i)==ch)
	            {
	                sb.append(ch);
	            }
	        }
	        if(sb.length()>0)
	        {
	            result = sb.toString();
	            break;
	        }
	    }
		System.out.println(result);
		scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/1fd1b911-d523-4de3-9757-16a7f418650b)
![image](https://github.com/user-attachments/assets/e0f6ebb6-8a58-485f-b5a7-19702ccf8b4c)










