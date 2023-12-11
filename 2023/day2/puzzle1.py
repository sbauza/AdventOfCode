import re

def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines


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
        if red > 12 or green > 13 or blue > 14:
            draws = []
            break                
        draws.append((red, green, blue))    
    return game, draws

def main(file):
    sum_hits = 0
    for line in read_file(file):
        line = line.rstrip('\n')
        game, draws = get_game(line)
        if draws:
            sum_hits += game
    return sum_hits

assert 8 == main('test.txt')
print(main('input.txt'))