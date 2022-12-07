
class FileDescriptor:

    def __init__(self, name: str, size: int = 0) -> None:
        self.name = name
        self.size = size
        self.parent_fd = None
        self.children = []

    def add_child(self, fd_name, size) -> None:
        new_fd = FileDescriptor(fd_name, size)
        new_fd.parent_fd = self
        self.children.append(new_fd) 

    def get_child(self, name: str):
        for child in self.children:
            if child.name == name:
                return child
        else:
            raise Exception(f"can't find file descriptor from {name}")

    def __str__(self):
        # Returns a JSON-compatible string
        return '{"name": "%s", ' % self.name + '"size": "%s", '% self.size + \
               '"children": [' + \
                ', '.join([str(child) for child in self.children]) + \
               ']}'

def create_filesystem_from_file(file: str) -> FileDescriptor:
    with open(file, 'r') as fs:
        lines = fs.readlines()
    fs = None
    current_fd = None
    for line in lines:
        line = line.rstrip('\n')
        if line.startswith('$ '):
            command = line[2:]
            if command == 'cd /':
                # make it simple, just initialize the filesystem
                fs = FileDescriptor('/')
                current_fd = fs
            elif command.startswith('cd '):
                target_dir = command[3:]
                if target_dir == '..':
                    current_fd = current_fd.parent_fd
                else:
                    current_fd = current_fd.get_child(target_dir)
            elif command == 'ls':
                pass
        else:
            if line.startswith('dir '):
                size = 0
                fd_name = line[4:]
            else:
                size, fd_name = line.split(' ')
                size = int(size)
            current_fd.add_child(fd_name, size)
    return fs


DIRS = []
# Heh, a decorator wasn't really needed but meh ;-)
def report_size(func):
    def wrapped(fs):
        size = func(fs)
        DIRS.append((fs, size))
        return size
    return wrapped


@report_size
def size_of_dir(fs: FileDescriptor) -> int:
    total_size = 0
    for child in fs.children:
        total_size += child.size
        if child.size == 0:
            total_size += size_of_dir(child)
    return total_size


def answer1(file):
    global DIRS
    DIRS = []
    filesystem = create_filesystem_from_file(file)
    size_of_dir(filesystem)
    # let's just sum the size for the non-larger dirs
    return sum([dir[1] for dir in DIRS if dir[1] < 100000])


assert 95437 == answer1("test.txt")
print("Answer1: %s " % answer1('input.txt'))


# Part 2

def answer2(file):
    global DIRS
    DIRS = []
    filesystem = create_filesystem_from_file(file)
    total_size = size_of_dir(filesystem)
    space_left = 70000000 - total_size
    # We need to consider how much we need to delete
    space_missing = 30000000 - space_left
    dir_sizes = [dir[1] for dir in DIRS]
    # We take the closest number above the missing space
    return min(filter(lambda x: x > space_missing, dir_sizes))


assert 24933642 == answer2("test.txt")
print("Answer2: %s " % answer2('input.txt'))
