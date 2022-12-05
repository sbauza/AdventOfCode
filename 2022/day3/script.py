#!/usr/bin/python

with open('input.txt', 'r') as fs:
    lines = fs.readlines()

sum_prio = 0
for line in lines:
    char = ''
    prio = 0
    line = line.strip()
    print(line)
    comp1, comp2 = line[:len(line)//2], line[len(line)//2:]
    common_set = set(comp1).intersection(set(comp2))
    print(common_set)
    if common_set:
        char = common_set.pop()
    if char.islower():
        prio = ord(char) - 96
    if char.isupper():
        prio = ord(char) - 38
    sum_prio += prio

print(sum_prio)