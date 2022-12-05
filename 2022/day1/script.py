#!/usr/bin/python

with open('input.txt', 'r') as fs:
    lines = fs.readlines()

elves = set()
num_elves = 0
cur_elf = 0
for line in lines:
    if line.strip() == '':
        elves.add(cur_elf)
        cur_elf = 0
        num_elves += 1
    else:
        cur_elf += int(line.strip())

print(elves)
print(max(elves))
sorted_elves = sorted(elves)
print(sorted_elves)
print(sorted_elves[-3:])
print(sum(elf for elf in sorted_elves[-3:]))