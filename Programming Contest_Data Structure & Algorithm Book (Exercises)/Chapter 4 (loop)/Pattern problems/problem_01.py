"""  
Program to print the right triangle star pattern:
  *       
  **     
  *** 
"""

row_size = int(input("Enter the row size: "))

for i in range(row_size+1):
    for j in range(i):
        print("*", end="")

    print("\r")