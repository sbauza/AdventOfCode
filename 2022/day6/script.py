#!/usr/bin/python


def parse(input):
    index = 4
    found = False
    while not found and index <= len(input):
        buffer = input[index-4:index]
        if len(set(buffer)) == 4:
            found = True
        else:
            index += 1
    return index if found else None

assert 7 == parse('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
assert 5 == parse('bvwbjplbgvbhsrlpgdmjqwftvncz')
assert 6 == parse('nppdvjthqldpwncqszvftbrmjlhg')
assert 10 == parse('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
assert 11 == parse('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')

with open('input.txt', 'r') as fs:
    lines = fs.readlines()

assert len(lines) == 1
print(parse(lines[0]))
