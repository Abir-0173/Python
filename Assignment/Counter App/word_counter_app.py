search_words = ["Python", "C", "OOP", "Hello", "Java"]
with open('input.txt', 'r') as file:
     # print(file.read())
     words_from_text_file = file.read()

def Convert(string):
    li = list(string.split("\n"))
    return li
print("text from input.txt File ==>" , Convert(words_from_text_file))

def countX(lst, x):
    counts = {}  # Dictionary to store counts of elements from list x
    for ele in x:  # Loop through each element in x
        counts[ele] = lst.count(ele)  # Count occurrences of ele in lst and store in dictionary
    return counts

# Driver Code
lst = words_from_text_file
x = ["Python", "C", "OOP", "Hello", "Java"]

# Count occurrences of elements in x in lst
counts = countX(lst, x)

# Print counts in desired format
for element, count in counts.items():
    print('{} {} times'.format(element, count))


'''

# def count_words(p, q):
# for x  in search_words:
#     print(x)

# count_words(p, q)
# for x in search_words:
#     print(x)

# file = open("input.txt", "r")
# print(file.read())


# search_words = ["Python", "C", "OOP", "Hello", "Java"]
# with open('input.txt', 'r') as file:
#      # print(file.read())
#      words_from_text_file = file.read()


     # print(words_from_text_file)


# count_words(words_from_text_file, search_words)
# -----------------
# def Convert(string):
#     li = list(string.split("\n"))
#     return li
# print(Convert(words_from_text_file))
# text_word = Convert(words_from_text_file)
# print(text_word)
# count = 0;
# ----------------
 for element in enumerate(text_word):
    # print(element)
    if element == "python":
        count += 1
    print(element)
    print(count)      


def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


# Driver Code
lst = ["Python", "C", "OOP", "Hello", "Java", "Python", "C", "OOP", "Hello", "Java"]
x = ["Python", "C", "OOP", "Hello", "Java"]
newlo = countX(lst, x)
print(newlo)

print('{} has occurred {} times'.format(x, countX(lst, x))) '''

