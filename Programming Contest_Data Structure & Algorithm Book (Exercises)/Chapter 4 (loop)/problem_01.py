"""
Find the sum of the series: "1+2+3+4+......+n"
"""

n = int(input("Enter the range of number: "))

sum = 0
for i in range(1, n+1):
    sum += i

print("The sum of the series: ", sum)