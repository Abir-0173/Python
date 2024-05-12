class A:
    def __init__(self):
        print("From class A")
class B(A):
    def __init__(self):
        print("From Class B")
        # A.__int__(self)
        super().__init__()

    def my_method(self):
        print("This is from Class B")
class C(B):
    def __init__(self):
        print("From class c")
        # B.__int__(self)
        super().__init__()

    def my_method(self):
        print("This is from Class B")

class D(C, B):
    def __init__(self):
        print("from class D")
        # C.__init__(self)
        super().__init__()


object_D = D()