"""
Question 100:

Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
"""

# Solution_1
def solve(numheads,numlegs):
    ns = 'No solutions!'

    for i in range(numheads+1):
        j = numheads-i

        if 2*i+4*j == numlegs:
            return i,j
        
    return ns,ns

numheads = 35
numlegs = 94
solutions = solve(numheads,numlegs)

print(solutions)

# Solution_2
import itertools

def animal_counter(lst):
    chickens = 0	
    rabbits = 0
    for i in lst:
        if i == 2:
            chickens += 1
        elif i == 4:
            rabbits += 1
    print(f"Number of chickens is {chickens}\nNumber of rabbits is {rabbits}")


def animal_calculator(total_legs, total_heads, legs_of_each_species):
    combinations = itertools.combinations_with_replacement(legs_of_each_species, total_heads)
    correct_combos = []
    for i in list(combinations):
        if sum(i) == total_legs:
            correct_combos.append(i)
    print(correct_combos)
    for i in correct_combos:
        animal_counter(i)

animal_calculator(94, 35, legs_of_each_species=[2,4])