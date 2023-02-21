"""
Find the sum of the series: 1-2+3-4+5- ... +nth term
"""

n = int(input('Enter the range of the number: '))

sum = 0

for i in range(1, n+1):
    if (i % 2 == 0):
        sum -= i
    else:
        sum += i

print("The sum of the series: ", sum)