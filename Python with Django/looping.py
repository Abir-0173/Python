'''

# looping
# for i in tuple, range, dictionary, list
myTuple = ("a", "b", "c", "d")
myList = [("a", 1, "BDT"), ("b", 2, "USD"), ("c", 3, "CAD")]
myDict = {"name" : "Simanta", "age" : 26, "country" : "Bangladesh"}
myStr = "Bohubrihi"
mySet = {"BDT", "USD", "CAD"}
#for x, y, z in myList:
#    print(f"{x}, {y}, {z}")

#for key, value in myDict.items():
    #print(f"{key} => {value}")

#for ch in myStr:
#    print(ch)

for currency in mySet:
    print(currency)

amarList = list(range(0, 40, 4))
print(amarList)

for i in range(0, 51, 2):
    print(i)

myList = ["spanish", "english", "french", "german", "irish", "chinese"]

for i in range(len(myList)):
    print(f"Language: {myList[i]}")


myList = ["spanish", "english", "french", "german", "irish", "chinese"]

# for fruit in enumerate(myList):
#     print(fruit)
# enumerate function of python
for i, fruit in enumerate(myList):
    print(f"{i} index of {fruit}")
'''
myList1 = ["spanish", "english", "french", "german", "irish", "chinese"]
myList2 = [1, 2, 3, 4, 5, 6, 7]

# zip
# for i, j in zip(myList2, myList1):
#     print(i, j)

# for i in sorted(myList1):
for i in reversed(myList1):
    print(i)


