#!/usr/bin/python

with open('input.txt', 'r') as fs:
    lines = fs.readlines()

elves_assignments = []
max_max = 0
for line in lines:
    line = line.strip()
    print(line)
    elf1, elf2 = line.split(',')
    temp_ass = []
    for elf in [elf1, elf2]:
        min, max = elf.split('-')
        temp_ass.append([int(min), int(max)])
        if int(max) > max_max:
            max_max = int(max)
    elves_assignments.append(temp_ass)

# assert max_max == 99

double_assignements = 0
print(elves_assignments)
for elves_pair in elves_assignments:
    print(elves_pair)
    min1, max1 = elves_pair[0]
    min2, max2 = elves_pair[1]
    if min1 <= min2 and max1 >= max2:
        # elf1 assignment over elf2
        print('elf1')
        double_assignements += 1
    elif min2 <= min1 and max2 >= max1:
        print('elf2')
        double_assignements += 1

print(double_assignements)

overlaps = 0
for elves_pair in elves_assignments:
    print(elves_pair)
    min1, max1 = elves_pair[0]
    min2, max2 = elves_pair[1]
    if min1 <= min2 and not max1 < min2 :
        # elf1 assignment overlaps elf2
        print('elf1')
        overlaps += 1
    elif min2 <= min1 and not max2 < min1:
        print('elf2')
        overlaps += 1
print(overlaps)
