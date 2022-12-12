import numpy as np
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

    monkey_items = []
    for _m, v in monkeys.items():
        monkey_items.append(np.array([i for i in v['items']], dtype=np.int_))
    # we gonna trick by finding the least common multiple between all the
    # divisible numbers
    lcm = np.prod([monkey['divisible'] for monkey in monkeys.values()])
    for _round in range(1, rounds + 1):
        print('Round %s' % _round)
        for monkey_n, monkey in monkeys.items():
            monkey_n = int(monkey_n)
            debug('Monkey %s:' % monkey_n)
            debug('Monkey items: %s' % monkey_items[monkey_n])
            operator = monkey['operator']
            if operator == '*':
                if monkey['operand'] == 'old':
                    monkey_items[monkey_n] **= 2
                else:
                    monkey_items[monkey_n] *= int(monkey['operand'])
            if operator == '+':
                monkey_items[monkey_n] += int(monkey['operand'])
            if not part2:
                monkey_items[monkey_n] //= 3 
            else:
                # for part2, let's take our best chances with the LCM
                monkey_items[monkey_n] %= lcm
            modulo_items = monkey_items[monkey_n] % monkey['divisible']
            divisibles = monkey_items[monkey_n][np.where(modulo_items == 0)]
            non_divisibles = monkey_items[monkey_n][np.where(modulo_items != 0)]
            inspections[monkey_n] += divisibles.size + non_divisibles.size

            monkey_items[int(monkey['true'])] = np.append(
                monkey_items[int(monkey['true'])], divisibles)
            monkey_items[int(monkey['false'])] = np.append(
                monkey_items[int(monkey['false'])], non_divisibles)
            monkey_items[int(monkey_n)] = np.array([], dtype=np.int_)
        if _round in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000,
                      9000, 10000]:
            debug('Round %s' % _round)
            debug(inspections)
    # Let's arrange this by the number of inspections
    inspections_arranged = sorted(inspections, reverse=True)
    print(inspections_arranged)

    return inspections_arranged[0] * inspections_arranged[1]

assert 10605 == play('test.txt')
print('Answer 1: %s' % play('input.txt'))

DEBUG = False
assert 2713310158 == play('test.txt', part2=True)

print('Answer 2 : %s' % play('input.txt', part2=True))
