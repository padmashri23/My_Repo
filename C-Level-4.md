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
### 3.Program to concatenate two strings using strcat() function:
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
### 7.C program to convert lowercase string to uppercase:
```C
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
### 8.C program to convert Uppercase string to lowercase:
```C
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
    printf("The converted string is:");
    for(i=0;str[i]!='\0';i++)
    {
        if(isupper(str[i]))
        {
            putchar(tolower(str[i]));
        }
        else
        {
            putchar(str[i]);
        }
    }
    return 0;
}
```
![image](https://github.com/user-attachments/assets/633cf936-dd47-492b-81d8-269bce26f2d8)
### 9.C program to count total number of vowels and consonants in a string:
```C
#include<stdio.h>
#include<string.h>
#define MAX_SIZE 1000
int main()
{
    int i,len,vowel,consonant;
    char str[MAX_SIZE];
    printf("Enter the string:");
    fgets(str,MAX_SIZE,stdin);
    str[strcspn(str,"\n")]='\0';        
    vowel=0;
    consonant=0;
    len=strlen(str);
    for(i=0;i<len;i++)
    {
        if((str[i]>='a' && str[i]<='z') || (str[i]>='A' && str[i]<='Z'))
        {
            if (str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u' || str[i]=='A' || str[i]=='E' || str[i]=='I' ||str[i]=='O' ||str[i]=='U' )
            {
                vowel++;
            }
            else
            {
                consonant++;
            }
        }
    }
    printf("Vowels:%d\n",vowel);
    printf("Consonant:%d",consonant);
    return 0;
}
```
![image](https://github.com/user-attachments/assets/86ac76e2-830a-4243-b2da-2fc90e729e48)
### 10.//C Program to count number of words in string
```C
#include<stdio.h>
#include<string.h>
#define MAX_SIZE 1000
int main()
{
    int i,w=0;
    char str[MAX_SIZE];
    printf("Enter the string:");
    fgets(str,MAX_SIZE,stdin);
    str[strcspn(str,"\n")]='\0';
    for(i=0;str[i]!='\0';i++)
    {
        if((str[i]!=' ' && str[i]!='\n')&&(str[i+1]==' '||str[i+1]=='\n' || str[i+1]=='\0'))
        {
            w++;
        }
    }
    printf("The WordCount is:%d",w);
    return 0;
}
```
![image](https://github.com/user-attachments/assets/cd84be9a-3033-4b4f-894d-836af897ffa5)
### 11.//Program to find reverse of a string
```C
#include<stdio.h>
#include<string.h>
#define MAX_SIZE 1000
int main()
{
    int i,len;
    char temp,str[MAX_SIZE];
    printf("Enter the string:");
    fgets(str,MAX_SIZE,stdin);
    str[strcspn(str,"\n")]='\0';
    len=strlen(str);
    for(i=0;i<len/2;i++)
    {
        temp=str[i];
        str[i]=str[len-i-1];
        str[len-i-1]=temp;
    }
    printf("The reversed string is:%s",str);
    return 0;
}
```
![image](https://github.com/user-attachments/assets/50aeb894-2af1-4624-a74c-985b51fbe99b)
### 12.Program to check palindrome string:
```C
#include<stdio.h>
#include<string.h>
#define MAX_SIZE 1000
int main()
{
    int i,start,end,ispalindrome=1;
    char str[MAX_SIZE];
    printf("Enter the string:");
    fgets(str,MAX_SIZE,stdin);
    str[strcspn(str,"\n")]='\0';
    start=0;
    end=strlen(str)-1;
    while(start<end)
    {
        if(str[start]!=str[end])
        {
            ispalindrome=0;
            break;
        }
        start++;
        end--;
    }
    if(ispalindrome)
    {
        printf("Palindrome");
    }
    else    
    {
        printf("Not palindrome");
    }
    return 0;
}
```
![image](https://github.com/user-attachments/assets/72eb41c4-c4fa-4070-ae65-91891e7012fd)
![image](https://github.com/user-attachments/assets/e0854514-216b-4aee-9256-9ad3d3dc3ede)












