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
### 2.Boy or Girl :
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
### 16.(A) Arrival of the General:
```java
import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
 
        int n = sc.nextInt();
        int maxvalue = 0;
        int minvalue = 1000;//The given constraint value is 100
        int maxindex = 0;
        int minindex = 0;
 
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
 
            if (x > maxvalue) {
                maxindex = i;
                maxvalue = x;
            }
            if (x <= minvalue) {
                minindex = i;
                minvalue = x;
            }
        }
 
        if (maxindex > minindex) {
            System.out.println((maxindex - 1) + (n - minindex) - 1);//Taking the second occurance of the element or the occurance of the element which is nearest to the last position. 
        } else {
            System.out.println((maxindex - 1) + (n - minindex));
        }
    }
}
```
![image](https://github.com/user-attachments/assets/e96ab0af-c998-4609-9472-7a89edec8451)
### 17.A. Amusing Joke
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        String guest = scanner.next();
        String host = scanner.next();
        String pile = scanner.next();
        if(canFormNames(guest,host,pile))
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }
        scanner.close();
    }
    private static boolean canFormNames(String guest,String host,String pile)
    {
        String combined= guest+host;
        char[] combinedArr = combined.toCharArray(); 
        char[] pileArr=pile.toCharArray();
        Arrays.sort(combinedArr);
        Arrays.sort(pileArr);
        return Arrays.equals(combinedArr,pileArr);
    }
}
```
![image](https://github.com/user-attachments/assets/f474ab4e-3f47-4212-894e-1de502503729)
### 18.(A) Presents:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n=scanner.nextInt();
        int[] p = new int[n];
        int[] result = new int[n];
        for(int i=0;i<n;i++)
        {
            p[i]=scanner.nextInt();
        }
        for(int i=0;i<n;i++)
        {
            result[p[i]-1]=i+1;
        }
        for(int i=0;i<n;i++)
        {
            System.out.print(result[i]+" ");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/a6cb2cc4-c474-4c71-88bf-d24afb30df78)
![image](https://github.com/user-attachments/assets/cb731571-55ba-4526-bee7-f3b4e1bd29e1)

for     

![image](https://github.com/user-attachments/assets/f2412b86-8131-4c6d-9461-d27973f37bbc)
![image](https://github.com/user-attachments/assets/c5fd6dbd-23de-4126-9f3f-0796ac8ae229)

### 19.(A) Epic Game
```java
import java.util.*;
public class Main{
    public static int gcd(int a,int b)
    {
        return (b==0) ? a : gcd(b,a%b);//recursive euclidean algorithm
    }
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b= scanner.nextInt();
        int n=scanner.nextInt();
        while(true)
        {
            n-=gcd(a,n);
            if(n<0)//if simon cannot take enough stones
            {
                System.out.println("1");//Antisimon will win
                break;
            }
            n-=gcd(b,n);
            if(n<0)//if antisimon cannot take enough stones
            {
                System.out.println("0");//Simon will win
                break;
            }
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/f6628669-5e2f-4275-a773-3add02f5e3f0)
![image](https://github.com/user-attachments/assets/ac0325b7-8e82-41dc-9ce8-28f10e91ef4a)

### 21.(A) Petya and Strings:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        String str1=scanner.nextLine().toLowerCase();
        String str2= scanner.nextLine().toLowerCase();
        int result = str1.compareTo(str2);
        if(result<0)
        {
            System.out.println("-1");
        }
        else if(result>0)
        {
            System.out.println("1");
        }
        else
        {
            System.out.println("0");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/13160828-fcac-4794-9621-b2eb8b5f71e3)
### 22.(A) Nearly Lucky Number:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        String n = scanner.next();
        int luckycount=0;
        for(char c:n.toCharArray())
        {
            if(c=='4'||c=='7')
            {
                luckycount++;
            }
        }
        String countdigit=String.valueOf(luckycount);
        boolean isnearlyLucky=true;
        for(char c:countdigit.toCharArray())
        {
            if(c!='4'&&c!='7')
            {
                isnearlyLucky=false;
            }
        }
        System.out.println(isnearlyLucky?"YES":"NO");
        scanner.close();
        
    }
}
```
![image](https://github.com/user-attachments/assets/24cd615f-76a8-4fe0-bd30-5a11a70f7e19)
### 23. (A) Blackjack:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        if(n<=10 || n>21) //There is no card with a value of more than 10 in a standard deck of 52 cards.
        {
            System.out.println(0);
        }   
        else if(n==20)
        {
            System.out.println(15);
        }
        else
        {
            System.out.println(4);
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/07998590-5169-4d06-91a8-dd69d4ebcdf3)
![image](https://github.com/user-attachments/assets/9edb1a56-51a2-48fd-8403-df881e27909a)
### 24. (A) Chips:
```java
import java.util.Scanner; 
public class ChipsDistribution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); 
        int m = scanner.nextInt();       
        int i = 1;
        while (m >= i) {
            m -= i;
            i = (i % n) + 1;
        }
        System.out.println(m);
        scanner.close();  
    }
}
```
![image](https://github.com/user-attachments/assets/407fdfd9-7b94-4473-8298-977640aa53df)
![image](https://github.com/user-attachments/assets/573213e6-7e4c-447d-8341-95686743e0e1)
![image](https://github.com/user-attachments/assets/8b462246-7561-44d0-8ec9-d8adc0adade8)
### 26.(A) Way Too Long Words:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();
        for(int i=0;i<n;i++)
        {
            String word = scanner.nextLine();
            if(word.length()>10)
            {
                System.out.println(word.charAt(0)+String.valueOf(word.length()-2)+word.charAt(word.length()-1));
                
            }
            else
            {
                System.out.println(word);
            }
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/ece83ad4-e5ee-4606-9eaa-3c22caee2ad6)
### 27. (A) Ultra-Fast Mathematician:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        String num1 = scanner.nextLine();
        String num2 = scanner.nextLine();
        StringBuilder result = new StringBuilder();//using it since it is mutable
        for(int i =0;i<num1.length();i++)
        {
            result.append(num1.charAt(i)==num2.charAt(i)?'0':'1');
        }
        System.out.println(result);
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/f943ca66-39de-467e-9ddb-d475c040e1c9)
### 28. A. Word:
```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        int uppercount=0;
        int lowercount=0;
        for(char c:s.toCharArray())
        {
            if(Character.isUpperCase(c))
            {
                uppercount++;
            }
            else
            {
                lowercount++;
            }
        }
        if(uppercount>lowercount)
        {
            System.out.println(s.toUpperCase());
        }
        else
        {
            System.out.println(s.toLowerCase());
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/e160bbf0-4b4c-456c-9ff7-e0f952d7b190)
### 29. A. Panoramix's Prediction:
```java
//check the m value is the next prime number for the given n;
import java.util.*;
public class Main{
    public static boolean isPrime(int num)
    {
        if(num<2)
        {
            return false;
        }
        for(int i = 2;i * i <= num;i++)
        {   
            if(num%i==0)
            {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int nextPrime = n + 1;
        while(!isPrime(nextPrime))
        {
            nextPrime++;
        }
        if(nextPrime == m)
        {
            System.out.print("YES");
        }
        else{
            System.out.print("NO");
        }
        scanner.close();
    }
}
```
<img width="334" height="506" alt="image" src="https://github.com/user-attachments/assets/74992f71-60a8-4f62-a6ec-0a1dfb75c0a8" />



                                            



























