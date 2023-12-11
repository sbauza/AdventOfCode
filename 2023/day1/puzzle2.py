
def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines


letters_to_digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def digit_is_letters(line):
    for letter in letters_to_digits:
        if line.startswith(letter):
            return letters_to_digits[letter]
    return False

def sum_digits(file):
    lines = read_file(file)
    sum = 0
    for line in lines:
        first = ''
        last = ''
        for idx, char in enumerate(line):
            if char.isdigit():
                last = char
                if not first:
                    first = char
            else:
                left_line = line[idx:]
                digit = digit_is_letters(left_line)
                if digit:
                    last = digit
                    if not first:
                        first = digit
        cur = str(first) + '' + str(last)
        print(cur)
        sum += int(cur)
    print(sum)
    return sum

assert 281 == sum_digits('test2.txt')
sum_digits('input.txt')
