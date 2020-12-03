# Advent of Code 2020 day 2
# https://adventofcode.com/

# The task is to check whether "passwords" in the data set are valid or not, and count the number of valid passwords.
# Each line of the data set contains two digits, a key letter, and the password.
# In task 1 the digits indicate the minimum and maximum occurrences of the key letter in the password.
# In task 2 the digits indicate exact positions in the password, exactly one of them must contain the key letter.

import re

with open('2_data.txt') as f:
	lines = f.readlines()

lines = [i.strip('\n') for i in lines]

validLines1 = []
validLines2 = []

for i in range(0, len(lines)):
	s = lines[i]

	ints = re.findall('[0-9]+', s)
	min = int(ints[0])
	max = int(ints[1])


	key = re.search('(?<=\s)(.*)(?=:)', s).group(0)
	password = re.search('(?<=:\s)(.*)', s).group(0)


	# PART ONE
	# count how many key characters there are in the password
	i = password.count(key)

	# if password contains as many key characters as needed but not more than allowed, the string is added to the 'valid' list
	if i >= min and i <= max:
		validLines1.append(s)

	# PART TWO
	# min and max indicate exact positions in the password
	# exactly one of these positions must contain the key character for the password to be valid
	
	if password[min-1] == key and password[max-1] != key:
		validLines2.append(s)
	elif password[min-1] != key and password[max-1] == key:
		validLines2.append(s)

answer1 = len(validLines1)
answer2 = len(validLines2)

print("Answer 1 is", answer1)
print("Answer 2 is", answer2)
