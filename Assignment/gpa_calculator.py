'''
Bangla english math science
1-100
average of all subject from user

0-40 = F
41-60 = D
61-70 = C
71-80 = B
81-90 = A
91-100 = A+


'''
Bangla  =int( input("Enter Your Number: "))
english =int( input("Enter Your Number: "))
math =int( input("Enter Your Number: "))
science =int( input("Enter Your Number: "))
print(Bangla,english, math, science)

average_of_all_Subject = (Bangla + english + math + science)/4
print(average_of_all_Subject)
# def F():
#     print("Your Grade is F")

def Calculation(b):
    if b <= 40:
        print("Your grade is F")
    elif b >= 41 and b <= 60:
        print("Your Grade is D")
    elif b >= 61 and b <= 70:
        print("Your Grade is C")
    elif b >= 71 and b <= 80:
        print("Your Grade is B")
    elif b >= 81 and b <= 90:
        print("Your Grade is A")
    elif b >= 91 and b <= 100:
        print("Your Grade is A+")
    else:
        print("Invalid number given By user")

    # return inner(average_of_all_Subject)

Calculation(average_of_all_Subject)

