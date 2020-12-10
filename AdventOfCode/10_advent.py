# Advent of Code 2020 day 10
# https://adventofcode.com/

# Task 1 is very simple, count how many steps of 1 or 3 there are in the given list of digits.
# Task 2 is anything but simple, I'll leave that for another time.

with open('10_data.txt') as f:
    lines = f.readlines()
lines = [i.strip('\n') for i in lines]
lines = [int(i) for i in lines]

lines.sort()

lines.insert(0, 0)
lines.append(lines[-1] + 3)

j1 = []
j3 = []

for i in range (0, len(lines) - 1):
    dif = lines[i+1] - lines[i]
    if dif == 1:
        j1.append(lines[i+1])
    elif dif == 3:
        j3.append(lines[i+1])

print("Answer 1 is", len(j1) * len(j3))



