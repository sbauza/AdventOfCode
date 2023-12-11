import logging
import os
import re

log = logging.getLogger(__name__)
if os.environ.get('DEBUG'):
    logging.basicConfig(level=logging.DEBUG)


ASKED_Y = 10

def excludes_area(excludes: set, sensor: tuple, beacon: tuple):
    s_x, s_y = sensor
    b_x, b_y = beacon
    # Definition of the Manhattan distance between sensor and beacon
    distance = abs(b_x - s_x) + abs(b_y - s_y)
    log.warning(f'Distance between {sensor} and {beacon} : {distance}')
    for x in range(0, distance +1):
        for y in range(0, distance +1):
            if x + y <= distance:
                if os.environ.get('DEBUG'):
                    excludes.add((s_x + x, s_y + y))
                    excludes.add((s_x - x, s_y + y))
                    excludes.add((s_x - x, s_y - y))
                    excludes.add((s_x + x, s_y - y))
                else:
                    if s_y - y == ASKED_Y:
                        excludes.add((s_x - x, s_y - y))
                        excludes.add((s_x + x, s_y - y))
                    elif s_y + y == ASKED_Y:
                        excludes.add((s_x + x, s_y + y))
                        excludes.add((s_x - x, s_y + y))                

def run(file, part2=False):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    pattern = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    excludes = set()
    known_positions = set()
    for line in lines:
        match = re.search(pattern, line)
        if match:
            s_x, s_y, b_x, b_y = map(int, match.groups())
            excludes_area(excludes, (s_x, s_y),(b_x, b_y))
            known_positions = known_positions.union([(s_x, s_y),(b_x, b_y)])
    log.debug(f"Known positions {known_positions}")
    count_cannot = 0
    unknown_positions = excludes - known_positions
    for x, y in unknown_positions:
        if y == 10:
            log.debug(f'Found excluded {(x, y)}')
            count_cannot += 1
    print("Cannot : %s" % count_cannot)
    return count_cannot

assert 26 == run('test.txt')
print('Answer 1: %s' % run('input.txt'))

# assert 0 == run('test.txt', part2=True)
# print('Answer 2: %s' % run('input.txt', part2=True))
