# Advent of Code 2020 day 6
# https://adventofcode.com/

import string

with open('6_data.txt') as f:
    d = f.read().split('\n\n')

# TASK 1
# For each group in the data set, count the letters, each letter is counted at most once.
# The answer is the sum of the letter counts for all groups.

d1 = [i.replace('\n', '') for i in d]
lines1 = []

for i in d1:
    lines1.append([char for char in i])

answer1 = 0

for group in range(len(lines1)):
    answer1 += len(set((lines1[group])))

print("The answer for Task 1 is", answer1)

# TASK 2
# For each group in the data set, count only letters that can be found in every line of the group.
# The answer is the sum of these letter counts for all groups.

lines2 = [i.split('\n') for i in d]
answer2 = 0
alphabet = list(string.ascii_lowercase)

for group in range(len(lines2)):
    for a in range(len(alphabet)):
        if lines1[group].count(alphabet[a]) != len(lines2[group]):
            continue
        else:
            answer2 += 1

print("The answer for Task 2 is", answer2)
