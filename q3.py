def stackSort(numba):
    stack = []
    leftSide = []
    rightSide = []
    
    numba = str(numba)[::-1]
    for l in str(numba):
        rightSide.append(int(l)) 

    #algo begins
    count = 0

    while rightSide:
        if len(stack) == 0 or rightSide[-1] < stack[-1]:
            count += 1
            stack.append(rightSide.pop())
        else:
            if rightSide[-1] > stack[-1]:
                count += 1
                leftSide.append(stack.pop())
    
    while stack:
        count += 1
        leftSide.append(stack.pop())

    
    return stack, leftSide, rightSide, count

stack, left, right, count = stackSort(231)

print(len(left))
print(left)
print(count)


