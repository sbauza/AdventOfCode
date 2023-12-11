import functools
import re

def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def get_max_rgb(rgb1, rgb2):
    return (max(rgb1[0], rgb2[0]),
            max(rgb1[1], rgb2[1]),
            max(rgb1[2], rgb2[2]))

def get_game(line):
    game = 0
    draws = []
    _game, _draws = line.split(': ')
    game = re.findall(r'\d+', _game)[0]
    game = int(game)
    for _draw in _draws.split('; '):
        red = green = blue = 0
        for match in re.finditer(r'(\d+) (\w+)[,]?', _draw):
            nb = match.group(1)
            color = match.group(2)
            red = int(nb) if color == 'red' else red
            green = int(nb) if color == 'green' else green
            blue = int(nb) if color == 'blue' else blue
        draws.append((red, green, blue))
    max_rgb = functools.reduce(get_max_rgb, draws)
    return game, max_rgb

def main(file):
    sum_hits = 0
    for line in read_file(file):
        line = line.rstrip('\n')
        game, max_rgb = get_game(line)
        sum_hits += (max_rgb[0] * max_rgb[1] * max_rgb[2])
    return sum_hits

assert 2286 == main('test.txt')
print(main('input.txt'))