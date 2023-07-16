def heapify(l, n, i):
    parent, left, right = i, 2*i, 2*i+1
    if left <= n and l[parent] < l[left]:
        parent = left
    if right <= n and l[parent] < l[right]:
        parent = right
    if parent != i:
        l[parent], l[i] = l[i], l[parent]
        heapify(l, n, parent)


def heapSort(l,n):
    size=n
    while size>1:
        l[size],l[1]=l[1],l[size]
        size-=1
        heapify(l,size,1)

l = [-1, 54, 53, 55, 52, 50]
n=len(l)-1
heapSort(l,n)

print(l)


