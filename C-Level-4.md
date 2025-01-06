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





