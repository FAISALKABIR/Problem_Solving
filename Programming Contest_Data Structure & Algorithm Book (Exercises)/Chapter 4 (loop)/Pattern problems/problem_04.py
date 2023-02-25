"""
Program to Print a solid Diamond Star Pattern:
     *         
   * * *     
 * * * * *    
   * * *        
     * 
"""

row_size = int(input("Enter the diamond's height: "))

for i in range(row_size):
    print(" " * (row_size-i), "*" * ((2*i)+1))

for i in range(row_size-2, -1, -1):
    print(" " * (row_size-i), "*" * ((2*i)+1))