"""
Find nPr and nCr using Function
"""

def fact(k):
    f = i = 1
    while (i <=k ):
        f = i * f
        i += 1

    return f

def findperm(x, y):
    num = fact(x)
    den = fact(x - y)
    perm = num / den

    return perm

def findcomb(x, y):
    num = fact(x)
    den = fact(x - y)
    den = fact(y) * den
    comb = num / den
    
    return comb

n = int(input("Enter the Value of n: "))
r = int(input("Enter the Value of r: "))

print("\nPermutation (nPr) =", findperm(n, r))
print("Combination (nCr) =", findcomb(n, r))