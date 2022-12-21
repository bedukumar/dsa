#include <stdio.h>

// datatype naam()

void SumArray(int a[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum = 0;
        for (int j = 0; j < n; j++)
        {
            if (i == j)
            {
                continue;
            }
            else
            {
                sum = sum + a[j];
            }
        }
        printf("%d ", sum);
    }
}

int main()
{
    int a[5], n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    SumArray(a, n);
}