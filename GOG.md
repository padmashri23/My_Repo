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



