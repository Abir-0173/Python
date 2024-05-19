'''
# Object Oriented Programming
# Inheritance
class A:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello from class A")

class B:
    def __init__(self, job):
        self.job = job

    def hello(self):
        print("Hello from class B")


class C(A, B):
    def __init__(self, name, job):
        A.__init__(self, name)
        B.__init__(self, job)

    def hello(self):
        A.hello(self)
        B.hello(self)
        print(f"{self.name} is {self.job}")

obj = C("Simanta", "Mentor")
obj.hello()

# >>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
'''
# Object Oriented Programming
# Inheritance
class A:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello from class A")

class B(A):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job

    def hello(self):
        print(f"{self.name} is a {self.job}")

obj = B("Simanta", "Mentor")
obj.hello()
print(dir(obj))
