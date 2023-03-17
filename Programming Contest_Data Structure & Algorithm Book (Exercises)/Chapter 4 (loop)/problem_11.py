"""
Find nPr (Permutation)
Formula: nPr = n!/(n-r)!
"""

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

fact = 1
i = 1
while (i <= n):
    fact = i * fact
    i = i + 1

numerator = fact        # n!
sub = n - r             # (n - r)
fact = 1
i = 1
while (i <= sub):
    fact = i * fact
    i = i + 1

denominator = fact      # (n - r)!
perm = numerator / denominator

print("\nPermutation (nPr) =", perm)




# Using library function
"""
import math

print("Enter the Value of n: ", end="")
try:
  n = int(input())
  print("Enter the Value of r: ", end="")
  try:
    r = int(input())

    numerator = math.factorial(n)
    denominator = math.factorial(n-r)
    perm = numerator/denominator

    print("\nPermutation =", perm)
  except ValueError:
    print("\nInvalid Input!")
except ValueError:
  print("\nInvalid Input!")
"""