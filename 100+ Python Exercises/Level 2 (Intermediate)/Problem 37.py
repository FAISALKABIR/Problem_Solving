"""
Question 37:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
"""

# Solution
def printList():
	li = list()
	
	for i in range(1,21):
		li.append(i**2)
		
	print(li)	

printList()