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













