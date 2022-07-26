#result of functions using different args
def f1(a,b):
    print(a,b)

f1(1,2)             #1 2
f1(b = 2, a = 1)    #1 2

def f2(a, *b):
    print(a,b)

f2(1, 2, 3)         #1 (2, 3)

def f3(a, **b):
    print(a,b)

f3(1, x=2, y=3)     #1 {'x': 2, 'y': 3}

def f4(a, *b, **c):
    print(a,b,c)

f4(1, 2, 3, x=2, y=3)   #1 (2, 3) {'x': 2, 'y': 3}

def f5(a, b=2, c=3):
    print(a,b,c)

f5(1)               #1 2 3
f5(1,4)             #1 4 3

def f6(a, b=2, *c):
    print(a,b,c)

f6(1)               #1 2 ()
f6(1, 3, 4)         #1 3 (4,)