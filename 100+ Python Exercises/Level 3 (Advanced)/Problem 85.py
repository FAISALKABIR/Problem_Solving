"""
Question 85:

Please write a program to shuffle and print the list [3,6,7,8].

Hints:
Use shuffle() function to shuffle a list.
"""

# Solution
import random

# shuffle with a chosen seed
lst = [3,6,7,8]
seed = 7

random.Random(seed).shuffle(lst)

print(lst)