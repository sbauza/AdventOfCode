import re
import math

def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines

def main(file):
    lines = read_file(file)
    time = int(''.join(re.findall(r'\d+', lines[0])))
    distance = int(''.join(re.findall(r'\d+', lines[1])))
    wins = 0
    # We need to resolve the polynomial expression : 
    # hold * run_time > distance which translates into a 2nd degree equation :
    # hold * (time - hold) - distance > 0
    # we can factorize hold here :
    # hold * time - hold * hold - distance > 0
    # this way we have a polynomial equation :
    # - x^2 + x * y - z > 0 
    # and its discriminant is time * time - 4 * (-1) * -distance
    discriminant = time**2 - 4 * -distance * -1
    lower_bound = (-1 * time + math.sqrt(discriminant)) / (2 * -1)
    higher_bound = (-1 * time - math.sqrt(discriminant)) / (2 * -1)
    low = int(math.floor(lower_bound) +1) # we need the next one
    high = int(math.ceil(higher_bound)-1) # we need the previous one
    return (high - low + 1)

assert 71503 == main('test.txt')
print(main('input.txt'))