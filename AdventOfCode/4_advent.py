# Advent of Code 2020 day 4
# https://adventofcode.com/

# The task is to check whether each series of data ("passport") contains all of the required information.

import re
import string

with open('4_data.txt') as f:
	lines = f.read()

lines = lines.split('\n\n')
lines = [l.replace('\n', ' ') for l in lines]

checkList = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
valid = []

# TASK 1
# Count how many of the passports have all required fields.

for i in range(0, len(lines)):
	if all(c in lines[i] for c in checkList):
		valid.append(lines[i])
	else:
		continue

print("The data set contains", len(valid), "passports that have the required fields.")


# TASK 2 - Data validation
# byr - 4 digits, 1920-2002
# iyr - 4 digits, 2010-2020
# eyr - 4 digits, 2020-2030
# hgt - a number followed by cm or in
#  	if cm, 150-193
# 	if in, 59-76
# hcl - '#' followed by exactly 6 characters 0-9 or a-f
# ecl - exactly one of amb blu brn gry grn hzl oth
# pid - 9 digits
# cid - ignored, missing or not

# Count all passwords where all required fields are both present and valid according to the above rules.

# First creating a function that contains all the rules.
# The function will take the key and value pair as input and check whether the value is valid.

def validate(k, v):

	if k == 'byr':
		if len(str(v)) == 4 \
				and 1919 < int(v) < 2003:
			return True

	elif k == 'iyr':
		if len(str(v)) == 4 \
				and 2009 < int(v) < 2021:
			return True

	elif k == 'eyr':
		if len(str(v)) == 4 \
				and 2019 < int(v) < 2031:
			return True

	elif k == 'hgt':
		height = int(re.findall('[0-9]+', v)[0])
		if 'cm' in v[3:] and 149 < height < 194:
			return True
		elif 'in' in v[2:] and 58 < height < 77:
			return True

	elif k == 'hcl':
		if len(v) == 7 \
				and v[0] == '#' \
				and	all(c in string.hexdigits for c in v[1:]):
			return True

	elif k == 'ecl':
		allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		if len(v) == 3 \
				and any(a in v for a in allowed):
			return True

	elif k == 'pid':
		if len(str(v)) == 9 \
				and v.isnumeric():
			return True

	elif k == 'cid':
		return True

	else:
		return False


# Turning the data set into a dictionary.

for i in range(0, len(valid)):
	valid[i] = valid[i].split(' ')
	valid[i] = dict(map(lambda s: s.split(':'), valid[i]))

# Going through each 'passport' and validating the data.
# Creating a copy of the list of valid passports, and removing every invalid passport from the new list.

valid2 = valid.copy()

for i in range(0, len(valid)):
	for key in valid[i].keys():
		if validate(key, valid[i][key]):
			continue
		else:
# 			print(key)
# 			print("Not valid:", valid[i])
			valid2.remove(valid[i])
			break

# The answer for Task 2 is the length of the new list of valid passports.

print("The data set contains", len(valid2), "valid passports.")
