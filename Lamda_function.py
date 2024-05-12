'''
# def cube(a):
#     return a ** 3


# def average(a, b):
#     return (a+b)/2

square = lambda a : a ** 2
average = lambda a, b : (a + b) / 2


print(square(4))
print(average(4, 6))


# Time tutorial .py
import time
print(time.time())

second = 1714934769.696374

print(time.ctime(second))

print("I am new Line")

time.sleep(2)
print("I am new  anotherLine")
'''

# Date time-------------------

import datetime
print(datetime.datetime.now())

#current_utc Time

# print(datetime.datetime.utcnow())
print(datetime.date.today())

# timestamp

random_date = datetime.date.fromtimestamp(1234567)
print(random_date)
print(type(random_date))
