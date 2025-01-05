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



