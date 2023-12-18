import math
import re

def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def main(file):
    lines = read_file(file)

    instructions = list(lines[0].rstrip('\n'))
    network = {}
    positions = []
    for line in lines[2:]:
        start, left, right = re.findall(r'\w+', line)
        if start.endswith('A'):
            positions.append(start)
        network[start] = (left, right)

    counts = []
    for idx, pos in enumerate(positions):
        steps = 0
        while not pos.endswith('Z'):
            instruction = instructions[steps % len(instructions)]
            steps += 1
            pos = network[pos][0] if instruction == 'L' else network[pos][1]
        counts.append(steps)
    return math.lcm(*counts)

assert 6 == main('test3.txt')

print(main('input.txt'))