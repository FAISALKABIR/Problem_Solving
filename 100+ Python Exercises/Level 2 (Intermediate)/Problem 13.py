"""
Question 13:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

# Solution:
s = input()
d = {"DIGITS":0, "LETTERS":0}

for c in s:
    if c.isdigit():
        d["DIGITS"] += 1

    elif c.isalpha():
        d["LETTERS"] += 1

    else:
        pass

print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])