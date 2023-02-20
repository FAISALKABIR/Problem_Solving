"""
Find the sum of all integer numbers lying between 1 and N inclusive (use if_else)
"""

n = int(input("Enter an integer number: "))

if (n > 0):
    print(int(n*(n+1) / 2))
elif (n == 0):
    print('1')
else:
    print(int(n*(n-1) / -2 + 1))