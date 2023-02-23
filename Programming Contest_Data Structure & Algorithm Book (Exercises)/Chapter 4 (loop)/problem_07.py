"""
Find the sum of the series: 1*n + 2*(n-1) + ... + n*1
"""

n = int(input('Enter the range of the number: '))

sum = 0

for i in range(1, n+1):
    sum += i * (n - i+1)


print("The sum of the series: ", sum)