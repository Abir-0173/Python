# key ==> value

mydict = {'key1': "tanimur", "key2": 1280}

print(mydict)
# add
mydict['key3'] = "Abir"

print(mydict)
# delete
del mydict['key2']
print(mydict)

# some process of creating dictionary

a = dict(key1 = "abir", key2 = "home", key3 = 15) # use dict and () Brackets
b = {'key1': 'abir', 'key2': 14}       # use {} bracket
c = dict(zip(['key1', 'key2', 'key3'], ['abir', 'rakib', 20])) # use zip inside dict
d = dict([('key1', 'abir'),('key2', 'vai'),('key3', 'bro'),])
e = dict({'key1': 'abir', 'key2': 14} )
f = dict({'key1': 'abir', 'key2': 14}, key2 = "Home")

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print(e.pop("key1"))
print(a.pop("key3"))