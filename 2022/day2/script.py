#!/usr/bin/python


# Rock wins Scissors 1 > 3
# Paper wins Rock 2 > 1
# Scissors wins Paper 3 > 2

OP_ = ['A', 'B', 'C']
ME_ = ['X', 'Y', 'Z']


def fight(opponent, me):
    if OP_.index(opponent) == 2 and ME_.index(me) == 0:
        return 6
    elif OP_.index(opponent) == ME_.index(me):
        return 3
    elif OP_.index(opponent) < ME_.index(me):
        if not (OP_.index(opponent) == 0 and ME_.index(me) == 2):
            return 6
        else:
            return 0
    else:
        return 0

def calc(opponent, hint):
    if hint == 'Y':
        # we need to draw
        me = ME_[OP_.index(opponent)]
        return me
    elif hint == 'X':
        return ME_[OP_.index(opponent)-1]
    else:
        try:
            return ME_[OP_.index(opponent)+1]
        except IndexError:
            return 'X'

with open('input.txt', 'r') as fs:
    lines = fs.readlines()

total = 0
for line in lines:
    print(line)
    opponent, hint = line.strip().split(' ')
    me = calc(opponent, hint)
    res = fight(opponent, me)
    shape = ME_.index(me) + 1
    rnd = res + shape
    print(rnd)
    total += rnd


print(f'Total: {total}')