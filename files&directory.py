'''


import os

path = '../Python-code-Bohubrihi'

all_files = os.listdir(path)

for files in all_files:
    if os.path.isfile(os.path.join(path, files)):
        print("{} is a file".format(files))


# os.scandir() method

all_files = os.scandir(path)
for file in all_files:
    if file.is_file():
        print("{} is new file".format(file.name))


#   Using pathlib module
import pathlib

# path object construct

path_object = pathlib.Path(path)

for file in path_object.iterdir():
    if file.is_file():
        print(file.name)
# -----------------------------------------

file = open('myfile.txt', 'r')

# print(file.read())
# print(file.readline())
# print(file.readline())
# --------
# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line)
# ---

# file.readlines()  here "s" look
all_lines = file.readlines()
print(all_lines)
# --------------------------


# file = open('myfile.txt', 'r')
# print(file.read())
#
# file.close()

# alwase use this -----------------------------------------------
# with open('myfile.txt', 'r') as file:
#      print(file.read())
#------------------------------------

# with open("myfile.txt", "a") as file:
#     my_list = ["\nhay this x\n", "hay this y\n", "hay this z\n"]
#     file.writelines(my_list)
#     -------------------------------------
# multiple file creating

user_data = [
    {
        'file_name': 'user_1.txt',
        'context': "hellow this is from User 1 "
    },
    {
        'file_name': 'user_2.txt',
        'context': "hellow this is from User 1 "
    },
    {
        'file_name': 'user_3.txt',
        'context': "hellow this is from User 1 "
    }
]
for user in user_data:
    file_name = user['file_name']
    context = user['context']

    with open(file_name, 'w') as file:
        file.write(context)
# ------------------------------
# user_names = [user['file_name'] for user in user_data]
# print(user_names)
# with open(user_names, 'w') as file:
#     file.write(user_names)

#------- file checking ------------------
# path = 'myfile.txt'
# # os.path
#
# import os
# print(os.path.isfile(path))

# pathlib

# import pathlib
#
# file = pathlib.Path(path)
#
# print(file.is_file())

# ------ REMOVE FILE ------------------------------
import os

path = 'user_1.txt'

if os.path.isfile(path):
    os.remove(path)

# -----------------  DELETING A FOLDER  os.removedirs(file-path)---------------------------------
# import os
#
# path = '1234'
#
# if os.path.exists(path):
#     # os.remove(path)
#     os.removedirs(path)

import shutil

path = '1234'

try:
    shutil.rmtree(path)
    print(f"Directory '{path}' successfully removed.")
except OSError as e:
    print(f"Error: {e}")
'''


class A:
    def __int__(self):
        print("From class A")


class B(A):
    def __int__(self):
        print("From Class B")
        # A.__int__(self)
        A.__init__(self)

    def my_method(self):
        print("This is from Class B")


class C(B):
    def __int__(self):
        print("From class c")
        # B.__int__(self)
        B.__init__(self)

    def my_method(self):
        print("This is from Class B")


class D(C, B):
    def __int__(self):
        print("from class D")
        C.__init__(self)
        B.__init__(self)


object_D = D()