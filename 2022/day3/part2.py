#!/usr/bin/python

with open('input.txt', 'r') as fs:
    lines = fs.readlines()

sum_prio = 0

temp_group = []
for idx, line in enumerate(lines):
    char = ''
    prio = 0
    common_set = set()
    line = line.strip()
    print(line)
    temp_group.append(line)
    if idx % 3 == 2:
        common_set = set(temp_group[0]).intersection(set(temp_group[1])).intersection(set(temp_group[2]))
        temp_group = []
    print(common_set)
    if common_set:
        char = common_set.pop()
    if char.islower():
        prio = ord(char) - 96
    if char.isupper():
        prio = ord(char) - 38
    sum_prio += prio

print(sum_prio)