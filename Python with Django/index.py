# Sequence Unpacking
myTuple = ("Bangladesh", "India", "Pakistan")

myList = ["Bangladesh", "India", "Pakistan", "USA", "Canada"]
c1, *c2, c3, c4 = myList

print(c1)
print(c2)
print(c3)
print(c4)
