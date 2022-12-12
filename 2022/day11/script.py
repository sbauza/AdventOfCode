import re

DEBUG = True

def debug(str, format=None):
    global DEBUG
    if DEBUG == True:
        if format:
            print(str % format)
        else:
            print(str)


def create_monkeys(file):
    monkeys = {}

    with open(file, mode='r') as fs:
        lines = fs.readlines()

    current_monkey = None
    is_monkey = re.compile(r'Monkey (\d+):')
    is_test = re.compile(r'Test: divisible by (\d+)')
    is_true = re.compile(r'If true: throw to monkey (\d+)')
    is_false = re.compile(r'If false: throw to monkey (\d+)')
    for line in lines:
        line = line.rstrip('\n')
        match_monkey = re.search(is_monkey, line)
        match_test = re.search(is_test, line)
        match_true = re.search(is_true, line)
        match_false = re.search(is_false, line)
        if match_monkey is not None:
            current_monkey = match_monkey.groups()[0]
            if current_monkey not in monkeys:
                monkeys[current_monkey] = {}
        elif 'Starting items' in line:
            items = line.split(':')[1].replace(' ', '').split(',')
            items = [int(item) for item in items]
            monkeys[current_monkey]['items'] = items
        elif 'Operation' in line:
            old, operator, operand = line.split('=')[1].lstrip().split(' ')
            monkeys[current_monkey]['operator'] = operator
            monkeys[current_monkey]['operand'] = operand
        elif match_test is not None:
            divisible = match_test.groups()[0]
            monkeys[current_monkey]['divisible'] = int(divisible)
        elif match_true is not None:
            monkey_true = match_true.groups()[0]
            monkeys[current_monkey]['true'] = monkey_true
        elif match_false is not None:
            monkey_false = match_false.groups()[0]
            monkeys[current_monkey]['false'] = monkey_false
    return monkeys


def play(file, part2=False):
    monkeys = create_monkeys(file)

    if part2:
        rounds = 10000
    else:
        rounds = 20
    inspections = [0] * len(monkeys)

    lcm = 1
    for monkey in monkeys.values():
        lcm *= monkey['divisible']
    for _round in range(1, rounds + 1):
        print('Round %s' % _round)
        for monkey_n, monkey in monkeys.items():
            debug('Monkey %s:', monkey_n)
            debug(monkey)
            for item in monkey['items']:
                debug('Monkey inspects an item with a worry level of %d ', item)
                inspections[int(monkey_n)] += 1
                operator = monkey['operator']
                if operator == '*':
                    item *= (int(monkey['operand'])
                             if monkey['operand'] != 'old' else item)
                if operator == '+':
                    item += int(monkey['operand'])
                debug('New value of item after operation: %d', item)
                if not part2:
                    item //=  3
                    debug('Divided by 3: %d', item)
                else:
                    item %= lcm
                if item % monkey['divisible'] == 0:
                    debug(f'Divisible by {monkey["divisible"]}')
                    send_to = 'true'
                else:
                    debug(f'not Divisible by {monkey["divisible"]}')
                    send_to = 'false'
                debug('%d thrown to monkey %s', (item, monkey[send_to]))
                monkeys[monkey[send_to]]['items'].append(item)
            monkeys[monkey_n]['items'] = []
    debug(monkeys)
    # Let's arrange this by the number of inspections
    inspections_arranged = sorted(inspections, reverse=True)

    return inspections_arranged[0] * inspections_arranged[1]

assert 10605 == play('test.txt')
DEBUG = False
assert 2713310158 == play('test.txt', part2=True)

print('Answer 1: %s' % play('input.txt'))
print('Answer 2 : %s' % play('input.txt', part2=True))
