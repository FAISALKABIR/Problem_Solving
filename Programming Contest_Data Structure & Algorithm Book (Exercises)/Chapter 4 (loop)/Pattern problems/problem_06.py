"""
Program to print a solid Pyramid Number Pattern:
        1
      1 2 1
    1 2 3 2 1
      1 2 1 
        1
"""

row_size = int(input("Enter the diamond's height: "))

for i in range(1, row_size * 2 + 1):
    print(end = " ")
print("0")

# generating the middle pattern.
for i in range(1, row_size * 2):
    # printing the increasing pattern
    if (i < row_size):
        for j in range(1, (row_size - i) * 2 + 1):
            print(end = " ")
    else:
        for j in range(1, (i % row_size) * 2 + 1):
            print(end = " ")
    
    if (i < row_size):
        for j in range(i % row_size + 1):
            print(j, end = " ")
        for j in range(i % row_size - 1, -1, -1):
            print(j, end = " ")

    # printing the decreasing pattern
    elif (i > row_size):
        for j in range(row_size - (i - row_size) + 1):
            print(j, end = " ")
        for j in range((row_size - (i - row_size)) - 1, -1, -1):
            print(j, end = " ")

    else:
        for j in range(row_size + 1):
            print(j, end = " ")
        for j in range(row_size - 1, -1, -1):
            print(j, end = " ")
            
    print()

# putting the space in last line
for i in range(1, row_size * 2 + 1):
    print(end = " ")
print("0", end = "")

