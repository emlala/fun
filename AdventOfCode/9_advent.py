# Advent of Code 2020 day 9
# https://adventofcode.com/

# Find the first number in the list (after the preamble of 25 numbers)
# which is not the sum of two of the 25 numbers before it.

with open('9_data.txt') as f:
    lines = f.readlines()
lines = [i.strip('\n') for i in lines]
lines = [int(i) for i in lines]

slice = []
y = 25
x = 0

# Creating a list of all possible sums of two numbers in the range 0-24, and checking if 25 is in the list.
# If it is, clearing the list and doing the same to numbers 1-25 and 26.
# Continuing until the program finds a number that is not in the list of sums of the previous 25.

for i in range(len(lines)):
    for j in range(x, y):
        for k in range(x+1, y):
            slice.append(lines[j]+lines[k])
    if lines[j+1] not in slice:
        print("The answer is", lines[j+1])
        break
    else:
        x += 1
        y += 1
        slice.clear()
