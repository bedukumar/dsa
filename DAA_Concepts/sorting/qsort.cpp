#include <iostream>

using namespace std;

void swap(int *p1, int *p2)
{
    int t = *p1;
    *p1 = *p2;
    *p2 = t;
}

int partition(int arr[], int l, int r)
{
    int pivot = arr[r];
    int i = l - 1;
    for (int j = l; j < r; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[r]);
    return i + 1;
}

void q(int a[], int l, int r)
{
    if (l < r)
    {
        int pi = partition(a, l, r);
        q(a, l, pi - 1);
        q(a, pi + 1, r);
    }
}

int main()
{
    int a[5] = {5, 4, 3, 2, 1};
    q(a, 0, 4);
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}
