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





   

























 


















