import math

def a(n):
    count = 0
    for i in range(0, n):   #i: 0 to n-1
        j = i
        while j > 0:
            count += 1 #count how many times print(i, j) runs
            j = j - 2
    return count

def formulaA(n):
    if n % 2 == 0:
        return (n/2) * (n/2)
    else:
        return math.floor((n/2)) * (n+1)/2

def b(n):
    count = 0
    for i in range(0, n):   # i: 0 to n-1
        for j in range(0, 2*i+1):
            count += 1
    return count

def formulaB(n):
    return n*n


def c(n):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if i != j and i != k and k != j:
                    count += 1
    return count

def formulaC(n):
    return n*(n-1)*(n-2)

testCases = set()

for i in range(1,100):
    testCases.add(i)



def checkA(n):
    if a(n) == formulaA(n):
        return True

def checkB(n):
    if b(n) == formulaB(n):
        return True

def checkC(n):
    if c(n) == formulaC(n):
        return True

def conclusiveCheck():
    check = True
    for i in testCases:
        if not (checkA(i) and checkB(i) and checkC(i)):
           check = False
    if check == True:
        print("Passed testcases")
    else:
        print("failed")

conclusiveCheck()
