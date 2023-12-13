import re
from tqdm import tqdm


def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def main(file):
    lines = read_file(file)
    time = int(''.join(re.findall(r'\d+', lines[0])))
    distance = int(''.join(re.findall(r'\d+', lines[1])))
    wins = 0
    for hold in tqdm(range(time)):
        run_time = time - hold
        if hold * run_time > distance:
            wins += 1
    return wins
assert 71503 == main('test.txt')
print(main('input.txt'))