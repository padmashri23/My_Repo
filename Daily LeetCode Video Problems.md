### 1.TWO SUM:
//Note this is not an optimal approach:
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {      
        int ans[]=new int[2];   
        for(int i=0;i<nums.length;i++)
        {
            for(int j=i+1;j<nums.length;j++)
            {
                if(nums[i]+nums[j]==target)     
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
![image](https://github.com/user-attachments/assets/8acf876d-37a9-45c3-b7ef-00a9f34b8195)
![image](https://github.com/user-attachments/assets/8baba236-cb08-4aee-ba17-a9166336bbda)  

