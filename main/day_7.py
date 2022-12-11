def new_lines():
    lines = ["$ cd /",
             "$ ls",
             "dir a",
             "14848514 b.txt",
             "8504156 c.dat",
             "dir d",
             "$ cd a",
             "$ ls",
             "dir e",
             "29116 f",
             "2557 g",
             "62596 h.lst",
             "$ cd e",
             "$ ls",
             "584 i",
             "$ cd ..",
             "$ cd ..",
             "$ cd d",
             "$ ls",
             "4060174 j",
             "8033020 d.log",
             "5626152 d.ext",
             "7214296 k"]
    return lines


def print_tree(root, marker_str="+- ", level_markers=[]):
    empty_str = " "*len(marker_str)
    connection_str = "|" + empty_str[:-1]
    level = len(level_markers)
    mapper = lambda draw: connection_str if draw else empty_str
    markers = "".join(map(mapper, level_markers[:-1]))
    markers += marker_str if level > 0 else ""
    if len(root.get_children()) == 0:
        type_ = "file"
    else:
        type_ = "dir"
    s = f"({type_}, size={root.size})"
    if len(root.get_children()) != 0:
        print(f"{markers}{root.name}", s)
    else:
        print(f"{markers}{root.name}")
    for i, child in enumerate(root.children):
        isLast = i == len(root.children) - 1
        print_tree(child, marker_str, [*level_markers, not isLast])


def sum_dirs(root):
    if len(root.get_children()) == 0:
        return int(root.get_size())
    total = 0
    for child in root.get_children():
        val = sum_dirs(child)
        total += val
    root.set_size(total)
    return total


class Item:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.size = 0
        self.parent = ""

    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

    def add_child(self, item):
        self.children.append(item)

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_parent(self, p):
        self.parent = p

    def get_parent(self):
        return self.parent

def create_tree(lines):
    root = Item("/")

    current = root

    for i in range(len(lines)):
        l = lines[i]
        if "$" not in l:
            split = l.split(" ")
            new_child = Item(split[1])
            new_child.set_parent(current)
            current.add_child(new_child)
            if "dir" not in l:
                new_child.set_size(split[0])
        elif l == "$ cd /":
            current = root
        elif l == "$ cd ..":
            current = current.get_parent()
        elif "$ cd" in l:
            dol, com, name = l.split(" ")
            c_ = current.get_children()
            for c in c_:
                if c.get_name() == name:
                    current = c

    return root

def to_delete(root, free):

    if len(root.get_children()) == 0:
        return 999999999999999999999
    cur = 999999999999
    if root.get_size() > free:
        cur = root.get_size()
    for child in root.get_children():

        s = to_delete(child, free)
        if free < s < cur:
            cur = s
        print(child.get_size())
    return cur


def process_lines(lines):

    # lines = new_lines()
    root = create_tree(lines)

    sum_dirs(root)
    print_tree(root)

    total = 70000000
    free = total - root.get_size()
    need = 30000000 - free
    print("free space", need)

    print(to_delete(root, need))


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/7.txt"
    process_lines(readfile(file))
