# Advent of Code 2020 day 3
# https://adventofcode.com/

# The idea is to navigate a "map" line by line, going x step down and y steps left.
# At the end of the line the map continues on the next line from the start.
# The task is to count how many "trees" (#) there are in the trail.

from functools import reduce

with open('3_data.txt') as f:
    lines = f.readlines()

lines = [i.strip('\n') for i in lines]

tree = '#'
treeCounts = []


def tree_calculator(x, y):
    position = 0
    length = len(lines[0]) - 1
    a = 0
    for line in lines[::y]:
        if line[position] == tree:
            a += 1
        if position <= (length - x):
            position += x
        else:
            position += x - 1
            position -= length

    treeCounts.append(a)

# TASK 1
# 3 steps left, 1 step down

tree_calculator(3, 1)

print("There are", treeCounts[0], "trees on the 1st trail.")

# TASK 2
# Calculate how many trees there are in the following trails:
# Right 1, down 1.
# Right 3, down 1.(This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# The answer is the tree counts multiplied together.

tree_calculator(1, 1)
tree_calculator(5, 1)
tree_calculator(7, 1)
tree_calculator(1, 2)

answer = reduce(lambda x, y: x*y, treeCounts)

print("The right answer for Task 2 is ", answer, ".", sep='')
