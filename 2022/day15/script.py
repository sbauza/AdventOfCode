import logging
import os
import re

log = logging.getLogger(__name__)
if os.environ.get('DEBUG'):
    logging.basicConfig(level=logging.DEBUG)


def run(file, part2=False):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    pattern = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    excludes = set()
    known_positions = set()
    known_sensors_with_distance = set()
    for line in lines:
        match = re.search(pattern, line)
        if match:
            s_x, s_y, b_x, b_y = map(int, match.groups())
            # Definition of the Manhattan distance between sensor and beacon
            distance = abs(b_x - s_x) + abs(b_y - s_y)
            known_sensors_with_distance.add(((s_x, s_y, distance)))
            known_positions = known_positions.union([(s_x, s_y),(b_x, b_y)])

    known_positions = sorted(known_positions, key=lambda pos: pos[0])
    known_sensors_with_distance = sorted(known_sensors_with_distance,
                                         key=lambda pos: pos[0])

    target_y = 10 if file == 'test.txt' else 2000000

    cannot_positions = set()

    min_x = known_sensors_with_distance[0][0]
    max_x = known_sensors_with_distance[-1][0]
    for s_x, s_y, distance in known_sensors_with_distance:
        offset_y = abs(s_y - target_y)
        if offset_y > distance:
            # this sensor is too far from what we want to check
            known_sensors_with_distance.remove((s_x, s_y, distance))
        # report the y offset to x to know the min and max values for this
        # sensor that can be detected.
        s_min_x = s_x - offset_y
        s_max_x = s_x + offset_y
        min_x = min(min_x, s_min_x)
        max_x = max(max_x, s_max_x)
        if part2:
            max_zone = 20 if file == 'test.txt' else 4000000
            if (s_x + distance < 0 or s_x - distance > 20
                or s_y + distance < 0 or s_y - distance > 20):
                # this sensor can't detect this zone.
                known_sensors_with_distance.remove((s_x, s_y, distance))
    log.warning(f"Min x : {min_x}, Max: {max_x}")

    for x in range(min_x, max_x + 1):
        if (x, target_y) in known_positions:
            continue
        for s_x, s_y, distance in known_sensors_with_distance:
            # if (s_x + distance) < x or (s_x - distance) > x:
            #     continue
            if abs(x - s_x) + abs(target_y - s_y) <= distance:
                log.debug(f"{(x, target_y)} can't exist due to less or eq "
                          f"{distance} from {s_x, s_y}")
                cannot_positions.add((x, target_y))
        if x % 100000 == 0:
            log.warning(f"Currently at {(x - min_x) * 100 // (max_x - min_x)}%")
    log.debug(f"Total of cannot positions {len(cannot_positions)}")
    return len(cannot_positions)


assert 26 == run('test.txt')
print('Answer 1: %s' % run('input.txt'))

# assert 0 == run('test.txt', part2=True)
# print('Answer 2: %s' % run('input.txt', part2=True))
