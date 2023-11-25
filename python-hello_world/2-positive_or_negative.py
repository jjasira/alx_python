# !/usr/bin/python3
import random
number = random.randint(-10, 10)
if number >= 0:
    print(str(number) + " is a positive number")
else:
    print(str(number) + " is a negative number")
