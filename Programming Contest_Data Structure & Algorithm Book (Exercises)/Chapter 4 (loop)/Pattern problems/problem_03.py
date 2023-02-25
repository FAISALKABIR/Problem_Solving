"""
Program to print the Full Pyramid Star pattern:
     * 
   * * *
 * * * * *
"""

row_size = int(input("Enter the row size: "))

for i in range(row_size+1):
    for j in range((row_size-i)+1):
        print(" ", end="")

    for k in range(2*i-1):
        print("*", end="")

    print("\r")