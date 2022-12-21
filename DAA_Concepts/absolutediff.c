#include <stdio.h>
#include <stdlib.h>
int nodigit(int n)
{
    int d = 0;
    while (n != 0)
    {
        n = n / 10;
        d++;
    }
    return d;
}

int main()
{
    int n1, n2;
    scanf("%d %d", &n1, &n2);
    while (n1 <= n2)
    {
        int digit = nodigit(n1), i = 1, e = 0, o = 0, t = n1;
        while (digit)
        {
            if (digit % 2 == 0)
            {
                e += t % 10;
            }
            else
            {
                o += t % 10;
            }
            --digit;
            t = t / 10;
        }
        printf("%d ", abs(e - o));
        ++n1;
    }
}