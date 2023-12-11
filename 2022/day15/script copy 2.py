from functools import reduce
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

    max_y = max_x = 20 if file == 'test.txt' else 4000000
    if not part2:
        targets = [10 if file == 'test.txt' else 2000000]
    else:
        targets = [y for y in range(0, max_y + 1)]
    ranges = dict()
    for target_y in targets:
        log.debug('Scanning row %s' % target_y)
        ranges[target_y] = sensors_ranges_for_y(known_sensors_with_distance, target_y)


    def reduce_set(x, y):
        if y[0] > x[0] + 1:
            # both ranges aren't contiguous
            pass
        
    spotted = set()
    for target_y, ranges in ranges.items():
        ranges = reduce(reduce_set,ranges, initial=set())
        for min_range, max_range in ranges:
            if part2:
                if max_range < 0 or min_range > max_x:
                    continue
                min_range = max(min_range, 0)
                max_range = min(max_range, max_x)
            for x in range(min_range, max_range + 1):
                if (x, target_y) in known_positions:
                    continue
                if part2 and x > max_x:
                    continue
                if not part2:
                    spotted.add((x, target_y))
                else:
                    known_positions.append(((x, target_y)))
    log.debug('Spotted : %s' % len(spotted))
    log.debug('Known : %s' % len(known_positions))
    return len(spotted)

def sensors_ranges_for_y(known_sensors_with_distance, target_y):

    ranges = set()
    for s_x, s_y, distance in known_sensors_with_distance:
        offset_y = abs(s_y - target_y)
        # we report the distance between the vertical point to the line and then
        # we calculate the left distance so the total of offset_y + offset_x is
        # equal to the sensor detection distance
        if distance < offset_y:
            # the sensor is too far from the row we check
            continue
        offset_x = abs(distance - offset_y)
        log.debug(f'offsets : {(offset_x, offset_y)}')
        # then we can consider that any position before and after this offset
        # with vertical coordinate of target_y can be detected by this sensor.
        s_min_x_for_t_y = s_x - offset_x
        s_max_x_for_t_y = s_x + offset_x
        log.debug(f'{(s_x, s_y, distance)} can detect '
                  f'[{s_min_x_for_t_y}-{s_max_x_for_t_y}] on {target_y}')
        assert offset_y + offset_x == distance

        ranges.add((s_min_x_for_t_y, s_max_x_for_t_y))
    ranges = sorted(ranges, key=lambda pos: pos[0])

    log.debug(f'On {target_y}, detected ranges : {ranges}')
    return ranges

    # min_x = known_sensors_with_distance[0][0]
    # max_x = known_sensors_with_distance[-1][0]
    # for s_x, s_y, distance in known_sensors_with_distance:
    #     offset_y = abs(s_y - target_y)
    #     if offset_y > distance:
    #         # this sensor is too far from what we want to check
    #         known_sensors_with_distance.remove((s_x, s_y, distance))
    #     # report the y offset to x to know the min and max values for this
    #     # sensor that can be detected.
    #     s_min_x = s_x - offset_y
    #     s_max_x = s_x + offset_y
    #     min_x = min(min_x, s_min_x)
    #     max_x = max(max_x, s_max_x)

    # log.warning(f"Min x : {min_x}, Max: {max_x}")
    # return min_x,max_x


assert 26 == run('test.txt')
# print('Answer 1: %s' % run('input.txt'))

assert 0 == run('test.txt', part2=True)
# print('Answer 2: %s' % run('input.txt', part2=True))
