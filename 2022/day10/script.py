BUFFER = ''


def parse(file):
    global BUFFER
    with open(file, 'r') as fs:
        lines = fs.readlines()

    cycle = 0
    X = 1
    lines_i = iter(lines)
    addx = None
    sum_signal_strengths = 0
    while True or cycle > 240:
        # Cycle in progress
        sprite_row = cycle % 40
        if sprite_row == 0:
            BUFFER += '\n'
        if sprite_row >= X - 1 and sprite_row <= X + 1:
            BUFFER += '#'
        else:
            BUFFER += '.'
        cycle += 1
        # End of cycle
        if (cycle - 20) % 40 == 0:
            print(f'Current cycle {cycle}')
            signal_strength = cycle * X
            print(f'Signal strength: {X}')
            sum_signal_strengths += signal_strength
        if addx:
            # We're at the end of the cycle, we can set the register.
            X += addx
            addx = None
            # Skip the parsing line for the next cycle
            continue 
        try:
            line = next(lines_i)
        except StopIteration:
            break
        line = line.rstrip('\n')
        instructions = line.split(' ')
        if instructions[0] == 'addx':
            # Pass it for the next loop
            addx = int(instructions[1])

    return sum_signal_strengths

assert 13140 == parse('test.txt')
print(BUFFER)

BUFFER = ''
print('Answer1 : %s' % parse('input.txt'))
print(BUFFER)
