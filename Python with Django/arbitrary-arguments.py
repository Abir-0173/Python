# Function
# def hello (fname, lname):
#     print(f"Full Name: {fname} {lname}")

# fname, lname -> parameter
# arguments --> tanimur, rahman ( Passed Value)
# hello("tanimur", "rahman")

# Arbitrary Arguments
def fun1(*argu):
    print(argu)

fun1("tanimur", "rahman", True, 26, False)

# Arbitrary Keyword Arguments
def fun2(**kwargs):
    print(kwargs['fname'])

# fun2(fname="Simanta", lname="Paul", age=25)

def hello3(*args, **kwargs):
    print(args, kwargs)

hello3()