'''
5! = 5 * 4 * 3 * 2 * 1 =120
4! = 4 * 3 * 2 * 1 = 24


def factorial(n):
    if n == 1:
        return 1
    m = factorial(n - 1)
    return n * m
print(factorial(4))

# ------------concept of decorator -----------------

def my_func():
    print('hello world')
    print("this is a function")

def print_function(func):
    func()
    print("this is from print function")
# my_func()
print_function(my_func)

# -----Nested function ---------

def greet (name):
    def hello():
        return "hello my name is " + name
    return hello()
my_variable = greet("abir")
print(greet("tanim"))
print(my_variable)

# --------

def greet(func):
    def inner():
        func()
        print("This is from inner function")

    return inner

# decoretor symbol '@" ------- ============
@greet
def hello():
    print("this is from hello func")

print(hello())

'''
def zero_division_error(func):
    def inner(a, b):
        if b == 0:
            return "zero Division Error"

        return func(a, b)
    return inner

@zero_division_error
def divide(a, b):
    return a/b

print(divide(10, 2))
print(divide(10, 3))
print(divide(10, 0))





