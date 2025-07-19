### 1.Ishaan Loves Chocolates:
```java
class Solution {
    public static int chocolates(int n, int[] arr) {
        int left=0,right=n-1;      
        while(left<right)
        {
            if(arr[left]>=arr[right])
            {
                left++;
            }
            else
            {    
                right--;
            }
        }
        return arr[left];
        // code here
    }
}
```
### Another approach for the same sum:
```java
class Solution {
    public static int chocolates(int n, int[] arr) {
        
        int min=arr[0];
        for(int i=0;i<n;i++)
        {
            if(arr[i]<min)
            {
                min=arr[i];
            }
        }
        return min;
    }
}
```
### 2.Move All Zeroes to End:
```java
class Solution {
    void pushZerosToEnd(int[] arr) {
        int l=0,r=0,n=arr.length;
        while(r<n)
        {
            if(arr[r]!=0)
            {
                int temp=arr[l];
                arr[l]=arr[r];
                arr[r]=temp;
                l++;
            }
            r++;
        }
    }
}
```
![WhatsApp Image 2025-01-22 at 23 48 06_6c82f1cc](https://github.com/user-attachments/assets/dc1fd36e-a099-4749-9730-f54eb8583a40)
### 3.Sum of Natural Numbers:
```java
class Solution {
    public static int seriesSum(int n) {
        int sum=0;
         for(int i=0;i<=n;i++)
        {
            sum=sum+i;
        }
        return sum;
    }
}
```
![image](https://github.com/user-attachments/assets/2b0aeca9-55f4-4e5a-b172-342920d18dba)
### 4.Value equals to index value:
```java
class Solution {
    public List<Integer> valueEqualToIndex(List<Integer> nums) {
        List<Integer> result =new ArrayList<>();
        for(int i=0;i<nums.size();i++)
        {
            if(nums.get(i)==i+1)
            {
              result.add(i+1);  
            }
        }
        return result;
    }
}
```
![image](https://github.com/user-attachments/assets/eb9a673a-f7a2-4ca7-912f-a4e5b6695d35)
### 5.Alternates in an Array:
```java
class Solution {
    public ArrayList<Integer> getAlternates(int arr[]) {
       ArrayList<Integer> result = new ArrayList<>();
       for(int i=0;i<arr.length;i++)
       {
         if(i%2==0)
         {
             result.add(arr[i]);
         }
       }
       return result;
    }
}
```
![image](https://github.com/user-attachments/assets/fbd770fc-f319-4c5d-8bec-e62866394678)
### 6.Palindromic Array
```java
class Solution {
    public static boolean isPalinArray(int[] arr) {
        for(int num:arr)
        {
            if(!isPalindrome(num))
            {
                return false;
            }
        }
        return true;
    }
    private static boolean isPalindrome(int num)
    {
        int original=num;
        int reverse =0;
        while(num>0)
        {
        int digit=num%10;
        reverse=reverse*10+digit;
        num=num/10;
        }
        return original==reverse;
    }
}
```
![image](https://github.com/user-attachments/assets/6fbe8350-bc22-4c7f-8478-2ca2b5fd1347)
### 7.Count of Smaller elements:
```java
class Solution {
    public int countOfElements(int x, List<Integer> arr) {
        int count=0;
        for(int num:arr)
        {
           if(num<=x)
           {
               count++;
           }
        }
        return count;
    }
}
```
![image](https://github.com/user-attachments/assets/12ba4f2f-9756-4f74-be9a-e3b8694bcff3)
### 8.Sum of Array:
```java
class Solution {
    int arraySum(int arr[]) {
        int sum=0;
        for(int num:arr)
        {
            sum=sum+num;
        }
        return sum ;
    }
}
```
![image](https://github.com/user-attachments/assets/1c287c94-0ec6-4a90-9790-24b6d7ac5768)
### 8.Print Elements of Array:
```java
class Solution {

    void printArray(int arr[]) {
      for(int i=0;i<arr.length;i++)
      {
          System.out.print(" "+arr[i]);
      }
    }
}
```
![image](https://github.com/user-attachments/assets/38d1e503-042d-486c-8e99-5387d49acc0b)
### 9.Find Index:
```java
class Solution {
    static int[] findIndex(int arr[], int key) {
     int startIndex=-1;
     int endIndex=-1;
     for(int i=0;i<arr.length;i++)
     {
         if(arr[i]==key)
         {
             if(startIndex==-1)
             {
                 startIndex=i;
             }
             endIndex=i;
         }
     }
     return new int[]{startIndex,endIndex};
    }
}
```
![image](https://github.com/user-attachments/assets/b1131d05-d7f6-4461-915e-0c9facebfe76)
![image](https://github.com/user-attachments/assets/efda9260-8c4a-4080-91fa-2cce359c4016)
### 10.Swap kth element:
```java
class Solution {
    public void swapKth(List<Integer> arr, int k) {
        int n=arr.size();
        if(k>n || k<1)
        {
            return;
        }
        int firstIndex=k-1;
        int lastIndex=n-k;
        
        int temp=arr.get(firstIndex);
        arr.set(firstIndex,arr.get(lastIndex));
        arr.set(lastIndex,temp);
        
    }
}
```
![image](https://github.com/user-attachments/assets/39254e72-7b40-41aa-b1d7-875c9f8d46bd)
### 11.Display longest name
```java
class Solution {
    public String longest(List<String> arr) {
       String longest=arr.get(0);
       for(String name:arr)
       {
           if(name.length()>longest.length())
           {
               longest=name;
           }
       }
       return longest;
    }
}
```
![image](https://github.com/user-attachments/assets/2081106e-eeac-49ba-a16d-5b90948072dc)
![image](https://github.com/user-attachments/assets/3bf14ac0-47e4-42e7-8982-6d4fce46c06d)
### 12.Palindrome Array:
```java
class Solution {
    public static boolean isPerfect(int[] arr) {
        int n=arr.length;
        for(int i=0;i<n/2;i++)
        {
            if(arr[i]!=arr[n-i-1])
          //we should use the not equal to first this code it will return true as soon as it finds the first matching pair of elements, even if the array is not a palindrome. This logic does not 
           fully check whether the array is a palindrome.
            {
                return false;
            }
        }
        return true;
    }
}
```
![image](https://github.com/user-attachments/assets/bd1c32e8-0b1c-4473-a622-766ad15cac3e)
### 13.Smaller and Larger:
```java
class Solution {
    int[] getMoreAndLess(int[] arr, int target) {
       int lessorequal=0;
       int greaterorequal=0;
       for(int num:arr)
       {
           if(num>=target)
           {
               greaterorequal++;
           }
           if(num<=target)
           {
               lessorequal++;
           }
       }
        return new int[]{lessorequal,greaterorequal};
       
    }
   
}
```
![image](https://github.com/user-attachments/assets/53c7f2d8-c71d-4f95-8551-f55affba67aa)
### 14.Atleast Two greater elements:
```java
class Solution {
    public long[] findElements(long arr[]) {
        if(arr.length<=2) return new long[0];
        Arrays.sort(arr);
        return Arrays.copyOfRange(arr,0,arr.length-2);
    }
}
```
![image](https://github.com/user-attachments/assets/8212226f-78a0-4842-ac82-0fc29fd36f37)
### 15.Find the left over element:
```java
class Solution {
    public static int leftElement(int[] arr) {
        Arrays.sort(arr); 

        int left = 0, right = arr.length - 1; 
        boolean removeMax = true;

        while (left < right) { 
            if (removeMax) {
                right--; 
            } else {
                left++;  
            }
            removeMax = !removeMax;
        }
        
        return arr[left];
    }
}
```
![image](https://github.com/user-attachments/assets/92b9452b-fcaf-4df7-854c-6a2a3cbf48b4)
![image](https://github.com/user-attachments/assets/e8e55f8a-393a-41e7-9c8a-5866ac75abcf)
![image](https://github.com/user-attachments/assets/3e535a6d-f9e5-4017-b7dd-2f9370c2eb81)
### 16.Fascinating Number:
```java
class Solution {
    boolean fascinating(long n) {
        if(n<100) 
        {
            return false;
        }
        long n1=n*2;
        long n2=n*3;
        String concatenated = n+""+n1+n2;
        if(concatenated.length()!=9)
        {
            return false;
        }
        HashSet<Character> digits = new HashSet<>();
        for(char c:concatenated.toCharArray())
        {
            if(c=='0'||digits.contains(c))
            {
                return false;   
            }
            digits.add(c);
        }
        return digits.size()==9;
    }
}
```
![image](https://github.com/user-attachments/assets/903e0827-f5b8-43ea-a88b-5845e62961d1)
### 17.Average of Prefix:
```java
class Solution {
    
    public ArrayList<Integer> prefixAvg(ArrayList<Integer> arr) {
       ArrayList<Integer> result = new ArrayList<>();
       if(arr==null || arr.size()==0)
       {
           return result;
       }//this is the optimal to check whether the array list is null or empty---If the list is empty, there are no elements to compute averages, so return an empty list.
       long sum=0;
       for(int i=0;i<arr.size();i++)
       {
           sum=sum+arr.get(i);
           result.add((int)(sum/(i+1)));
       }
       return result;
    }
}
```
![image](https://github.com/user-attachments/assets/0659224c-9385-4954-92f4-105ad8e16293)
### 18.Compete the skills
```java

class Solution {
   
    static ArrayList<Integer> scores(int arr1[], int arr2[]) {
       int scoreA=0;
       int scoreB=0;
       for(int i=0;i<3;i++)
       {
           if(arr1[i]>arr2[i])
           {
               scoreA++;
           }
           else if(arr1[i]<arr2[i])
           {
               scoreB++;
           }
       }
       ArrayList<Integer> result = new ArrayList<>();
       result.add(scoreA);
       result.add(scoreB);
       return result;
    }
}
```
![image](https://github.com/user-attachments/assets/5105bf00-df6c-4747-be89-42ee969df6a8)
### 19.Binary Search:
```java
    public int binarysearch(int[] arr, int k) {
      int left=0;
      int right=arr.length-1;
      int result=-1;
      while(left<=right)
      {
      int mid=left+(right-left)/2;
        if(arr[mid]==k)
        {
            result=mid;
            right=mid-1;
        }
        else if(arr[mid]<k)
        {
            left=mid+1;
        }
        else
        {
            right=mid-1;
        }
      }
      return result;
    }
}
```
![image](https://github.com/user-attachments/assets/b11653ae-9f35-4d2d-9d41-1134315d0061)

[Binary Search](https://www.geeksforgeeks.org/binary-search/)

![image](https://github.com/user-attachments/assets/61c7ef29-0ece-4efe-b9bb-4e415f661459)

### 20.Check Equal Arrays:
```java
class Solution {
    public static boolean checkEqual(int[] a, int[] b) {
      if(a.length!=b.length)
      {
          return false;
      }
      Arrays.sort(a);
      Arrays.sort(b);
      return Arrays.equals(a,b);
    }
}//use hashmap for the optimized O(n) complexity
```
![image](https://github.com/user-attachments/assets/ddcb822e-a901-4def-b8ce-fa8db91ef5aa)

### 21.Reverse array in groups:
```java
class Solution {
    void reverseInGroups(ArrayList<Long> arr, int k) {
    int n =arr.size();
    for(int i=0;i<n;i=i+k)
    {
        int left=i;
        int right=Math.min(i+k-1,n-1);
    while(left<right)
    {
        long temp = arr.get(left);
        arr.set(left, arr.get(right));
        arr.set(right, temp);
        left++;
        right--;
    }
    } 
}
}
```
![image](https://github.com/user-attachments/assets/8511d2b5-0e9b-4e82-bc75-6ed7c61914f5)
![github img](https://github.com/user-attachments/assets/85c34053-d9ee-4d77-83e8-ef04231590ba)

### 22.Array Search:
```java
class Solution {
    static int search(int arr[], int x) {
      int n=arr.length;
      for(int i=0;i<n;i++)
      {
          if(arr[i]==x)
          {
              return i;
          }
      }
      return -1;
    }
}
```
![image](https://github.com/user-attachments/assets/a4fcef36-715b-4837-b11c-596e0d433441)

### 23.Array Subset:
```java
class Solution {
    public boolean isSubset(int a[], int b[]) {
       Arrays.sort(a);
       Arrays.sort(b);
       int i=0;
       int j=0;
       while(i<a.length && j<b.length)
       {
           if(a[i]==b[j])
           {
               j++;
           }
               i++;
       }
       return j==b.length;
    }
}
```
![image](https://github.com/user-attachments/assets/0862af15-39e7-4577-b401-09370378e6c7)
![image](https://github.com/user-attachments/assets/44487b4a-3969-47b4-b39e-af27f2078499)
### BETTER USE HASHMAP

### 24.Rotate Array by One:
```java
class Solution {
    public void rotate(int[] arr) {
      if(arr==null||arr.length<=1)
      {
          return;
      }
      int lastelement=arr[arr.length-1];
      for(int i=arr.length-1;i>0;i--)
      {
          arr[i]=arr[i-1];
      }
      arr[0]=lastelement;
    }
}
```
![image](https://github.com/user-attachments/assets/1458c2f2-40b5-404e-9129-f86d4dd99820)
### 25.Min and Max in ArraY:
```java
class Solution {
    public Pair<Integer, Integer> getMinMax(int[] arr) {
       if(arr== null || arr.length==0)
       {
           return new Pair<>(-1,-1);
       }
       int min=arr[0];
       int max=arr[0];
       for(int num:arr)
       {
           if(num<min)
           {
               min=num;
           }
           if(num>max)
           {
               max=num;
           }
       }
       return new Pair<>(min,max);
    }
}
```
![image](https://github.com/user-attachments/assets/36b7e7e5-6738-4b73-84b0-9be3a1053ce4)
### 26.Min and Max in Array:
```java
class Solution {
    public static int largest(int[] arr) {
    int max=arr[0];
    for(int num:arr)
    {
        if(num>max)
        {
            max = num;
        }
    }
    return max;
    }
}
```
![image](https://github.com/user-attachments/assets/e613b52c-70fe-4c44-af0a-02eb3a2b73c1)
### 27.Immediate Smaller Element:
```java
class Solution {
    public void immediateSmaller(int arr[]) {
        int n=arr.length;
        for(int i=0;i<n-1;i++)
        {
            if(arr[i]>arr[i+1])
            {
                arr[i]=arr[i+1];
            }
            else
            {
                arr[i]=-1;
            }
        }
        arr[n-1]=-1;
    }
}
```
![image](https://github.com/user-attachments/assets/b36fc52b-8df7-489b-8d1e-981e7122bc15)
### 28.At Least K Occurrences:
```java
class Solution {
    public int firstElementKTime(int[] arr, int k) {
    int n=arr.length;
    int[] freq = new int[1000001];
    for(int i=0;i<n;i++)
    {
        freq[arr[i]]++;
        if(freq[arr[i]]>=k)
        {
            return arr[i];
        }
    }
    return -1;
    }
}
```
![image](https://github.com/user-attachments/assets/96cc4650-868a-4cf7-a540-1f34ef8b67dd)
![image](https://github.com/user-attachments/assets/d87eda41-be28-4529-a32c-ca3889863883)
![image](https://github.com/user-attachments/assets/f174f243-6549-429b-adf8-9ac8960d3991)

### 29.Java Switch Case statement:
```java
import java.util.*;
class Solution {
    static double switchCase(int choice, List<Double> arr) {
        if(choice == 1)
        {
            double R = arr.get(0);
            double ans = Math.PI*R*R;
            return ans;
        }
        else {
            double L = arr.get(0);
            double B = arr.get(1);
            double ans = L*B;
            return ans;
        }
    }
}
```
![image](https://github.com/user-attachments/assets/f531639a-989d-4b72-9cd8-123f6ff93139)

### 30)Vowel or Not:
```java
class Solution {
    String isVowel(char c) {
    if(c == 'a' || c=='e' || c=='i' || c=='o' || c=='u' ||
    c == 'A' || c=='E' || c=='I' || c=='O' || c=='U')
        {
            return "YES";
        }
        else{
            return "NO";
        }
        
    }
}
```
![image](https://github.com/user-attachments/assets/79119bf2-7255-4031-a7eb-06654692dd43)

### 31)Pattern Printing:
```java
// User function Template for Java
class Solution {
    static void printPattern(int N) {
        // code here
        for(int i = 1;i<=N;i++)
        {
            for(int j = 1;j<=i;j++)
            {
                System.out.print("*");
            }
            System.out.print(" ");
        }
    }
}
```
![image](https://github.com/user-attachments/assets/03025a32-08cd-4f9f-a526-6c767a11a143)

### 33)Sum 1 to n Divisors:
```java
class Solution {
    public static long sumOfDivisors(long n) { 
    int totalsum  = 0;
    for(int i = 1;i<=n;i++)
    {
        int sum = 0;
        for(int j = 1;j<=i;j++)
        {
            if(i%j==0)
            {
                sum = sum + j;
            }
        }
        totalsum = totalsum + sum;
    }
    return totalsum;
    }
}
```
![image](https://github.com/user-attachments/assets/9b1459a6-a6ec-48e1-8ff2-40be79e6d633)

### 34)Count Digits:
```java

class Solution {
    static int evenlyDivides(int n) {
        int count = 0;
        int a;
        int og = n;
        while(n!=0)
        {
            a = n % 10;
            if(a!=0 && og%a==0)
            {
                count++;
            }
            n = n/10;
        }
        return count;
    }
}
```
![image](https://github.com/user-attachments/assets/93f80783-3fcc-47a1-b125-38b3a147a4b0)

### 35)Find nth root of m:
```java

import java.math.*;
class Solution {
    public int nthRoot(int n, int m) {
        double pow;
        for(int i = 1;i<=m;i++)
        {
          pow =  Math.pow(i,n);
          if(pow==m)
          {
              return i;
          }
          else if(pow>m) {
              break;
          }
        }
        return -1;
    }
}
```
![image](https://github.com/user-attachments/assets/67719fe4-db37-47c6-a75e-e04e71c1dca0)

### 36)Count Squares:
```java
import java.util.*;
class Solution {
    static int countSquares(int n) {
        int count = 0;
        for(int i = 1;i*i<n;i++)
        {
          count++;
        }
        return count;
    }
}
```
![image](https://github.com/user-attachments/assets/f8b9ccda-22dd-49e4-91b3-83c1886af3c9)
![image](https://github.com/user-attachments/assets/f74555d1-9bf7-46ba-9186-3e49a4398b7a)

 ### 37)Replace all 0's with 5:
```java
class Solution {
    int convertfive(int num) {
        if(num == 0)
        {
            return 5;
        }
        int a;
        int result = 0;
        int place = 1;
        while(num!=0)
        {
            a = num%10;
            if(a==0)
            {
               a=5;
            }
            result = result+a*place;
            place = place * 10;
            num = num/10;
        }
        return result;
    }
}
```
![image](https://github.com/user-attachments/assets/f773b2b6-6678-4116-b431-756ee0640374)

### 38)Count ways to N'th Stair(Order does not matter):
```java
class Solution {
    public int nthStair(int n) {
        return (n / 2) + 1;
    }
}
```
![image](https://github.com/user-attachments/assets/625c7d23-845c-4a91-b91b-7888cc8103c1)

### 39)Precise Format - Java:
```java
class Solution {
    static ArrayList<Float> divisionWithPrecision(float a, float b) {
        float ans1 = a/b;
        float ans2 = Float.parseFloat(String.format("%.3f",ans1));
        return new ArrayList<>(Arrays.asList(ans1,ans2));
    }
}
```
![image](https://github.com/user-attachments/assets/bce67073-e3a5-4b7f-a022-5f7370a63360)

### 40)Divisibility by 8:
```java
class Solution {
    int DivisibleByEight(String s) {
         int len = s.length();
         String lastthree;
         if(len<3)
         {
             lastthree = s;
         }
         else{
             lastthree = s.substring(len - 3);
         }
         int number = Integer.parseInt(lastthree);
         if(number%8==0)
         {
             return 1;
         }
         else {
             return -1;
         }
    }
}
```
![image](https://github.com/user-attachments/assets/d66a1716-c124-4b2e-93e1-070e71244d79)

### 41)Remainder on dividing by 11:
```java
// User function Template for Java
import java.util.*;
import java.math.*;
class Solution {
    static int xmod11(String x) {
        BigInteger bigint = new BigInteger(x);
        BigInteger mod = bigint.mod(BigInteger.valueOf(11));
        return mod.intValue();
    }
}
```
![image](https://github.com/user-attachments/assets/783b2df3-c99f-4f09-ad12-23d6105dc10d)

### 42)Number of occurrence:
```java
class Solution {
    int countFreq(int[] arr, int target) {
        // code here
        int count = 0;
        for(int i = 0;i<arr.length;i++)
        {
            if(arr[i] == target)
            {
                count++;
            }
        }
        return count;
    }
}
```
![image](https://github.com/user-attachments/assets/b3d159bc-e642-4185-9779-b15f955b34c1)

### 43)Check if array is sorted:
```java
class Solution {
    public boolean arraySortedOrNot(int[] arr) {
        for(int i = 0;i<arr.length - 1;i++)
        {
            if(arr[i]>arr[i + 1])
            {
                return false;
            }
        }
        return true;
    }
}
```
```java
class Solution {
    public boolean arraySortedOrNot(int[] arr) {
        int[] copy = Arrays.copyOf(arr,arr.length);
        Arrays.sort(copy);
        for(int i = 0;i<arr.length;i++)
        {
            if(arr[i] != copy[i])
            {
                return false;
            }
        }
        return true;
    }
}
```
![image](https://github.com/user-attachments/assets/4e7bbed8-e052-4db0-bca9-c143d7f971eb)

### 44)Multiply Array:
```java
class Solution {
    public static int product(int arr[], int n) {
        int prod = 1;
        for(int i = 0;i<n;i++)
        {
            prod = prod * arr[i];
        }
        return prod;
    }
}
```
<img width="423" height="556" alt="image" src="https://github.com/user-attachments/assets/8a848c94-8bca-4edc-bed1-db0db01af697" />

### 45)Second Largest
```java
class Solution {
    public int getSecondLargest(int[] arr) {
        int n = arr.length;
        int max = arr[0];
        int second = -1;
        for(int i = 0;i<n;i++)
        {
            if(arr[i]>max)
            {
                second = max;
                max = arr[i];
            }
            else if(arr[i]>second && arr[i]<max)
            {
                second = arr[i];
            }
        }
        return (second==-1)?-1:second;
    }
}
```
<img width="915" height="527" alt="image" src="https://github.com/user-attachments/assets/b848b651-870d-46c5-b27d-4f45199f7b35" />

### 46)Find the Frequency:
```java
class Solution {
    int findFrequency(int arr[], int x) {
        int count = 0;
        for(int i = 0;i<arr.length;i++)
        {
            if(arr[i] == x)
            {
                count++;
            }
        }
        return count;
    }
}
```
<img width="587" height="315" alt="image" src="https://github.com/user-attachments/assets/813b082e-9901-4af9-a828-cd9e595fa947" />

### 47)Index of an Extra Element:
```java
class Solution {
    public int findExtra(int a[], int b[]) {
       int index = 0;
       int n1 = a.length;
       int n2 = b.length;
       for(int i = 0;i<n1;i++)
       {
           boolean found = false;
           for(int j = 0;j<n2;j++)
           {
               if(a[i] == b[j])
               {
                   found = true;
                   break;
               }
           }
           if(!found){
           index = i;
           }
       }
       return index;
    }
}
```
<img width="834" height="416" alt="image" src="https://github.com/user-attachments/assets/a6a485f7-50c0-42b2-a55c-3a94b0bf7ce0" />

### 48)Bitonic Point:
```java
class Solution {
    public int findMaximum(int[] arr) {
        int max = arr[0];
        int n = arr.length;
        for(int i = 0;i<n;i++)
        {
            if(arr[i]>max)
            {
                max = arr[i];
            }
        }
        return max;
    }
}
```
<img width="887" height="494" alt="image" src="https://github.com/user-attachments/assets/eb2b6d6d-73ee-4fbd-8316-d85426361f05" />

### 49)Java Arrays | Set 1:
```java
class Solution {
    public String average(int arr[]) {
        long n = arr.length;
        long sum = 0;
        for(int i = 0;i<n;i++)
        {
            sum = sum + arr[i]; 
        }
        double avg = (double)sum/n;
        return String.format("%.2f",avg);
    }
}
```
<img width="887" height="281" alt="image" src="https://github.com/user-attachments/assets/69c6449a-9d24-4c67-84cf-bd40b752b991" />

### 50)Missing in Array:
```java
class Solution {
    int missingNum(int arr[]) {
        long n = arr.length;
        long add = n + 1;
        long sum = 0;
        long total = add * (add + 1) / 2;
        for(int i = 0;i<n;i++)
        {
            sum = sum + arr[i];
        }
        long missing = total - sum;
        return (int)missing;
    }
}
```
<img width="756" height="442" alt="image" src="https://github.com/user-attachments/assets/cd7dc906-728b-4590-964f-86b4cde417c9" />

### 51)Reverse an Array:
```java
class Solution {
    public void reverseArray(int arr[]) {
        int n = arr.length;
        int left = 0;
        int right = n - 1;
        while(left<right)
        {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left ++ ;
            right --;
        }
    }
}
```
<img width="916" height="519" alt="image" src="https://github.com/user-attachments/assets/cbeb8305-fa99-45e6-995d-2b72390144ac" />

### 52)Minimum Number in a sorted rotated array:
```java
class Solution {
    static int minNumber(int arr[], int low, int high) {
       int n = arr.length;
       int min = arr[0];
       for(int i = 0;i<n;i++)
       {
           if(arr[i]<min)
           {
               min = arr[i];
           }
       }
        return  min;
    }
}
```
<img width="452" height="599" alt="image" src="https://github.com/user-attachments/assets/73aa855f-da7b-493d-bba1-9eba5d2938a5" />

### 53)Facing the sun:
```java
class Solution {
    public int countBuildings(int[] arr) {
         int  n = arr.length;
         int max = arr[0];
         int count = 1;
         for(int i = 0;i<n;i++)
         {
             if(arr[i]>max)
             {
                 count++;
                 max = arr[i];
             }
         }
         return count;
    }
}
```
<img width="909" height="422" alt="image" src="https://github.com/user-attachments/assets/6ef27ec7-26ce-45d0-9442-a11e19690ec3" />
<img width="790" height="565" alt="image" src="https://github.com/user-attachments/assets/b7b64873-36a8-4f2e-b78f-2606961f9ca6" />











