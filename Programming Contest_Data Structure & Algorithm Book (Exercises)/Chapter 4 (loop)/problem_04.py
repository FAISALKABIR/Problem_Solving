"""
Find the sum of the series: 1 + (2+3) + (4+5+6) + .... + nth term
"""

n = int(input('Enter the range of the number: '))

sum = 0

for i in range(1, n+1):
    for j in range(i+1, i):
        sum += j

print("The sum of the series: ", sum)