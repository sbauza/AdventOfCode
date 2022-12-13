from collections import deque
from functools import cmp_to_key

def count(file, part2=False):
    with open(file, mode='r') as fs:
        lines = fs.readlines()

    pairs = [[eval(lines[idx*3].rstrip('\n')), 
              eval(lines[idx*3+1].rstrip('\n'))]
              for idx in range((len(lines) // 3) +1 )]

    sum_indexes = 0
    for idx, pair in enumerate(pairs, 1):
        valid = is_pair_valid(pair)
        if valid:
            sum_indexes += idx
    if not part2:
        return sum_indexes
    # we're now on part2
    packets = [packet for pair in pairs for packet in pair]       
    packets.append([[2]]) 
    packets.append([[6]]) 
    sorted_packets = sorted(packets,
                            key=cmp_to_key(
                                lambda x,y: -1 if is_pair_valid([x, y]) else 1))
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)

def is_pair_valid(pair):
    pair = [deque(v) for v in pair]
    while len(pair[0]) > 0 and len(pair[1]) > 0:
        left = pair[0].popleft()
        right = pair[1].popleft()
        if isinstance(left, int) and isinstance(right, int):
            if left == right:                    
                continue
            elif left < right:
                return True
            else:
                return False
        if isinstance(left, list) and isinstance(right, list):
            ret = is_pair_valid([left, right])
            if ret is None:
                continue
            else:
                return ret
        if isinstance(left, int) and isinstance(right, list):
            pair[0].appendleft([left])
            pair[1].appendleft(right)
        if isinstance(left, list) and isinstance(right, int):
            pair[0].appendleft(left)
            pair[1].appendleft([right])
    if len(pair[0]) - len(pair[1]) == 0:
        return None
    else:
        return len(pair[0]) < len(pair[1])

assert 13 == count('test.txt')

assert None == is_pair_valid([[1, 2, 3], [1, 2, 3]])
assert True == is_pair_valid([[1, 2], [1, 2, 3]])
assert False == is_pair_valid([[3], []])

assert True == is_pair_valid([
    [[[],[[7,4,7,7]]],[7],[0,[]],[3]],
    [[0,[[6,5],[2],0,[],[5]]],[[1]],[]]
])

assert False == is_pair_valid([
    [[],[6,[7,5]],[6,6,3]],
    [[],[[2,3],5,6],[7,[]]]
])

assert True == is_pair_valid([
    [[1,[[6,5,2,7,0],4],[2,1],9],[],[[[4,3,1,0,1],9,1,6]],[[[6,7,0],1,5],5,7],[4,3]],
    [[[1,[3],0],[[5],[10],2,[2,1,3,6]],6,[1,[7],1,[],7]],[[],[[10,4,7,7,5],4,[4,5],[3,6,10,9]],[[2,8,5,7],[8,1,0,9]],[[0,6,8],0,7,5,[4,1]],[3]]]
])

assert True == is_pair_valid([
    [],
    [[],[1,5,8,10,8]]
])

print('Answer1 : %s' % count('input.txt'))

assert 140 == count('test.txt', part2=True)
print('Answer2 : %s' % count('input.txt', part2=True))
