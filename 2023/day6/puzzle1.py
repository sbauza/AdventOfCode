import re


def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def main(file):
    lines = read_file(file)
    times = list(map(int, re.findall(r'\d+', lines[0])))
    distances = list(map(int, re.findall(r'\d+', lines[1])))
    prod_wins = 1
    for time, distance in zip(times, distances):
        wins = 0
        for hold in range(time):
            run_time = time - hold
            if hold * run_time > distance:
                wins += 1
        prod_wins *= wins
    return prod_wins
assert 288 == main('test.txt')
print(main('input.txt'))