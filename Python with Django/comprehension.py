# Comprehension
# iterable -> List, Tuple, Dictionary, Set, Range
# create -> List, Dictionary, Set
myList = [1, 2, 3, 4, 5, 6]

# From List
newList = [i+1 for i in myList] #list create
newDict = {i: i*i for i in myList} # Dictionary create
newSet = {i**3 for i in myList} # create set
newTuple = tuple(i**4 for i in myList) # create Tuple
newTlist = [(i, i**2, i**3) for i in myList]
print(newTlist)

# From Dictionary
myDict = {"name": "Bohubrihi", "address": "Dhaka", "employee": 50}

# remember this .items()
newList = [key for key, value in myDict.items()] # get the keys/values for Dictionary
newTlist = [(key, value) for key, value in myDict.items()]
newDict = {key + " Key": value for key, value in myDict.items()}

print(newDict) 