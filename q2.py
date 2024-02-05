import random


def MinMax(arr):

    i = 1
    m = 0
    M = 0
    n = len(arr) - 1
    count = 0
    while i <= n:
        if arr[i] < arr[m]:
            m = i
            count += 1
        if arr[i] > arr[M]:
            M = i
            count +=1
        i = i + 1
    return (m+1, M+1, count)   #indexed at 1 for some reason

arr = [3, 5, 7 ,3 ,41, 33]



lists = {}

for i in range(1,51):
    list_name = "list" + str(i)
    lists[list_name] = []


i = 2
for list in lists:
    for j in range(i):                      #list1 has 2 random, list2 has 4, ...
        numba = random.randint(1,100)
        lists[list].append(numba)
    i += 2

print(MinMax(arr))

for list in lists:
    arr = lists[list]
    print("Min, Max, Count for length " + str(len(arr)) + " " + str(MinMax(arr)))
