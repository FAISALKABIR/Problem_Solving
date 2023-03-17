"""
Check whether a given number is prime or not
"""

import math

num = int(input("Enter an integer number: "))

count = 0

for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        count += 1

if (count == 0):
    print("This is a prime number...!")
else:
    print("This is not a prime number...!")
