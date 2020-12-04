# Advent of Code 2020 day 1
# https://adventofcode.com/

# TASK 1
# From 1_data.txt find the two entries that sum to 2020.
# Answer 1 is the two digits multiplied together.

with open('1_data.txt') as f:
    lines = f.readlines()

lines = [i.strip('\n') for i in lines]

for i in range(0, len(lines)):
    lines[i] = int(lines[i])

key = 2020

for i in range(0, len(lines)):
    n = key - lines[i]
    for j in range(i+1, len(lines)):
        if lines[j] == n:
            a1 = lines[i]
            a2 = lines[j]
        else:
            continue

answer1 = a1*a2
print("Answer 1 is", answer1)


# TASK 2
# Next find three entries that sum to 2020.
# Answer 2 is the three digits multiplied together.

for i in range(0, len(lines)):
    n = key - lines[i]
    for j in range(i+1, len(lines)):
        m = n - lines[j]
        for k in range(j+1, len(lines)):
            if lines[k] == m:
                b1 = lines[i]
                b2 = lines[j]
                b3 = lines[k]
            else:
                continue

answer2 = b1*b2*b3
print("Answer 2 is", answer2)
