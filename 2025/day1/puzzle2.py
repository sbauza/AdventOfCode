
def read_file(file):
    with open(file, mode='r') as fs:
        lines = fs.readlines()
    return lines


def sum_digits(file):
    lines = read_file(file)
    pos = 50
    sum = 0
    for line in lines:
        direction = -1 if line[0] == 'L' else 1
        move = int(line[1:])
        
        new_pos = (pos + direction * move) % 100
        
        if direction == 1:  # moving right
            count = (pos + move) // 100
            sum += count
        else:  # moving left (direction == -1)
            if pos == 0:
                count = move // 100
            else:
                if pos < move:
                    # When landing on a multiple of 100, we need to count it
                    count = (move - pos) // 100 + 1
                else:
                    count = 1 if (pos - move) == 0 else 0
            sum += count
        
        pos = new_pos
        print(pos)
    print(sum)
    return sum

assert 6 == sum_digits('test1.txt')
sum_digits('input.txt')
