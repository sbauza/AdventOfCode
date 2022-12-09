from dataclasses import dataclass

POSITIONS = set()


@dataclass
class Position:
    x: int
    y: int

    def far_from(self, pos) -> bool:
        if abs(self.x - pos.x) > 1 or abs(self.y - pos.y) > 1:
            return True
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def make_adjacent(self, pos):
        if self.x == pos.x:
            # we only need to shorten the rope by the half-distance on y
            self.y += int((pos.y - self.y) / 2)
        elif self.y == pos.y:
            # we only need to shorten the rope by the half-distance on x
            self.x += int((pos.x - self.x) / 2)
        else:
            # we need to jump on a diagonal
            diff_y = pos.y - self.y
            diff_x = pos.x - self.x
            if abs(diff_x) == 2:
                self.x += int(diff_x / 2)
            else:
                self.x += diff_x
            if abs(diff_y) == 2:
                self.y += int(diff_y / 2)
            else:
                self.y += diff_y

    def record_position(self):
        global POSITIONS
        # Given the object is mutable, we need to copy it.
        POSITIONS.add(Position(self.x, self.y))


@dataclass(init=False)
class Instruction:
    x: int
    y: int
    def __init__(self, direction: str, steps: int):
        if direction == 'U':
            self.x = 0
            self.y = steps
        elif direction == 'D':
            self.x = 0
            self.y = steps * -1
        elif direction == 'R':
            self.x = steps
            self.y = 0
        elif direction == 'L':
            self.x = steps * -1        
            self.y = 0

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    def compute(self, knots):
        action = self.x if self.x != 0 else self.y
        for _step in range(abs(action)):
            bit = int(action/abs(action)) # we move either by 1 or -1
            if self.x != 0:
                move = (bit, 0)
            else:
                move = (0, bit)
            knots[0].move(*move)
            for idx, knot in enumerate(knots[1:], 1):
                previous_knot = knots[idx-1]
                if knot.far_from(previous_knot):
                    knot.make_adjacent(previous_knot)
            knots[-1].record_position()
        return knots


assert "x: 0, y: 1" == str(Instruction('U', 1))


def get_instructions(file):
    with open(file, 'r') as fs:
        lines = fs.readlines()

    instructions = []
    for line in lines:
        line = line.rstrip('\n')
        dir, steps = line.split(" ")
        instructions.append(Instruction(dir, int(steps)))
    return instructions


def run_1(instructions):
    head = Position(0, 0)
    tail = Position(0, 0)
    tail.record_position()
    for instruction in instructions:
        instruction.compute([head, tail])

def run_2(instructions):
    knots = []
    for i in range(10):
        knots.append(Position(0, 0))
    knots[-1].record_position()
    for instruction in instructions:
        knots = instruction.compute(knots)

test_instructions = get_instructions('test.txt')
run_1(test_instructions)
assert 13 == len(POSITIONS)

POSITIONS = set()
run_2(test_instructions)
assert 1 == len(POSITIONS)

test_instructions = get_instructions('test2.txt')

POSITIONS = set()
run_2(test_instructions)
assert 36 == len(POSITIONS)

input_instructions = get_instructions('input.txt')

POSITIONS = set()
run_1(input_instructions)
print("Answer 1: %s" % len(POSITIONS))

POSITIONS = set()
run_2(input_instructions)
print("Answer 2: %s" % len(POSITIONS))
