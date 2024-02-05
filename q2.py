def MinMax(arr):
    i = 1
    m = 0
    M = 0
    n = len(arr) - 1
    while i <= n:
        if arr[i] < arr[m]:
            m = i
        if arr[i] > arr[m]:
            M = i
        i = i + 1
    return (m+1, M+1)   #indexed at 1 for some reason

arr = [3, 5, 7 ,3 ,41]


print(MinMax(arr))