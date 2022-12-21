#include <stdio.h>
#include <string.h>

void printFrom(char *a, int v, int l)
{
    for (int i = v + 1; i <= l - 1; i++)
    {
        printf("%c", a[i]);
    }
    printf(" ");
}

int main()
{
    char a[1000];
    scanf("%[^\n]s", a);
    int l = strlen(a);
    int j = 0, b = l;
    for (int i = l - 1; i >= -1; i--)
    {
        if (a[i] == ' ' || i == -1)
        {
            printFrom(a, i, b);
            b = i;
        }
    }
}