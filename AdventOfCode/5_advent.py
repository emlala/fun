# Advent of Code 2020 day 5
# https://adventofcode.com/

# Binary space partitioning
# The first 7 characters will either be F or B.
# These specify exactly one of the 128 rows on an airplane (numbered 0 through 127).
# Each letter tells you which half of a region your seat is in.
# Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63)
# or the back (64 through 127).
# The next letter indicates which half of that region the seat is in, and so on, until you're left with exactly one row.

# The last three characters will be either L or R.
# These specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The process is as above.

# Every seat also has a unique seat ID: multiply the row by 8, then add the column number.

# TASK 1: What is the highest seat ID in the data set?

with open('5_data.txt') as f:
    lines = f.readlines()
lines = [i.strip('\n') for i in lines]


def seat_id(position):
    upper = 127
    lower = 0
    middle = 63.5
    u_col = 7
    l_col = 0
    m_col = 3.5

    for i in range(0, len(position)):
        if i <= 6:
            if position[i] == 'F':
                lower = lower
                upper = middle
                middle = (upper + lower) / 2
            elif position[i] == 'B':
                upper = upper
                lower = middle
                middle = (upper + lower) / 2

        if i > 6:
            if position[i] == 'L':
                l_col = l_col
                u_col = m_col
                m_col = (u_col + l_col) / 2
            elif position[i] == 'R':
                u_col = u_col
                l_col = m_col
                m_col = (u_col + l_col) / 2

    id = round(middle) * 8 + round(m_col)
    return id

highest = 0
idList = []

for i in range(len(lines)):
    seatID = seat_id(lines[i])
    idList.append(seatID)
    if seatID > highest:
        highest = seatID
    else:
        continue

print("Highest seat ID:", highest)

# TASK 2
# Your seat ID is missing from the list.
# The seats with IDs +1 and -1 from yours will be in your list.
# What is the ID of your seat?

idList = sorted(idList)
mySeat = 0

for i in range(idList[0], idList[-1]):
    if i in idList:
        continue
    else:
        mySeat = i

print("My seat ID:", mySeat)
