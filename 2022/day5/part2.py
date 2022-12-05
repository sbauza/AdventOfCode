#!/usr/bin/python

import re


def run(file):
    with open(file, 'r') as fs:
        lines = fs.readlines()

    stacks_to_read = []
    nb_stacks = 0
    instructions = []
    for line in lines:
        line = line.rstrip('\n')
        if '[' in line:
            # we need to pile
            stacks_to_read.append(line)
        elif line.startswith(' 1'):
            # calculate the stacks number
            raw_line = line.split(' ')
            nb_stacks = max([int(char) for char in raw_line if char.isnumeric()])
        elif line.startswith('move'):
            # That's an instruction
            instructions.append(line)


    cargo = [[] for i in range(nb_stacks)]
    pattern = ''
    pattern += r'[\[ ]([\w ])[\] ]\ ?'*nb_stacks
    # Now, read the stacks
    for line in reversed(stacks_to_read):
        match = re.search(pattern, line)
        crates = match.groups()
        for pos, crate in enumerate(crates):
            if crate and crate != ' ':
                cargo[pos].append(crate)

    print(f'Begin: {cargo}')
    #now, let's read the instructions so we can flip the crates between stakes.
    for instruction in instructions:
        pattern = r'move (\d+) from (\d+) to (\d+)'
        match = re.search(pattern, instruction)
        if not match:
            print("wrong line")
            continue
        match = match.groups()
        nb_crates_to_move = int(match[0])
        from_stack = int(match[1])
        to_stack = int(match[2])

        #The part2 change ;-)
        crates_to_move = cargo[from_stack-1][-nb_crates_to_move:]
        del cargo[from_stack-1][-nb_crates_to_move:]
        cargo[to_stack-1].extend(crates_to_move)
    print(cargo)

    message = ''
    for i in range(nb_stacks):
        message += cargo[i][-1]
    return message

assert 'MCD' == run('test.txt')

print(run('input.txt'))