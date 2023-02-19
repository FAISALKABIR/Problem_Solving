"""
Three sides are given of a triangle. Find out all the angles of the triangle.
"""

from math import acos, pi

a, b, c = map(int,input("Enter the side values: ").split())

angle_a = round((180/pi) * acos((b**2 + c**2 - a**2) / (2*b*c)))
angle_b = round((180/pi) * acos((a**2 + c**2 - b**2) / (2*a*c)))
angle_c = round((180/pi) * acos((a**2 + b**2 - c**2) / (2*a*b)))

print(angle_a, angle_b, angle_c)