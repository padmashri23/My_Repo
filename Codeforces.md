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
### 7. (A) Series of Crimes
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    int n=scanner.nextInt();
	    int m=scanner.nextInt();
	    scanner.nextLine();
	    int x=0;
	    int y=0;
	    for(int i=0;i<n;i++)
	    {
	        String row = scanner.nextLine();
	        for(int j=0;j<m;j++)
	        {
	            if(row.charAt(j)=='*')
	            {
	                x^=i+1;
	                y^=j+1;
	            }
	        }
	    }
		System.out.println(x+" "+y);
		scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/2f7d2f93-8b85-4d85-9210-0071efd63289)
### 10. (A) Next Round:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    int n=scanner.nextInt();
	    int k=scanner.nextInt();
	    int[] scores = new int[n];
	    for(int i=0;i<n;i++)
	    {
	        scores[i]=scanner.nextInt();
	    }
	    int threshhold = scores[k-1];
	    int count=0;
	    for(int score:scores)
	    {
	        if(score>=threshhold && score>0)
	        {
	            count++;
	        }
	    }
		System.out.println(count);
		scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/3ea5704a-abc3-4cef-9bfd-cf81be9a43e2)
### 11.(A) I_love_\%username\%
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    int n=scanner.nextInt();
	    int[] scores = new int[n];
	    for(int i=0;i<n;i++)
	    {
	        scores[i]=scanner.nextInt();
	    }
	    int maxscore=scores[0];
	    int minscore=scores[0];
	    int amazingcount=0;
	    for(int i=0;i<n;i++)
	    {
	        if(i==0)
	        {
	            continue;
	        }
	        if(scores[i]>maxscore)
	        {
	            amazingcount++;
	            maxscore=scores[i];
	        }
	        else if(scores[i]<minscore)
	        {
	            amazingcount++;
	            minscore=scores[i];
	        }
	            
	        }
		System.out.println(amazingcount);
		scanner.close();
	
}
}
```
![image](https://github.com/user-attachments/assets/0ceb45cb-7b50-4cef-83e2-374accfacb30)
![image](https://github.com/user-attachments/assets/305606db-3389-4a8e-88e6-4f41be20b7f8)
### 13.(A) Soft Drinking:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    int n=scanner.nextInt();
	    int k=scanner.nextInt();
	    int l=scanner.nextInt();
	    int c=scanner.nextInt();
	    int d=scanner.nextInt();
	    int p=scanner.nextInt();
	    int nl=scanner.nextInt();
	    int np=scanner.nextInt();
	    
	    int softdrinks=k*l;
	    int drinksoftoasts=softdrinks/nl;
	    int limes=c*d;
	    int salt=p/np;
	    
	    int min=Math.min(drinksoftoasts,Math.min(limes,salt));
	    int res=min/n;
		System.out.println(res);
		scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/eebcf1e3-1139-4632-b3ae-94dd174b433c)
### 12.(A) Remove Smallest:
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int t= scanner.nextInt();
		while(t-->0)
		{
			int n = scanner.nextInt();
			int[] arr = new int[n];

			for(int i=0; i<n; i++)
			{
				arr[i]=scanner.nextInt();
			}
			Arrays.sort(arr);

			boolean possible= true;
			for(int i=1; i<n; i++)
			{
				if(arr[i]-arr[i-1]>1)
				{
					possible = false;
					break;
				}

			}
			if(possible==true)
			{
				System.out.println("YES");
			}
			else {
				System.out.println("NO");
			}

		}

		scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/a830e5fa-22a3-4309-b42f-36efac478b33)
![image](https://github.com/user-attachments/assets/8b130985-f8a3-46d8-8fad-4e1add273d74)
### 14. (A) Insomnia cure
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    int k=scanner.nextInt();
	    int l= scanner.nextInt();
	    int m=scanner.nextInt();
	    int n=scanner.nextInt();
	    int d= scanner.nextInt();
	    int count=0;
	    for(int i=1;i<=d;i++)
	    {
	        if(i%k==0||i%l==0||i%m==0||i%n==0)
	        {
	            count++;
	        }
	    }
		System.out.println(count);
		scanner.close();
	}
}
```
![image](https://github.com/user-attachments/assets/9de4de02-aba0-4751-9e95-8d4de2e17991)
### 15.(A) Lucky Ticket
```java
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    int n=scanner.nextInt();
	    String ticket=scanner.next();
	    int sumfirsthalf=0;
	    int sumsecondhalf=0;
	    for(int i=0;i<n;i++)
	    {
	        char ch = ticket.charAt(i);
	        if(ch!='4'&& ch!='7')
	        {
	         System.out.println("NO");   
	         return;
	        }
	        if(i<n/2)
	        {
	          sumfirsthalf=sumfirsthalf+ch-'0';  
	        }
	        else
	        {
	            sumsecondhalf=sumsecondhalf+ch-'0';
	        }
	    }
	    if(sumfirsthalf==sumsecondhalf)
	    {
		System.out.println("YES");
	    }
		else
		{
		 System.out.println("NO");   
		}
	}
}
```
![image](https://github.com/user-attachments/assets/743cc49c-bd72-484b-84a4-ff418d682bb9)




















