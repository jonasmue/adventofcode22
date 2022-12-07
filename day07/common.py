from collections import deque, defaultdict


class FileSystem:

    def __init__(self):
        self.current_dir = deque()
        self.sizes = defaultdict(int)

    @staticmethod
    def get_dir_path(path):
        return "/".join(path)

    def get_all_parent_paths(self):
        return [self.get_dir_path(list(self.current_dir)[:i + 1]) for i in range(len(self.current_dir))]

    def current_dir_path(self):
        return self.get_dir_path(self.current_dir)

    def parse_ls(self):
        pass

    def parse_cd(self, target):
        if target == "/":
            self.current_dir = deque(list(["/"]))
        elif target == "..":
            self.current_dir.pop()
        else:
            self.current_dir.append(target)

    def parse_command(self, command):
        if command[0] == "cd":
            self.parse_cd(command[1])
        elif command[0] == "ls":
            self.parse_ls()

    def add_size(self, int_size):
        for path in self.get_all_parent_paths():
            self.sizes[path] += int_size

    def parse_print(self, print_out):
        if print_out[0] == "dir":
            return
        else:
            self.add_size(int(print_out[0]))

    def parse_instructions(self, instructions):
        for inst in instructions:
            split = inst.split()
            if split[0] == "$":
                self.parse_command(split[1:])
            else:
                self.parse_print(split)


def get_input():
    with open("input.txt") as f:
        return [l.strip() for l in f.readlines()]
