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





