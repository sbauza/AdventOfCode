#!/usr/bin/python


#Part 1
def get_floor(input):
    open_bracket = input.count('(')
    closing_bracket = input.count(')')
    return open_bracket - closing_bracket

assert 0 == get_floor('(())')
assert 0 == get_floor('()()')
assert 3 == get_floor('(((')
assert 3 == get_floor('(()(()(')

with open('input.txt', 'r') as fs:
    lines = fs.readlines()

assert len(lines) == 1
print(get_floor(lines[0]))

#Part2

def get_basement_pos(input):
    index = 1
    floor = 0
    for char in input:
        if char == '(':
            floor += 1
        if char == ')':
            floor -= 1
        if floor == -1:
            break
        index += 1
    return index


assert 1 == get_basement_pos(')')
assert 5 == get_basement_pos('()())')

print(get_basement_pos(lines[0]))
