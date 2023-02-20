"""
Find the Quadrant based on the Coordinate (x & y position)
"""

x = int(input("Enter the position of x: "))
y = int(input("Enter the position of y: "))

print("(",x,",",y,")", end="")

if (x < 0 and y > 0):
    print(" belongs to I Quadrant...!")
elif (x > 0 and y > 0):
    print(" belongs to II Quadrant...!")
elif (x < 0 and y < 0):
    print(" belongs to III Quadrant...!")
else:
    print(" belongs to IV Quadrant...!")