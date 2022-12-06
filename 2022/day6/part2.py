#!/usr/bin/python


def parse(input):
    index = 14
    found = False
    while not found and index <= len(input):
        buffer = input[index-14:index]
        if len(set(buffer)) == 14:
            found = True
        else:
            index += 1
    return index if found else None

assert 19 == parse('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
assert 23 == parse('bvwbjplbgvbhsrlpgdmjqwftvncz')
assert 23 == parse('nppdvjthqldpwncqszvftbrmjlhg')
assert 29 == parse('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
assert 26 == parse('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
assert None == parse('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
assert None == parse('a')

with open('input.txt', 'r') as fs:
    lines = fs.readlines()

assert len(lines) == 1
print(parse(lines[0]))
