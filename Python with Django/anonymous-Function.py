"""
# function
def add(x, y):
    return x + y

# lambda function
# Anonymous function
# IIFE
print((lambda x, y: x + y)(20, 15))


# map function
def func(n):
    return n*n*n

l = [3, 4, 1, 0, 6]

newL = list(map(lambda n: n*n*n, l)) # newL = [n*n*n for n in l]

l = ['Simanta', 'Bohubrihi', 'Dhaka']

l2 = list(map(list, l))

print(l2)
# -------------------------
# filter function
l = [1, 3, 4, 6, 88, 4, 2, 9, 5]

def func(n):
    return n%2==1

newList = list(filter(lambda n: n%2==1, l))
print(newList)
# -------------------------
# reduce
from functools import reduce
li = [1, 2, 3, 4,2 ,3 ,4]
def func(x, y):
    return x + y

sum = reduce(lambda x, y: x+y, li)
print(sum)

# ------------------------------------->>><<<<<<<<<<<<<<<<<<<<<<<<<-------------------


# Higher Order Function
def hof(fn):
    print(fn.__name__)
    fn()

def greet():
    print("hello world")

def hello():
    print("hello abir")

# hof(hello)
# hof(greet)

li = [1, 2, 3, 4, 5, 6]
# Heirorder ============createing filter=============>>>>>>>>>>>>
def myFilter(fn, l):
    newL = []
    for i in l:
        if fn(i):
            newL.append(i)
    return newL

# Heirorder =========================>>>>>>>>>>>>

newList = myFilter(lambda x: x%2 == 1, li)
# newList = list(filter(lambda x: x%2 == 1, li))
print(newList)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Higher Order Function <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
"""
# Higher Order Function -> Accepts function as argument or returns function

# Wrapper
def myWrapper(fn):
    def test():
        print("I am from test! Before")
        fn()
        print("I am from test! After")

    return test

# Decorators
@myWrapper
def greet():
    print("Hello world!")

@myWrapper
def hello():
    print("Hello Hello")

# hello = myWrapper(hello)
#greet()
hello()





