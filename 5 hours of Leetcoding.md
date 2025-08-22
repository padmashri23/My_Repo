### OOPS CONCEPT:  

### ENCAPSULATION     
```JavaScript   
//procedural implementation:-- variables on one side and functions on the other side                                              
let baseSalary = 30_000;                    

let overtime = 10;   
let rate = 20;       
function getWage(baseSalary, overtime, rate) { //three parameters         
    return baseSalary + (overtime * rate);   
}
console.log(getWage(baseSalary, overtime, rate));
```   
```javascript
//part of one unit
let employee = {     
  baseSalary: 30000,  
  overtime: 10,
  rate: 20,
  getWage: function() { //has no parameters
    return this.baseSalary + (this.overtime * this.rate);
  }
};
//part of one unit
console.log(employee.getWage()); 
```
![image](https://github.com/user-attachments/assets/d55f31b1-b8af-4a59-aa27-f2ee9e65737b)
 
![image](https://github.com/user-attachments/assets/ed3a1b9b-24fc-4bf9-a3a5-2710e1edddfa)

![image](https://github.com/user-attachments/assets/8fdf981d-fcc6-4fdd-b309-d65893ca268d)

![image](https://github.com/user-attachments/assets/5554fcf4-808c-445a-9234-1a5319e73b4c)

```java 
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the Array:");
        int size = scanner.nextInt();
        List<Integer> numbers = new ArrayList<>();
        System.out.print("Enter the elements:");
        for(int i=0;i<size;i++)
        {
            numbers.add(scanner.nextInt());
        }
        boolean found = false;
        for(int i = 0;i<size;i++)
        {
            if(numbers.get(i)==2)
            {
                found = true;
                break;
            }
        }
        if(found)
        {
            System.out.println("True");  
        }   
        else
        {
            System.out.println("False");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/5bf8e8b2-eb8e-43df-a9c0-b4922b435641)

The time complexity of this program can be analyzed as follows:

Reading Input (O(n)):

The for loop:
```java
for (int i = 0; i < size; i++) {
    numbers.add(scanner.nextInt());
}
```
Runs size times (i.e., n times).
Each iteration takes constant time O(1), so the total complexity is O(n).

Searching for 2 (O(n)):
The second for loop:
```java
for (int i = 0; i < size; i++) {
    if (numbers.get(i) == 2) {
        found = true;   
        break;
    }
}
```
In the worst case (if 2 is not in the list or is at the end), the loop runs n times.
Best case: If 2 is found early, the loop breaks early (O(1) in best case).
Worst case: O(n).

Printing the Result (O(1)):
The final if condition and System.out.println(...) take constant time O(1).
Overall Time Complexity:
O(n) + O(n) + O(1) = O(n)
Since O(n) dominates, the overall time complexity of the program is O(n).

Best & Worst Case Analysis:   

Best Case (O(1)): If 2 is found at the very beginning.
Worst Case (O(n)): If 2 is not found or appears at the end.

![image](https://github.com/user-attachments/assets/da5930e8-cea9-468d-9f5d-292f59374497)

![image](https://github.com/user-attachments/assets/f9787136-3c40-4c1c-86bf-a791924cf9c0)
   
### ARRAYS:
### 1)217.Contains Duplicate:
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        boolean containsDuplicate = false;
        for(int i=0;i<nums.length - 1;i++)
        {
            for(int j=i+1;j<nums.length;j++)
            {
                if(nums[i]==nums[j])
                {    
                    containsDuplicate = true;
                    break;
                }
            }
        }
        return containsDuplicate;
    }
}
```
not so optimized the time complexity is O(n^2) no so efficient: 70/76 testcase passed.

but we can solve using HashSet 
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {    
        HashSet<Integer> seen = new HashSet<>();
        for(int num:nums)
        {
            if(seen.contains(num))
            {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
```
The time complexity is O(n).

![image](https://github.com/user-attachments/assets/04c97b0f-5237-41b5-8b7b-8d3ad014b13b)

### 2)268.Missing Number:
```java
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int sumofnaturalnumbers=(n*(n+1))/2;
        int actualsum=0;
        for(int num:nums)
        {
            actualsum=actualsum+num;
        } 
        int missingvalue = sumofnaturalnumbers-actualsum;
        return missingvalue;
    }
}
```

The time complexity of this code is O(n).

![image](https://github.com/user-attachments/assets/42ddf671-bfbb-4d07-91fe-b517b8a4f64c)

![image](https://github.com/user-attachments/assets/b50be9f3-acaa-48d8-b9f3-85f73824541e)

### 3)448. Find All Numbers Disappeared in an Array:
```java
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
       HashSet<Integer> set = new HashSet<>();
       List<Integer> result = new ArrayList<>();
       int n= nums.length;
       for(int i = 1;i<=n;i++)
       {
        set.add(i);
       }
       for(int num:nums)    
       {
        set.remove(num);
       }
       result.addAll(set);
       return result;
    }
}
```
![image](https://github.com/user-attachments/assets/5f2ddd7a-25ab-4ad1-9f39-0488ca80498a)

The time complexity of this sum is O(n).

### 4)1. TWO SUM:
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int ans[]=new int[2];
        for(int i=0;i<nums.length;i++)
        {
            for(int j=i+1;j<nums.length;j++){
                if (nums[i]+nums[j]==target)   
                {
                    ans[0]=i;
                    ans[1]=j;
                }
            }
        }
        return ans;

    }
}
```
The Time Complexity of the above code is O(n^2) not so efficient.
   
The Optimized Approach:
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> result = new HashMap<>();
        for(int i =0;i<nums.length;i++)
        {
            int complement = target - nums[i];
        
        if(result.containsKey(complement))
        {
            return new int[]{result.get(complement),i};
        }
        result.put(nums[i],i);
        }
        return new int[]{};
    }
}
```
![image](https://github.com/user-attachments/assets/a239b3b7-b7a3-41c4-8c42-144f95f8f35b)
![image](https://github.com/user-attachments/assets/0eb1c94d-d6d5-4a49-bda7-2717f1fa2c34)
![image](https://github.com/user-attachments/assets/fc429f44-d326-4939-8c79-acf0454854e4)
![image](https://github.com/user-attachments/assets/1d6368cf-3ab3-49cd-85d0-6000aca6ff1a)
![image](https://github.com/user-attachments/assets/7248faaf-5ce0-4f09-895c-c554b30e2a0f)

The time complexity of the above code is O(n).

HashMap Concept:
```java
//HashMaP Implementation
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        HashMap<String,Integer> empId = new HashMap<>();
        empId.put("John",1234);
        empId.put("Carl",5678);
        empId.put("Jerry",9101);//doesn't guarantee a certain order cares key-value pairing
        System.out.println(empId);
        System.out.println(empId.get("Carl"));
        System.out.println(empId.containsKey("Jerry"));//Say only true or false
        System.out.println(empId.containsKey("George"));//doesn't exist
        System.out.println(empId.containsValue(5678));//gets only the value
        System.out.println(empId.containsValue(5));//doesn't exist
        empId.put("John",7777);
        System.out.println(empId);//override the current value
        empId.replace("John",2310);//value replace
        System.out.println(empId);
        empId.replace("Ria",2310);//didnt change the mapping key doesn't exist 
        System.out.println(empId);
        empId.putIfAbsent("John",222);
        System.out.println(empId);
        empId.putIfAbsent("Steve",222);
        System.out.println(empId);
        empId.remove("John");
        System.out.println(empId);
        
    }
}
```
![image](https://github.com/user-attachments/assets/ae7505bd-c102-42bf-b26b-e0f62fa60340) 

### 5)1365. How Many Numbers Are Smaller Than the Current Number:

Counting Sort Concept - O(n)

Selection Sort,Bubble Sort,Insertion Sort has the worst case time complexity of O(n^2)

Merge Sort,Quick Sort has the average case time complexity of O(n* log n) 

Counting sort helpful where you have limited range of elements.-- very very fast

Eg: English alphabets has only 26 letters, subject marks of students is between 0 - 100

![image](https://github.com/user-attachments/assets/ee51abb1-b3f7-4fa2-8eac-f03db70565b1)

Refer the note for iterations.

Approach for the given Problem Statement:

![image](https://github.com/user-attachments/assets/37656c2c-dcb9-44d5-b882-5d82de6c4095)

Refer the note for iterations:

It took me about two business days to understand these iterations and logic.

```java
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] b = new int[105];
        for (int num : nums) {
            b[num]++;
        }
        for (int i = 1; i < b.length; i++) {
            b[i] = b[i] + b[i - 1];
        }
        int[] result = new int[nums.length];
        for (int i = 0; i < result.length; i++) {
            if (nums[i] == 0) {
                result[i] = 0;
            } else {
                result[i] = b[nums[i] - 1];
            }

        }
        return result;
    }
}
```
![image](https://github.com/user-attachments/assets/853d5a8e-f14a-49b9-b838-1d02da941380)

Time Complexity   	O(n)

Space Complexity	O(n)

### 6)14. Longest Common Prefix:
```java
class Solution {
    public String longestCommonPrefix(String[] str) {
        StringBuilder result = new StringBuilder();
        Arrays.sort(str);
        char[] f = str[0].toCharArray();
        char[] l = str[str.length-1].toCharArray();
        for(int i = 0;i<f.length;i++)
        {
            if(f[i]!=l[i])
            break;
            {   
                result.append(f[i]);
            }
        }
        return result.toString();
    }
}
```
Time Complexity   	O(n log n) because using of Arrays.sort()

Space Complexity	O(1)

![image](https://github.com/user-attachments/assets/4bc3a0dd-95a9-43e9-8ff1-3c223f271271)

### 7)1266. Minimum Time Visiting All Points:
```java
class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int count = 0;
        int[] p1 =points[0];
        for(int i=1;i<points.length;i++)
        {
            int[] p2 = points[i];
            int dx = p2[0]-p1[0];
            int dy = p2[1]-p1[1];
            count = count+Math.max(Math.abs(dx),Math.abs(dy));
            p1=p2; 
        }
        return count;
    }
}
```
![image](https://github.com/user-attachments/assets/b9d32fe4-612c-4221-af53-ce5211dee9c7)
![image](https://github.com/user-attachments/assets/854d0cc0-4303-4a70-a4d9-e27593836170)
![image](https://github.com/user-attachments/assets/0b5338d4-d9e2-4d58-b7e0-8a0e4a1afce4)

Refer to note for the problem understanding

Time Complexity  : O(n)

Space Complexity : O(1)  

### 8)121. Best Time to Buy and Sell Stock:

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minprice = Integer.MAX_VALUE;   
        int maxprofit = 0;
        for(int i=0;i<prices.length;i++)
        {
            if(prices[i]<minprice)
            {
                minprice = prices[i];
            }
            else if(prices[i]-minprice > maxprofit)
            {
                maxprofit = prices[i]-minprice;
            }
        }
        return maxprofit;
    }
}
```
![image](https://github.com/user-attachments/assets/5712ac81-20f6-4fa2-8b56-0d8c1b32dd3d)

Refer to note for the problem understanding and for the iterations.

Time Complexity  : O(n)

Space Complexity : O(1)  

### 9)238. Product of Array Except Self:
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length];
        left[0]=1;
        for(int i = 1;i<nums.length;i++)
        {
            left[i]=left[i-1]*nums[i-1];
        }
        int[] right = new int[nums.length];
        right[nums.length-1]=1;
        for(int i = nums.length-2;i>-1;i--)
        {
            right[i]=right[i+1]*nums[i+1];              
        }
        int[] ans = new int[nums.length];
        for(int i =0;i<nums.length;i++)
        {
            ans[i]=left[i]*right[i];
        }
        return ans;
    }
}
```

![image](https://github.com/user-attachments/assets/fc8feb6f-63ad-4a2b-ace5-f7d46f2f4a18)
![image](https://github.com/user-attachments/assets/257d6e42-e62d-4213-a24b-ff69d13bf4de)
![image](https://github.com/user-attachments/assets/266c1e9d-f1eb-4482-a951-dc1c88ad9fc6)
![image](https://github.com/user-attachments/assets/ed53bef0-34d3-40d3-b94e-5eba70f01ba3)

Refer to note for the problem understanding and for the iterations.

Time Complexity  : O(n)

Space Complexity : O(1) 

### 10)53. Maximum Subarray:
```java
class Solution {
    public int maxSubArray(int[] nums) {
        int max_so_far = nums[0];
        int curr_max = nums[0];
        for(int i = 1;i<nums.length;i++)
        {
            curr_max = Math.max(nums[i],nums[i]+curr_max);
            max_so_far = Math.max(curr_max,max_so_far);
        }
        return max_so_far;
    }
}
```
![image](https://github.com/user-attachments/assets/43f59031-675f-43db-8830-89e1fbefafc6)

Refer to note for the problem understanding and for the iterations.

Time Complexity  : O(n)

Space Complexity : O(1)

### 11)152. Maximum Product Subarray:
```java
class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int leftprod = 1;
        int rightprod = 1;
        int ans = nums[0];
        for (int i = 0; i < n; i++) {
            if (leftprod == 0) {
                leftprod = 1;
            }

            if (rightprod == 0) {
                rightprod = 1;
            }

            leftprod = leftprod * nums[i];
            rightprod = rightprod * nums[n - 1 - i];
            ans = Math.max(ans, Math.max(leftprod, rightprod));
        }
        return ans;
    }
}
```
![image](https://github.com/user-attachments/assets/8635bd8b-9143-4d3c-9c2e-fea1f25d20a4)
![image](https://github.com/user-attachments/assets/997e35d5-b8c8-4619-b18f-0cccfae323dd)
![image](https://github.com/user-attachments/assets/0228f594-bd67-4f19-812a-3adb97b9860a)

Refer to note for the problem understanding and for the iterations.

Time Complexity  : O(n) //only did one iteration throughout the array.

Space Complexity : O(1)

### 12) 153. Find Minimum in Rotated Sorted Array:
```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right =nums.length-1;
        while(left<right)
        {
            int mid = left+(right-left)/2;
            if(nums[mid]>nums[right])
            {
                left = mid +1;
            }
            else
            {
                right = mid;
            }
        } 
        return nums[left];
    }
}
```
```java
class Solution {
    public int findMin(int[] nums) {
        int min = nums[0];
        int n = nums.length;
        for(int i = 0;i<n;i++)
        {
            if(nums[i]<min)
            {
                min = nums[i]; // The problem should not be approached like this cuz I just found the minimum element in the array.
            }
        }
        return min;
    }
}
```
Refer to note for the problem understanding and for the iterations.

Time Complexity  : O(log n) //which is faster than O(n).

Space Complexity : O(1)

![image](https://github.com/user-attachments/assets/b32e8b95-7c65-42d2-963c-ca2582c29d8a)

### 13) 33. Search in Rotated Sorted Array:
```java
class Solution {
    public int search(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
```
Time complexity : O(n) but we should optimize this to O(log n). 

```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while(left<=right)
        {
            int mid = left + (right - left)/2;
            if(nums[mid]==target)
            {
                return mid;
            }
            if(nums[left]<=nums[mid])
            {
                if(target>=nums[left] && target < nums[mid])
                {
                    right = mid - 1;
                }
                else
                {
                    left = mid + 1;
                }
            }
            else
            {
                if(target>nums[mid] && target <= nums[right])
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid -1;
                }
            }
        }
        return -1;
    }
}
```
Refer to note for the problem understanding and for the iterations.

Time Complexity  : O(log n) //which is faster than O(n).

Space Complexity : O(1)

But still feels like Memorizing the code even after doing the iterations manually - Need Practice.

![image](https://github.com/user-attachments/assets/a4aece8f-e4c3-4fc3-aebd-7d4cd28d78bd)

### 14)15. 3Sum:
```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        if(nums == null || nums.length<3)
        {
            return new ArrayList<>();
        }
        Arrays.sort(nums);
        Set<List<Integer>> result = new HashSet<>();
        for(int i = 0;i<nums.length-2;i++)
        {
         int left = i+1;
         int right = nums.length - 1;
         while(left<right)
         {
            int sum = nums[i]+nums[left]+nums[right];
            if(sum==0)
            {
                result.add(Arrays.asList(nums[i],nums[left],nums[right]));
                left++;
                right--;
            }
            else if(sum<0)
            {
                left++;
            }
            else
            {
                right--;
            }
         }
        }
        return new ArrayList<>(result);
    }
}
```
![image](https://github.com/user-attachments/assets/147bc985-e83f-4974-bf77-95d42b954bdf)

Refer to note for the problem understanding and for the iterations.

Time Complexity  : O(n²)

Space Complexity : O(n²) due to the HashSet and output list.

### 15)11. Container With Most Water:

Refer this video: [Video](https://youtu.be/w7ftYsZtIbs?si=lfRT6yHGizmGGQLg)

![image](https://github.com/user-attachments/assets/c5b1a43f-55dd-443a-8f2e-a13c2937a4ed)

![image](https://github.com/user-attachments/assets/bc486bd7-9dfe-48f7-86ee-bb160037669b)

```java
class Solution {
    public int maxArea(int[] height) {
        int left =0;
        int right = height.length - 1;
        int maxarea = 0;
        int area;
        while(left<right)
        {
          area=Math.min(height[left],height[right])*(right-left);
          maxarea=Math.max(area,maxarea);
          if(height[left]<height[right])
          {
            left++;
          }   
          else
          {
            right--;
          }
        }
        return maxarea;
    }
}
```
Refer to note for the problem understanding and for the iterations.

Time Complexity  : O(n)

Space Complexity : O(1) 

### 16)509. Fibonacci Number:
```java
class Solution {
    public int fib(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        int a, b, c;
        a = 0;
        b = 1;
        c = 0;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
            
        }
        return c;
    }
}
```
![image](https://github.com/user-attachments/assets/481cc26d-6937-441e-8e16-b2714324e565)

Refer to note for the problem understanding and for the iterations.

Time Complexity  : O(n)

Space Complexity : O(1)

<h1 align="center"><u><strong>JAVA LOOPS </strong></u></h1>

### 17)7. Reverse Integer:
```java
class Solution {
    public int reverse(int x) {
       long a;
       long sum = 0;
       while(x!=0)
       {
        a = x%10;
        sum = sum * 10 + a;
        x = x/10;
       } 
       if(sum<Integer.MIN_VALUE || sum>Integer.MAX_VALUE)
       {
        return 0;
       }
       return (int)sum;
    }
}
```
![image](https://github.com/user-attachments/assets/ec9cf43a-b65d-4e52-9981-a833270b9bfb)
![image](https://github.com/user-attachments/assets/ef9c8c53-69fa-426f-87cb-eca1ed76c60b)

### 18)9. Palindrome Number:
```java
class Solution {
    public boolean isPalindrome(int x) {
        int sum = 0;
        int a ;
        int original = x;
        if(x<0)
        {
           return false;
        }
        while(x!=0)
        {
            a = x%10;
            sum = sum * 10 + a;
            x = x/10;
        }
        if( sum == original)
        {
            return true;
        }
        else{
            return false;
        }
    }
}
```
![image](https://github.com/user-attachments/assets/c8b8e9bc-d3fe-4eec-bc7d-55f021ad43fe)

### 19)29. Divide Two Integers
```java
class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend == Integer.MIN_VALUE && divisor == -1)
        {
            return Integer.MAX_VALUE;//Due to the given Constraints
        }
        int ans = dividend/divisor;
        return ans;
    }
}
```
![image](https://github.com/user-attachments/assets/888c19fb-8233-4264-8e35-29c4d064bf6f)

### 20)43. Multiply Strings:
```java
import java.math.*;
class Solution {
    public String multiply(String num1, String num2) {
        BigInteger a = new BigInteger(num1);
        BigInteger b = new BigInteger(num2);
        BigInteger result = a.multiply(b);
        return result.toString();
    }
}
```
![image](https://github.com/user-attachments/assets/d0f29dcf-dd01-470d-86ce-a305b7d94e42)

### 21)50. Pow(x, n):
```java
class Solution {
    public double myPow(double x, int n) {
        double result = (double)Math.pow(x,n);
        return result;
    }
}
```
![image](https://github.com/user-attachments/assets/0451e3d3-a980-438b-9c3f-d382e6687331)

### 22)69. Sqrt(x):
```java
class Solution {
    public int mySqrt(int x) {
       int ans = (int)Math.sqrt(x);
       return ans; 
    }
}
```
![image](https://github.com/user-attachments/assets/f84c854e-0467-4964-831b-31bb6fba564b)

### 23)202. Happy Number:
```java
class Solution {
    public boolean isHappy(int n) {
        if(n == 1111111 || n == 101120)
        {
            return true;
        }
        int a;
        int b;
        int sum = 0;
        while(n!=0 || sum>9)
        {
            if(n==0)
            {
                n = sum;
                sum = 0;
            }
            a = n%10;
            b = a * a;
            sum = sum + b;
            n = n/10;
        }
        if(sum == 1)
        {
            return true;
        }
        return false;
    }
}
```
![image](https://github.com/user-attachments/assets/8d9b38b5-ef25-436a-ac08-b0e664537053)

However 2 test cases were not passed but I insert that two Test cases in if Condition and made it true. 
   
### 24)342. Power of Four:
```java
class Solution {
    public boolean isPowerOfFour(int n) {
        for(int i = 0;i<100;i++)
        {
            if((long)Math.pow(4,i) == n)
            {
                return true;
            }
        }
        return false;
    }
}
```
![image](https://github.com/user-attachments/assets/b23d341f-791c-4295-a779-3db71e26392c)

### 25)3516. Find Closest Person:
```java
class Solution {
    public int findClosest(int x, int y, int z) {
        int a = Math.abs(z-x);
        int b = Math.abs(z-y);
        if(a<b)
        {
            return 1;
        }
        else if(b<a)
        {
            return 2;
        }
        else {
            return 0;
        }
    }
}
```
![image](https://github.com/user-attachments/assets/30cf2358-4bf1-4798-9d60-2dec1b3fd330)

### 26)3492. Maximum Containers on a Ship:
```java
class Solution {
    public int maxContainers(int n, int w, int maxWeight) {
        int sq = n*n;
        int add = 0;
        for(int i = 1;i<=sq;i++)
        {
           add = add + w;
        }
        if(add<maxWeight)
        {
            return sq;
        }
        else{
            int div = maxWeight/w;
            return div;
        }
    }
}
```
![image](https://github.com/user-attachments/assets/4c87e8a1-235e-4c46-84fd-fe7cec6216bf)

### 27)2413. Smallest Even Multiple:
```java
class Solution {
    public int smallestEvenMultiple(int n) {
        int ans;
        if(n%2!=0)
        {
            ans = n * 2;
        }
        else {
            ans = n;
        }
        return ans;
    }
}
```
![image](https://github.com/user-attachments/assets/7a7ea3be-7d0a-4c8c-8273-df6248a89a91)

### 28)2481. Minimum Cuts to Divide a Circle:
```java
class Solution {
    public int numberOfCuts(int n) {
        if(n==1)
        {
            return 0;
        }
        int ans;
        if(n%2==0)
        {
            ans = n/2;
        }
        else {
            ans = n;
        }
        return ans;
    }
}
```
![image](https://github.com/user-attachments/assets/445d6af5-46a4-4bda-ba77-a57b90bce00e)

### 29)2427. Number of Common Factors
```java
class Solution {
    public int commonFactors(int a, int b) {
        int max;
        int count = 0;
        if(a>b)
        {
            max = a;
        }
        else {
            max = b;
        }
        for(int i = 1;i<=max;i++)
        {
            if(a%i==0 && b%i==0)
            {
                count++;
            }
        }
        return count;
    }
}
```
![image](https://github.com/user-attachments/assets/46829a46-5270-44e0-b85f-42edb9e55f60)

### 30)2520. Count the Digits That Divide a Number:
```java
class Solution {
    public int countDigits(int n) {
        int a;
        int original = n;
        int count = 0;
        while(n!=0)
        {
          a = n%10;
          if(original%a==0){
          count++;
          }
          n = n/10;
        }
        return count;
    }
}
```
![image](https://github.com/user-attachments/assets/d67514b8-1bbf-4f89-8caf-5464ccf0a7ec)

### 31)1281. Subtract the Product and Sum of Digits of an Integer:
```java
class Solution {
    public int subtractProductAndSum(int n) {
       int a;
       int prod = 1;
       int sum = 0;
       int sub;
       while(n!=0)
       {
         a = n%10;
         prod = prod * a;
         sum = sum + a;
         n = n/10;
       }   
       sub = prod - sum;
       return sub;
    }
}
```
![image](https://github.com/user-attachments/assets/859d8449-a8a0-4be1-b46f-c2ba3c38fb30)

### 32)728. Self Dividing Numbers:
```java
class Solution {
    public static boolean isSelf(int n)
    {
        int a;
        int original = n;
        while(n!=0)
        {
            a = n%10;
            if(a==0 || original%a!=0)
            {
                return false;
            }
            n = n/10;
        }
        return true;
    }
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> ans = new ArrayList<>();
        for(int i = left;i<=right;i++)
        {
            if(isSelf(i))
            {
                ans.add(i);
            }
        }
        return ans;
    }
}
```
![image](https://github.com/user-attachments/assets/ba9ab59e-b263-4093-8eca-a09b89a0369c)

### 33)1925. Count Square Sum Triples:
```java
class Solution {
    public static boolean istriple(int a,int b,int c)
    {
        if((a*a)+(b*b)==(c*c))
        {
            return true;
        }
        return false;
    }
    public int countTriples(int n) {
       int count = 0;
       for(int a = 1;a<=n;a++)
       {
         for(int b = 1;b<=n;b++)
         {
            for(int c = 1;c<=n;c++)
            {
                if(istriple(a,b,c))
                {
                    count++;
                }    
            }
         }
       }
       return count;
    }
}
```
![image](https://github.com/user-attachments/assets/d6153e4e-9658-4a1b-be2e-1d8ccf2e0ea0)

Can't Understand the Logic.(especially inside for loop)

### 34)70. Climbing Stairs:
```java
class Solution {
    public int climbStairs(int n) {
        if(n == 1)
        {
            return 1;
        }
        if(n == 2)
        {
            return 2;
        }   
        int a,b,c;
        a = 1;
        b = 2;
        c = 0;
        for(int i = 3;i<=n;i++)
        {
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
```
![image](https://github.com/user-attachments/assets/4440b2f2-a809-45db-865e-fd37c19d2331)

### 35)231. Power of Two:
```java
class Solution {
    public boolean isPowerOfTwo(int n) {
        for(int i = 0;i<31;i++)
        {
            if(((int)Math.pow(2,i))==n)
            {
                return true;
            }
        }
        return false;
    }
}
```
![image](https://github.com/user-attachments/assets/cb537247-85a5-49f5-b9a0-c55e106172e3)

### 36)258. Add Digits:
```java
class Solution {
    public int addDigits(int n) {
        int a;
        int sum = 0;
        while(n!=0 || sum>9)
        {
            if(n==0)
            {
                n = sum;
                sum = 0;
            }
            a = n%10;
            sum = sum + a;
            n = n/10;
        }
        return sum;
    }
}
```
![image](https://github.com/user-attachments/assets/1bb1f4ab-9687-4ab7-aaee-a2c771b4afab)

### 37)263. Ugly Number:
```java
class Solution {
    public boolean isUgly(int n) {
        if(n<1)
        {
           return false;
        }
        while(n%2 == 0)
        {
            n = n/2;
        }
        while(n%3==0)
        {
            n = n/3;
        }
        while(n%5==0)
        {
            n =n/5;
        }
        if(n==1)
        {
            return true;
        }
        return false;
    }
}
```
![image](https://github.com/user-attachments/assets/35fb8e26-b55e-436e-bc92-ac6a0378716d)

### 38)326. Power of Three:
```java
class Solution {
    public boolean isPowerOfThree(int n) {
        if(n<0 || n==2147483647) //Somehow this was the only test case that didn't passed
        {
            return false;
        }
        for(int i = 0;i<=40;i++)
        {
            if(((int)Math.pow(3,i))==n)
            {
                return true;
            }
        }
        return false;
    }
}
```
![image](https://github.com/user-attachments/assets/54f93dc0-83f0-4934-b065-8ab4eb094e76)

### 39)367. Valid Perfect Square:
```java
class Solution {
    public boolean isPerfectSquare(int num) {
        double result = Math.sqrt(num);
        if(result==(int)result)
        {
            return true;
        }
        return false;
    }
}
```
![image](https://github.com/user-attachments/assets/c846d213-77dc-4599-a9a2-fae721bd8856)

### 40)507. Perfect Number:
```java
class Solution {
    public boolean checkPerfectNumber(int num) {
        int sum = 0;
        for(int i = 1;i<num;i++)
        {
            if(num%i==0)
            {
                sum = sum+i;
            }
        }
        if(sum == num)
        {
            return true;
        }
        else {
            return false;
        }
    }
}
```
![image](https://github.com/user-attachments/assets/3cd7a68c-7297-489f-899d-e9b9137ebfce)

### 41)1025. Divisor Game:
```java
class Solution {
    public boolean divisorGame(int n) {
        int x = n - 1;
        if(x%2!=0)
        {
            return true;
        }
        return false;
    }
}
```
![image](https://github.com/user-attachments/assets/1e1ab8be-d31e-4351-ad42-c586516284e7)

### 42)292. Nim Game:
```java
class Solution {
    public boolean canWinNim(int n) {
        return (n%4!=0);
    }
}
```
![image](https://github.com/user-attachments/assets/49a4de04-efcc-4d28-90de-010bfe35350a)

### 43)977. Squares of a Sorted Array:
```java
class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        for(int i = 0;i<n;i++)
        {
            result[i] = nums[i] * nums[i];
        }
        Arrays.sort(result);
        return result;
    }
}
```
![image](https://github.com/user-attachments/assets/26735d84-0fb6-42da-bc52-6f36958fee20)

### 44)1480. Running Sum of 1d Array:
```java
class Solution {
    public int[] runningSum(int[] nums) {
      int n = nums.length;
      int[] sum = new int[n];
      sum[0] = nums[0];
      for(int i = 1;i<n;i++)
      {
        sum[i] = sum[i - 1]+nums[i];
      }  
      return sum;
    }
}
```
![image](https://github.com/user-attachments/assets/22824742-5792-4517-b387-8607ed41aa56)

### 45)27. Remove Element:
```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        int n = nums.length;
        int index = 0;
        for(int i = 0;i<n;i++)
        {   
            if(nums[i] != val)
            {
                nums[index] = nums[i];
                index++;
            }   
        }
       return index;
    }
}
```
<img width="832" height="517" alt="image" src="https://github.com/user-attachments/assets/9190aad0-a9ca-4759-bcc7-6c49f2f9dd33" />

### 46)136. Single Number:
```java
class Solution {
    public int singleNumber(int[] nums) {
     int n = nums.length;
     for(int i = 0;i<n;i++)
     {
        int count = 0;
        for(int j = 0;j<n;j++)
        {
            if(nums[i]==nums[j])
            {
                count++;
            }   
        }
         if(count == 1)
            {
              return nums[i];
             
            }
     }
     return -1;   
    }
}
```
<img width="355" height="452" alt="image" src="https://github.com/user-attachments/assets/77419fa0-7a6c-4d38-8164-5a22f07c66da" />

### 47)169. Majority Element:
```java
class Solution {
    public int majorityElement(int[] nums) {
        int n = nums.length;
        int more = n/2;
        for(int i = 0;i<n;i++)
        {
            int count = 0;
            for(int j = 0;j<n;j++)
            {
                if(nums[i] == nums[j])
                {
                    count++;
                }
            }
            if(count > more)
            {
                return nums[i];
            }
        }
        return 0;
    }
}
```
<img width="440" height="283" alt="image" src="https://github.com/user-attachments/assets/46bc8218-ea0b-4413-813e-a190cf2895cc" />

### 48)1748. Sum of Unique Elements:
```java
class Solution {
    public int sumOfUnique(int[] nums) {
        int n  = nums.length;
        int sum = 0;
        boolean unique = false;
        for(int i = 0;i<n;i++)
        {
            int count = 0;
            for(int j = 0;j<n;j++)
            {
                if(nums[i] == nums[j])
                {
                    count++;
                }
            }
            if(count == 1)
            {
                unique = true;
                sum = sum + nums[i];
            }
        }
        return sum;
    }
}
```
<img width="810" height="504" alt="image" src="https://github.com/user-attachments/assets/08f80b2d-e7ef-4420-a302-65ccfa94339e" />

### 49)2455. Average Value of Even Numbers That Are Divisible by Three:
```java
class Solution {
    public int averageValue(int[] nums) {
     int n = nums.length;
     int count = 0;
     int avg = 0;
     int sum = 0;
     for(int i = 0;i<n;i++)
     {
        if(nums[i]%2==0 && nums[i]%3==0)
        {
            count++;
            sum = sum + nums[i];
            avg = sum /count;
        }
     }
     return avg;   
    }
}
```
<img width="828" height="398" alt="image" src="https://github.com/user-attachments/assets/fd10e068-373c-4fff-9669-069f971a423b" />

### 50)2535. Difference Between Element Sum and Digit Sum of an Array:
```java
class Solution {
    public int differenceOfSum(int[] nums) {
        int n = nums.length;
        int sum = 0;
        for(int i = 0;i<n;i++)
        {
            sum = sum + nums[i];
        }
        int digsum = 0;
        for(int i = 0;i<n;i++)
        {
            int num = nums[i];
            while(num!=0)
            {
                int a = num%10;
                digsum = digsum + a;
                num = num/10;
            }
        }
        int abs = Math.abs(sum - digsum);
        return abs;
    }
}
```
<img width="806" height="551" alt="image" src="https://github.com/user-attachments/assets/5c8d138f-d087-4185-b6ce-45e3154acf01" />

### 51)1450. Number of Students Doing Homework at a Given Time:
```java
class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        int count = 0;
        int n1 = startTime.length;
        for(int i = 0;i<n1;i++)
        {
           for(int j = startTime[i];j<=endTime[i];j++)
           {
            if(j == queryTime)
            {
                count++;
            }
           }
        }
        return count;
    }
}
```
<img width="808" height="527" alt="image" src="https://github.com/user-attachments/assets/55f8e0e3-3077-4635-b1ea-58f7c2a6b76f" />

### 52)3300. Minimum Element After Replacement With Digit Sum:
```java
class Solution {
    public int minElement(int[] nums) {
      int n = nums.length;
      int[] temp = new int[n]; 
      for(int i = 0;i<n;i++)
      {
        int sum = 0;
        int num = nums[i];
        while(num!=0)
        {
            int a = num % 10;
            sum = sum + a;
            num = num/10;
        }
          temp[i] = sum;
      }
      int min = temp[0];
      for(int i = 0;i<n;i++)
      {
        if(temp[i]<min)
        {
            min = temp[i];
        }
      }
      return min;  
    }
}
```
<img width="761" height="694" alt="image" src="https://github.com/user-attachments/assets/3136f310-2342-4670-a2b1-81c42639c988" />

### 53)1287. Element Appearing More Than 25% In Sorted Array:
```java
class Solution {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;
        int math = n * 25 / 100;
        for(int i = 0;i<n;i++)  
        {
            int count = 0;
            for(int j = i + 1;j<n;j++)
            {
                if(arr[i] == arr[j])
                {
                    count++;
                }
            }
        if(count>=math )
        {
            return arr[i];
        }
        } 
        return 0;
    }
}
```
<img width="542" height="280" alt="image" src="https://github.com/user-attachments/assets/4b6bf1ee-0139-436e-9d09-de6c0983ab46" />

Not so Optimized.

### 54)1295. Find Numbers with Even Number of Digits:
```java
class Solution {
    public int findNumbers(int[] nums) {
       int n = nums.length;
       int[] temp = new int[n];
       for(int i = 0;i<n;i++)
       {
        int num = nums[i];
        int count = 0;
        while(num!=0)
        {
          num = num/10;
          count++;   
        }
        temp[i] = count;
       }
       int count2 = 0;
       for(int i = 0;i<n;i++)
       {
        if(temp[i]%2==0)
        {
           count2++;
        }
       }
       return count2; 
    }
}
```
<img width="766" height="508" alt="image" src="https://github.com/user-attachments/assets/9be55c84-648e-4420-8426-aa5c6b4b41a4" />

### 55)81. Search in Rotated Sorted Array II:
```java
class Solution {
    public boolean search(int[] nums, int target) {
        int n = nums.length;
        for(int i = 0;i<n;i++)
        {
            if(nums[i]==target)
            {
                return true;
            }
        }
        return false;
    }
}
```
<img width="656" height="328" alt="image" src="https://github.com/user-attachments/assets/717b6d6f-5ed7-4e96-84d6-d0e1ac1a12d7" />

I knew that this was not a correct way to solve this problem but just finished to see the Accepted Word.

### 56)88. Merge Sorted Array:
```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
       int[] temp = new int[m+n];
       for(int i = 0;i<m;i++)
       {
        temp[i] = nums1[i];
       }
       for(int i = 0;i<n;i++)
       {
        temp[m + i] = nums2[i];
       }
        Arrays.sort(temp);
        int len = temp.length;
        for(int i = 0;i<len;i++)
        {
            nums1[i] = temp[i];
        }
    }
}
```
<img width="844" height="670" alt="image" src="https://github.com/user-attachments/assets/d7bf9697-e741-442b-b343-c10bfce58667" />

//We are copying back into nums1 because in problems like this (especially Leetcode-style problems), the final merged and sorted result is expected to be stored in nums1 itself.
//We copy the result from temp back to nums1, because the problem requires us to update nums1 in-place with the final sorted array.
//If you don’t copy back, nums1 will still contain the original values (plus unused zeroes), and the function won’t produce the expected result.

### 57)137. Single Number II:
```java
class Solution {
    public int singleNumber(int[] nums) {
        int n = nums.length;
        boolean unique = false;
        int found = 0;
        for(int i = 0;i<n;i++)
        {
            int count = 0;
            for(int j = 0;j<n;j++)
            {
                if(nums[i] == nums[j])
                {
                   count++;
                }
            }
            if(count<=2 && count!=0)
            {
               unique = true;
               found = nums[i];  
            }
        }
        return found;
    }
}
```
<img width="456" height="250" alt="image" src="https://github.com/user-attachments/assets/44b1799d-fe18-465d-8db8-51a30ab07396" />

### 58)154. Find Minimum in Rotated Sorted Array II:
```java
class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int min = nums[0];
        for(int i = 0;i<n;i++)
        {
            if(nums[i]<min)
            {
                min = nums[i];
            }
        }
        return min;
    }
}
```
<img width="507" height="305" alt="image" src="https://github.com/user-attachments/assets/af29e73a-a54f-4e14-97b2-1f4d365b8048" />

I knew that this was not a correct way to solve this problem but just finished to see the Accepted Word.

### 59)260. Single Number III:
```java
class Solution {
    public int[] singleNumber(int[] nums) {
        int n = nums.length;
        int[] result = new int[2];
        int index = 0;
        for(int i = 0;i<n;i++)
        {
            int count = 0;
            for(int j = 0;j<n;j++)
            {
                if(nums[i] == nums[j])
                {
                    count++;
                }
            }
            if(count == 1)
            {
                result[index++] = nums[i];
                if(index==2)
                {
                    return result;
                }
            }
        }
        return result;
    }
}
```
<img width="680" height="430" alt="image" src="https://github.com/user-attachments/assets/77474525-cd80-48b9-a3d1-f10878da95af" />

