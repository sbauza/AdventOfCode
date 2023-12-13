import re


def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def parse(file):
    # this is a dict of dicts
    mappings = {}
    lines = read_file(file)
    map = None
    seeds = []
    for line in lines:
        line = line.rstrip('\n')
        finds = re.findall(r'[\w-]+', line)
        if not finds:
            continue
        if finds[0] == 'seeds':
            seeds = [int(_seed) for _seed in finds[1:]]
        elif finds[1] == 'map':
            map = finds[0]
        else:
            if not map:
                print('stop with error %s' % finds)
                return
            if len(finds) != 3:
                print('invalid %s' % finds)
                return
            cur_map = [int(v) for v in finds]
            dest, source, length = cur_map
            state_map = mappings.setdefault(map, {})
            state_map[(source, length)] = (dest, length)
    return seeds, mappings


def get_dest_from_source(mappings, map_name, source):
    mapping = mappings[map_name]
    for (s, l), (d, _l) in mapping.items():
        if source >= s and source < s + l:
            diff = source - s
            return d + diff
    return source

def main(file):
    seeds, mappings = parse(file)
    states = ['seed', 'soil', 'fertilizer', 'water', 'light',
              'temperature', 'humidity', 'location']
    locations = []
    for seed in seeds :
        src = seed
        for idx, st in enumerate(states):
            if idx >= len(states) -1 :
                break
            map_to_call = st + '-to-' + states[idx+1]
            src = get_dest_from_source(mappings, map_to_call, src)
        locations.append(src)
    return min(locations)


assert 35 == main('test.txt')
print(main('input.txt'))