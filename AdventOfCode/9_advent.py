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

# Creating a list of all possible sums of two numbers between list indices 0-24
# Checking if one of the sums equals index 25.
# If it doesn't, the value of index 25 is our answer.
# If it does, clearing the list and doing the same comparison to numbers 1-25 and 26.

for i in range(len(lines)):
    for j in range(x, y):
        for k in range(x+1, y):
            slice.append(lines[j]+lines[k])
    if lines[j+1] not in slice:
        key = lines[j+1]
        print("The answer to task 1 is", key)
        break
    else:
        x += 1
        y += 1
        slice.clear()


# TASK 2

vals = []

for i in range(len(lines)):

    if sum(vals) == key:
        break

    else:
        # Adding each value to a list to compare the sum of the values to key.
        vals.append(lines[i])
        for j in range(i+1, len(lines)):
            vals.append(lines[j])
            s = sum(vals)
            # If sum is larger than key, empty the value list and start again from i+1.
            if s > key:
                vals.clear()
                break
            # If sum is less than key, keep adding.
            elif s < key:
                continue
            # If sum equals key, we have our list of values.
            else:
                break


# The answer is the sum of the largest and the smallest value in the list.

vals.sort()
print("The answer to task 2 is", vals[0]+vals[-1])
