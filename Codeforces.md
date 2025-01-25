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




