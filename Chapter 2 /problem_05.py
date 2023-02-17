"""
Find the nearest integer number of a square root of the number
"""

# Method 1: Without using any library function
def sqrt(x):
    # base case
    if (x == 0 or x == 1):
        return x

    # Starting from 1, try all numbers until
    # i*i is greater than or equal to x.
    i = 1
    result = 1
    while (result <= x):
        i += 1
        result = i * i

    return i - 1

x = int(input("Enter a number: "))
print(sqrt(x))


# Method 2: Using library function
import math

# Print the square root of different numbers
print(math.sqrt(10))
print(math.sqrt (12))
print(math.sqrt (68))
print(math.sqrt (100))

# Round square root downward to the nearest integer
print(math.isqrt(10))
print(math.isqrt (12))
print(math.isqrt (68))
print(math.isqrt (100)) 