<h1><u><b>STRINGS</b></u></h1>
 
### 1.Count the length of the string:

```C
#include<stdio.h>
#include<string.h>
#define MAX_SIZE 1000
int main()
{
    char text[MAX_SIZE];
    int length;
    printf("Enter the string:");
    fgets(text,MAX_SIZE,stdin);
    text[strcspn(text,"\n")]='\0';
    length=strlen(text);
    printf("The length of the string is '%s' = %d\n",text,length);
    return 0;
}
```
![image](https://github.com/user-attachments/assets/3126bf2a-130c-47b6-a6ab-6297fcdf1c1e)
### 2.Program to copy string using strcpy() function:
```C
#include<stdio.h>
#include<string.h>
#define MAX_SIZE 1000
int main()
{
    char text1[MAX_SIZE],text2[MAX_SIZE];
    printf("Enter the string:");
    fgets(text1,MAX_SIZE,stdin);
    strcpy(text2,text1);
    printf("The first string is:%s",text1);
    printf("The second string is:%s",text2);
    return 0;
}
```
![image](https://github.com/user-attachments/assets/63607ebd-9edc-4f3d-b6dc-d6f95ce85cfe)
### 3.Program to concatenate two strings using strcat() function
```C
#include<stdio.h>
#include<string.h>
#define MAX_SIZE 1000
int main()
{
    char str1[MAX_SIZE],str2[MAX_SIZE];
    printf("Enter the first string:");
    fgets(str1,MAX_SIZE,stdin);
    str1[strcspn(str1,"\n")]='\0';
    printf("Enter the second string:");
    fgets(str2,MAX_SIZE,stdin);
    str2[strcspn(str2,"\n")]='\0';
    strcat(str1," ");
    strcat(str1,str2);
    printf("The concatenated string is:%s",str1);
    return 0;
}
```
![image](https://github.com/user-attachments/assets/2a0c0fb1-d35f-44b1-8214-26f73bfafec6)
### 4.C program to compare strings using strcmp() function:
```C
#include<stdio.h>
#include<string.h>
#define MAX_SIZE 1000
int main()
{
    char str1[MAX_SIZE],str2[MAX_SIZE];
    int res;
    printf("Enter the first string:");
    fgets(str1,MAX_SIZE,stdin);
    str1[strcspn(str1,"\n")]='\0';
    printf("Enter the second string:");
    fgets(str2,MAX_SIZE,stdin);
    str2[strcspn(str2,"\n")]='\0';
    res=strcmp(str1,str2);
    if(res==0)
    {
        printf("Both strings ('%s' and '%s') are lexicographically equal.\n", str1, str2);
    }
    else if(res<0)
    {
        printf("The first string ('%s') is lexicographically smaller than the second string ('%s').\n",str1,str2);
    }
    else
    {
         printf("The first string ('%s') is lexicographically greater than the second string ('%s').\n",str1,str2);
    }
    return 0;
}
```
![image](https://github.com/user-attachments/assets/b2781726-4913-4c38-9ae4-d2b6ac1753e1)
### 5.C program to convert lowercase to uppercase and uppercase to lowercase:
```C
#include<stdio.h>
#include<ctype.h>
#define MAX_SIZE 1000
int main()
{
    char str[MAX_SIZE];
    int i;
    printf("Enter the string:");
    fgets(str,MAX_SIZE,stdin);
    printf("Toggeled Case:");
    for(i=0;str[i]!='\0';i++)
    {
        if(isupper(str[i]))
        {
            putchar(tolower(str[i]));
        }
        else if(islower(str[i]))
        {
            putchar(toupper(str[i]));
        }
        else
        {
            putchar(str[i]);
        }
    }
    return 0;
}
```
![image](https://github.com/user-attachments/assets/64fc9455-577b-4cdd-baf1-db352f503dad)
### 6.C program to Count the number of alphabets,digits and special characters in a string:
```C
#include<stdio.h>
#include<string.h>
#define MAX_SIZE 1000
int main()
{
    char str[MAX_SIZE];
    int alphabets,digits,others,i;
    alphabets=digits=others=i=0;
    printf("Enter the string:");
    fgets(str,MAX_SIZE,stdin);
    str[strcspn(str,"\n")]='\0';
    while(str[i]!='\0')
    {
        if((str[i]>='a' && str[i]<='z')||(str[i]>='A' && str[i]<='Z'))
        {
            alphabets++;
        }
        else if (str[i]>='0' && str[i]<='9')
        {
            digits++;
        }
        else
        {
            others++;
        }
        i++;
    }
    printf("Alphabets=%d\n",alphabets);
    printf("Digits=%d\n",digits);
    printf("Special Characters=%d\n",others);
    return 0;
}
```
![image](https://github.com/user-attachments/assets/5a4c3a3c-9278-4138-aaa1-fe2210d7e8df)
### 7.C program to convert lowercase string to uppercase
```
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#define MAX_SIZE 1000
int main()
{
    int i;
    char str[MAX_SIZE];
    printf("Enter the string:");
    fgets(str,MAX_SIZE,stdin);
    str[strcspn(str,"\n")]='\0';
    printf("The converted string:");
    for(i=0;str[i]!='\0';i++)
    {
        if(islower(str[i]))
        {
            putchar(toupper(str[i]));
        }
        else
        {
            putchar(str[i]);
        }
    }
    return 0;
}
```
![image](https://github.com/user-attachments/assets/2b32d406-2ca4-4c23-9768-ea0e30953831)







