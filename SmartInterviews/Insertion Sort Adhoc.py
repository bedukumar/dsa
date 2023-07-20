def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        print(j+1,end=" ")
        arr[j+1] = key
    
for _ in range(int(input())):
    input()
    insertionSort(list(map(int,input().split())))
    print()
    
