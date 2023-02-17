"""
Find the area of a rectangle with given coordinates
"""

def rect_area(x1, y1, x2, y2):
    # calculate the width & height
    width = abs(x1 - x2)
    height = abs(y1 - y2)

    area = height * width 
    return area

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

print("Area of the rectangle is ", rect_area(x1, y1, x2, y2))