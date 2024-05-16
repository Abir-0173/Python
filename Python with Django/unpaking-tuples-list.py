# sequence unpacking
"""
myTuple = ('sifat', "badhon", "saber")

c1, c2, c3 = myTuple
print(c1)
print(c2)
print(c3)
# print(c4)
"""
myTuple = ["sifat", "badhon", "saber", "abir", "isat"]

c1, *c2, c3, c4 = myTuple
print(c1)
print(c2)
print(c3)
print(c4)


