import logging
import os

log = logging.getLogger(__name__)
if os.environ.get('DEBUG'):
    logging.basicConfig(level=logging.DEBUG)


def allocate_rocks(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    coordinates = set()
    for rock_path in lines:
        raw_coords = rock_path.rstrip('\n').split(' -> ')
        old_x = old_y = None
        for raw_coord in raw_coords:
            x, y = (int(i) for i in raw_coord.split(','))
            if old_y and old_x:
                diff_x = x - old_x
                diff_y = y - old_y
                if diff_x:
                    min_x = min(old_x, x)
                    coordinates = coordinates.union([(i, y) for i in range(min_x + 1, min_x + abs(diff_x))])
                elif diff_y:
                    min_y = min(old_y, y)
                    coordinates = coordinates.union([(x, i) for i in range(min_y + 1, min_y + abs(diff_y))])
            coordinates.add((x, y))
            old_x, old_y = x, y

    return coordinates

class FakeCoordinates:
    def __init__(self, coordinates, max_y):
        self.coordinates = coordinates
        self.max_y = max_y
    def __contains__(self, item):
        return item in self.coordinates or item[1] == self.max_y + 2
    def add(self, item):
        self.coordinates.add(item)

    
def leak_sand(coordinates, part2):
    # We shouldn't have more grains of sand that the number of units we have
    max_y = max(y for (x, y) in coordinates)
    max_x = max(x for (x, y) in coordinates)

    if part2:
        coordinates = FakeCoordinates(coordinates, max_y)
    for sand_grains in range(max_x * max_y):
        sand = (500, 0)
        rested = False
        out = False
        while not rested:
            x, y = sand
            if not part2:
                if y > max_y:
                    out = True
                    break
            if part2 and (500, 0) in coordinates:
                # That means we stayed at the top
                out = True
                break
            if not (x, y + 1) in coordinates:
                sand = (x, y + 1)
            elif not (x - 1, y + 1) in coordinates:
                sand = (x - 1, y + 1)
            elif not (x + 1, y + 1) in coordinates:
                    sand = (x + 1, y + 1)
            else:
                coordinates.add((x, y))
                log.debug('Rested: '+ str((x, y)))
                rested = True

        if out:
            break
    log.debug("Total: %s" % sand_grains)
    # 
    return sand_grains

def run(file, part2=False):
    coordinates = allocate_rocks(file)
    return leak_sand(coordinates, part2)

assert 24 == run('test.txt')
print('Answer 1: %s' % run('input.txt'))

assert 93 == run('test.txt', part2=True)
print('Answer 2: %s' % run('input.txt', part2=True))
