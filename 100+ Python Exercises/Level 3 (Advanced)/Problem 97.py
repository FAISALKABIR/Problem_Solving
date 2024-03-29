"""
Question 97:

Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

Hints:
Use list[::-1] to iterate a list in a reverse order.
"""

# Solution_1
s = input()

s = s[::-1]

print(s)

# Solution_2
s = input()

s = ''.join(reversed(s))

print(s)