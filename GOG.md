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
