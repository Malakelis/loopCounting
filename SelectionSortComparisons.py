def SelectionSort(arr):
    count = 0
    n = len(arr) - 1
    for i in range(0,n):
        m = i
        for j in range(i+1, n+1):
            count += 1
            if arr[j] < arr[m]:
                m = j
            if i != m:
                arr[i], arr[m] = arr[m], arr[i]
    return count

array = [12,3,1,24,6,8,5]

print("length: " + str(len(array)) + " count of comparisons " +  str(SelectionSort(array)))