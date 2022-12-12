from collections import deque
import logging

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

def parse_map(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    map = []
    for line in lines:
        line = line.rstrip('\n')
        map.append(list(line))
    return map

def locate_position(spot, map, all=False):
    all_positions = []
    for idx_h, line in enumerate(map):
        for idx_v, char in enumerate(line):
            if char == spot:
                if not all:
                    all_positions = [(idx_h, idx_v)]
                    break
                else:
                    all_positions.append((idx_h, idx_v))
    if all_positions and not all:
        return all_positions[0]
    elif not all_positions:
        return (None, None)
    else:
        return all_positions
    
def game(file, part2=False):
    map = parse_map(file)
    position = locate_position('S', map)
    map[position[0]][position[1]] = 'a'
    end_position = locate_position('E', map)
    map[end_position[0]][end_position[1]] = 'z'
    if part2:
        a_positions = locate_position('a', map, all=True)
        results = []
        for a_pos in a_positions:
            result = run(map, a_pos, end_position)
            if result:
                results.append(result)
        final_result = min(results)
    else:
        final_result = run(map, position, end_position)
    return final_result

def run(map, position, end_position):
    step_count = 0
    # Let's add a queue to remember the ways
    to_process = deque()
    to_process.append((step_count, position))
    # we need to remember which positions we already checked.
    visited_history = set(position)
    while to_process:
        step_count, position = to_process.popleft()
        letter_pos = map[position[0]][position[1]]
        adjacents = [(position[0] - 1, position[1]),
                     (position[0] + 1, position[1]),
                     (position[0], position[1] - 1),
                     (position[0], position[1] + 1)]
        for neighbor in adjacents:
            x, y = neighbor
            if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
                # we're out of the bounds of the map
                continue
            if ord(map[x][y]) - ord(letter_pos) > 1:
                # there is at least one letter between the position and
                # the neighbor
                logger.debug('Skip %s due to %s too higher than %s' % (
                    neighbor, map[x][y], letter_pos))
                continue
            if neighbor in visited_history:
                logger.debug('Skip because (%s,%s) already visited' % neighbor)
                continue
            if neighbor == end_position:
                step_count += 1
                logger.debug('Exit found in %s steps' % step_count )
                return step_count
            visited_history.add(neighbor)
            to_process.append((step_count + 1, neighbor))

assert 31 == game('test.txt')
print('Answer1 : %s' % game('input.txt'))

assert 29 == game('test.txt', part2=True)
print('Answer2 : %s' % game('input.txt', part2=True))
