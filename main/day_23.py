import time

def parse_input(lines):
    elves = []

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                elves.append((i, j))

    return elves


def is_free(cur_dir, elf, elves):
    can_move = True
    if cur_dir == 'N':
        if (elf[0] - 1, elf[1] - 1) in elves or (elf[0] - 1, elf[1]) in elves or (elf[0] - 1, elf[1] + 1) in elves:
            can_move = False
    if cur_dir == 'S':
        if (elf[0] + 1, elf[1] - 1) in elves or (elf[0] + 1, elf[1]) in elves or (elf[0] + 1, elf[1] + 1) in elves:
            can_move = False
    if cur_dir == 'W':
        if (elf[0] + 1, elf[1] - 1) in elves or (elf[0], elf[1] - 1) in elves or (elf[0] - 1, elf[1] - 1) in elves:
            can_move = False
    if cur_dir == 'E':
        if (elf[0] + 1, elf[1] + 1) in elves or (elf[0], elf[1] + 1) in elves or (elf[0] - 1, elf[1] + 1) in elves:
            can_move = False

    return can_move

def move(cur_dir, e):
    if cur_dir == 'N':
        return (e[0] - 1, e[1])
    if cur_dir == 'S':
        return (e[0] + 1, e[1])
    if cur_dir == 'W':
        return (e[0], e[1] - 1)
    if cur_dir == 'E':
        return (e[0], e[1] + 1)


def print_map(elves):
    min_i = 9999
    min_j = 9999
    max_i = 0
    max_j = 0

    for e in elves:
        if e[0] > max_i:
            max_i = e[0]
        if e[0] < min_i:
            min_i = e[0]
        if e[1] > max_j:
            max_j = e[1]
        if e[1] < min_j:
            min_j = e[1]
    my_map = []

    for i in range(max_i - min_i + 1):
        my_map.append(['.'] * (max_j + 1 - min_j))

    for e in elves:
        my_map[e[0] - min_i][e[1] - min_j] = "#"

    count = 0
    for m in my_map:
        print("".join(m))
        count += m.count(".")
    print(count)


def process_lines(lines, max_r=10000):
    elves = parse_input(lines)

    dirs = ['N', 'S', 'W', 'E']

    for r in range(max_r):
        if r % 100 == 0:
            print_map(elves)
        # print(len(elves))
        new_loc = []
        has_moved = False
        for e in elves:
            if is_free('N', e, elves) and is_free('S', e, elves) and is_free('W', e, elves) and is_free('E', e, elves):
                new_loc.append(e)
                continue
            has_moved = True
            can_move = False
            for i in range(4):
                cur_dir = dirs[(r + i) % 4]
                if is_free(cur_dir, e, elves):
                    new_loc.append(move(cur_dir, e))
                    can_move = True
                    break
            if not can_move:
                new_loc.append(e)
        new_elves = []
        for j in range(len(new_loc)):
            if new_loc.count(new_loc[j]) == 1:
                new_elves.append(new_loc[j])
            else:
                new_elves.append(elves[j])
        elves = new_elves

        if not has_moved:
            print(r + 1)
            break

    print_map(elves)


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/23.txt"
    start = time.time()
    process_lines(readfile(file), max_r=10)
    process_lines(readfile(file))
    end = time.time()
    print(end - start)
