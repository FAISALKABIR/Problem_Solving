"""  
Program to print the Inverted Half Pyramid Star Pattern:
    ***
     **
      *
"""

row_size = int(input("Enter the row size: "))

for i in range(row_size+1):
    for j in range(i):
        print(" ", end="")
    
    for k in range(row_size+1, i+1, -1):
        print("*", end="")
    
    print("\r")