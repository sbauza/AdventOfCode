import re

def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def main(file):
    lines = read_file(file)

    instructions = list(lines[0].rstrip('\n'))
    network = {}
    for line in lines[2:]:
        start, left, right = re.findall(r'\w+', line)
        network[start] = (left, right)

    pos = 'AAA'
    steps = 0
    while pos != 'ZZZ':
        instruction = instructions[steps % len(instructions)]
        steps += 1
        pos = network[pos][0] if instruction == 'L' else network[pos][1]
    return steps

assert 2 == main('test1.txt')
assert 6 == main('test2.txt')

print(main('input.txt'))