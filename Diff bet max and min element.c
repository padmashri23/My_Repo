#include<stdio.h>
#define MAX_SIZE 1000
int main()
{
    int i,n,arr[MAX_SIZE],max,min,diff;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    max=arr[0];
    min=arr[0];
    for(i=0;i<n;i++)
    {
        if(arr[i]>max)
        {
            max=arr[i];
        }
        if(arr[i]<min)
        {
            min=arr[i];   
        }
    }
    diff=max-min;
    printf("%d",diff);
    return 0;
}
