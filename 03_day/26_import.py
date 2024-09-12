# import math

# print(math.pi)
# print(math.cos(90))

from math import pi, cos
from random import randint, shuffle
from datetime import datetime
from os import system, cpu_count

print(pi)
print(cos(90))
print(randint(1, 100))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(numbers)
print(numbers)
date_now = datetime.now()
print(date_now)
print(date_now.year)
print(date_now.month)
print(date_now.day)
print(date_now.hour)
print(date_now.minute)
print(date_now.microsecond)

new_date = datetime(2020, 10, 10)
new_date_2 = datetime(2021, 1, 1)
print(new_date.strftime("%Y. %B %d."))
print((new_date_2 - new_date).days)

print(cpu_count())
system("echo Hello")
system("dir")
