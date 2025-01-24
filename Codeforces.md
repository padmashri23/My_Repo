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

