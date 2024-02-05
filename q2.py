import random


def MinMax(arr):

    i = 1
    m = 0
    M = 0
    n = len(arr) - 1
    count = 0
    while i <= n:
        count +=1
        if arr[i] < arr[m]:
            m = i
        count += 1
        if arr[i] > arr[M]:
            M = i
            
        i = i + 1
    return (m+1, M+1, count)   #indexed at 1 for some reason




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


def ListCheck():
    for list in lists:
        arr = lists[list]
        print("Min, Max, Count for length " + str(len(arr)) + " " + str(MinMax(arr)))

arr = [56, 66, 18, 5, 28, 65, 11, 14 ,60, 51, 40, 55, 27, 46, 57, 31]
print("length: " + str(len(arr)) + " min, max, count " + str(MinMax(arr)))