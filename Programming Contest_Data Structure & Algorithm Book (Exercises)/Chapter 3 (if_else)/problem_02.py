"""
Find  i*(n-i+1) = 1*n + 2*(n-1) + ... n*1 where i=1 and n is given by the user (use if_else)
"""

n = int(input("Enter an integer number = "))
i = 1

if (n == 1):
    print("i*(n-i+1) =", i * (n - i + 1))
elif (n == 2):
    print("i*(n-i+1) =", i * (n - i + 1))
elif (n == 3):
    print("i*(n-i+1) =", i * (n - i + 1))
else:
    print("Please enter a number above 0 or less than 4")