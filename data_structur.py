employee = {
    "Name":"Tanimur Rahman",
    "skills": ["python", "Django", "Go"],

    "Yars-of-Experience": 4,
    "address":"Noakhali",
    "type":"parmanent"
}

#keys()
print(employee.keys())

#values
print(employee.values())

# items
print(employee.items())
# dict_items([('name', 'Tanimur Rahman'), ('skills', ['python', 'Django', 'Go']), ('Yars-of-Experience', 4), ('address', 'Noakhali'), ('type', 'parmanent')])

for key, value in employee.items():
    print(key, value)