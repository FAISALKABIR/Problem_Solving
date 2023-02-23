"""
Find the sum of the series: 1 + (2+3) + (4+5+6) + .... + nth term
"""

n = int(input('Enter the range of the number: '))

sum = 0
start = 1
end = 1

for i in range(1, n+1):
    for j in range(start, end+1):
        sum += j

    start = end + 1
    end = start + i

print("The sum of the series: ", sum)