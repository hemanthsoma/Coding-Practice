#include <stdio.h>
#include <stdlib.h>
int main() {
    char s[100];
    scanf("%s",s);
    printf("%s",s);
    printf("\n");
    int c=1,l=(strlen(s)/2)-1,d=0,g=(strlen(s)/2)+1;
    for(int i=0;i<strlen(s)/2-1;i++)
    {
        for(int i=0;i<c;i++)
        {
            printf("%c",'*');
        }
        for(int j=d;j<l;j++)
        {
            printf("%c",s[j]);
        }
        for(int k=g;k<strlen(s);k++)
        {
            printf("%c",s[k]);
        }
        for(int i=0;i<c;i++)
        {
            printf("%c",'*');
        }
        printf("\n");
        l--;
        c++;
        g++;
    }
    for(int i=0;i<strlen(s);i++)
    {
        printf("%c",'*');
    }
    return 0;
}
/*
Input:
barber

Output:
barber
*baer*
**br**
******
*/
