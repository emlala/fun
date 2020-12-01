# Advent of Code 2020 day 1
# https://adventofcode.com/

# From 1_data.txt find the two entries that sum to 2020; the answer 1 is the two digits multiplied together.
# Next find three entries that sum to 2020; the answer 2 is the three digits multiplied together.

with open('1_data.txt') as f:
    lines = f.readlines()

lines = [i.strip('\n') for i in lines]

for i in range(0, len(lines)):
    lines[i] = int(lines[i])

key = 2020

for i in range(0, len(lines)):
    n = key - int(lines[i])
    for j in range(i+1, len(lines)):
        m = n - int(lines[j])
        for k in range(j+1, len(lines)):
            if lines[k] == m:
                a1 = lines[i]
                a2 = lines[j]
                a3 = lines[k]
            else:
                continue

answer1 = a1*a2
answer2 = a1*a2*a3

print("Answer 1 is ", answer1)
print("Answer 2 is ", answer2)