"""
Find nCr (Combination)
Formula: nCr = n!/r!(n-r)!
"""

n = int(input("Enter the Value of n: "))
r = int(input("Enter the Value of r: "))

fact = i = 1
while (i <= n):
    fact = i * fact
    i += 1

numerator = fact
sub = (n - r)
fact = i = 1

while (i <= sub):
  fact = i * fact
  i += 1

denominator = fact
fact = i = 1
while (i <= r):
  fact = i * fact
  i += 1

denominator = fact * denominator
comb = numerator / denominator

print("\nCombination (nCr) =", comb)