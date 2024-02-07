def FunctionSolver(f, n, E):
    low = 0
    high = n
    val = (high + low)/2
    print("Val is now " + str(val))
    while high - low > 2*E:
        if f(val) == 0:
            return val
        if f(val) < 0:
            low = val
        if f(val) > 0:
            high = val
        val = (high + low)/ 2
    return val

def f(val):
    return pow(2, val) - 2*val

def f1(val):
    return pow()

print(FunctionSolver(f, 2, 0.03125))
