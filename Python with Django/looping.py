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


for i in range(2, 50, 2):
    print(i)