"""
Program to print the Full Inverted Pyramid Number Pattern:
    1 2 3 2 1
      1 2 1 
        1
"""

# row_size = int(input("Enter the diamond's height: "))

# for i in range(row_size, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end =" ")
#     for k in range(j-1, 0, -1):
#         print(k, end =" ")

#     print("\r")

def palindrome(rows):

    for i in range(0,rows+1):
        for j in range(i,rows+1):
                print(" ",end=" ")

        for j in range(1,i+1):
            print(j,end=" ")

        for j in range(i-1,0,-1):
            print(j,end=" ")

        print()

rows=int(input("Enter the number of rows :"))

palindrome(rows)