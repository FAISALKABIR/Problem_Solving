"""
Question 46:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
"""

# Solution
li = [1,2,3,4,5,6,7,8,9,10]

squaredNumbers = map(lambda x: x**2, li)

print(squaredNumbers)