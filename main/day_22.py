import time
import re


def parse_input(lines):
    map_lines = []
    path = lines[len(lines) - 1]

    max_len = 0

    for i in range(len(lines) - 2):
        map_lines.append(lines[i])
        if len(lines[i]) > max_len:
            max_len = len(lines[i])

    map_matrix = []
    for m in map_lines:
        new_line = list((m.replace(" ", "@")))

        new_line.extend(list("@" * (max_len - len(m))))
        map_matrix.append(new_line)

    return map_matrix, (re.split(r'([RL])', path)), map_matrix[0].index(".")


def process_lines_1(lines):
    map_matrix, path, start_point = parse_input(lines)

    pos = [0, start_point]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    current_dir = 0

    for action in path:
        if action == 'R':
            current_dir = (current_dir + 1) % 4
        elif action == 'L':
            current_dir = (current_dir - 1) % 4
        else:
            for _ in range(int(action)):
                new_pos_0 = (pos[0] + dirs[current_dir][0]) % len(map_matrix)
                new_pos_1 = (pos[1] + dirs[current_dir][1]) % len(map_matrix[0])

                if map_matrix[new_pos_0][new_pos_1] == '.':
                    pos[0] = new_pos_0
                    pos[1] = new_pos_1
                elif map_matrix[new_pos_0][new_pos_1] == '#':
                    break
                elif map_matrix[new_pos_0][new_pos_1] == '@':
                    temp_0 = new_pos_0
                    temp_1 = new_pos_1
                    move = True
                    while map_matrix[temp_0][temp_1] != '.':
                        temp_0 = (temp_0 + dirs[current_dir][0]) % len(map_matrix)
                        temp_1 = (temp_1 + dirs[current_dir][1]) % len(map_matrix[0])

                        if map_matrix[temp_0][temp_1] == '#':
                            move = False
                            break
                    if move:
                        pos[0] = temp_0
                        pos[1] = temp_1
    print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + current_dir)


def adjust_pos(current_dir, new_dir, pos, dim):
    if current_dir == 0 and new_dir == 0:
        pos[1] = 0
    if current_dir == 1 and new_dir == 1:
        pos[0] = 0
    if current_dir == 2 and new_dir == 2:
        pos[1] = dim
    if current_dir == 3 and new_dir == 3:
        pos[0] = dim
    if current_dir == 0 and new_dir == 2:
        pos[0] = dim - pos[0]
    if current_dir == 0 and new_dir == 3:
        temp = pos[1]
        pos[1] = pos[0]
        pos[0] = temp
    if current_dir == 1 and new_dir == 2:
        temp = pos[1]
        pos[1] = pos[0]
        pos[0] = temp
    if current_dir == 2 and new_dir == 0:
        pos[0] = dim - pos[0]
    if current_dir == 2 and new_dir == 1:
        temp = pos[1]
        pos[1] = pos[0]
        pos[0] = temp
    if current_dir == 3 and new_dir == 0:
        temp = pos[1]
        pos[1] = pos[0]
        pos[0] = temp

    return pos


def get_new_pos(pos, current_dir):
    dim = 50
    f = [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (3, 0)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    move_face = {
        (f[0], 0): (f[1], 0), (f[0], 1): (f[2], 1), (f[0], 2): (f[3], 0), (f[0], 3): (f[5], 0),
        (f[1], 0): (f[4], 2), (f[1], 1): (f[2], 2), (f[1], 2): (f[0], 2), (f[1], 3): (f[5], 3),
        (f[2], 0): (f[1], 3), (f[2], 1): (f[4], 1), (f[2], 2): (f[3], 1), (f[2], 3): (f[0], 3),
        (f[3], 0): (f[4], 0), (f[3], 1): (f[5], 1), (f[3], 2): (f[0], 0), (f[3], 3): (f[2], 0),
        (f[4], 0): (f[1], 2), (f[4], 1): (f[5], 2), (f[4], 2): (f[3], 2), (f[4], 3): (f[2], 3),
        (f[5], 0): (f[4], 3), (f[5], 1): (f[1], 1), (f[5], 2): (f[0], 1), (f[5], 3): (f[3], 3),
    }

    temp_0 = pos[0]
    temp_1 = pos[1]

    cube_0 = 0
    cube_1 = 0

    while temp_0 >= dim:
        temp_0 -= dim
        cube_0 += 1
    while temp_1 >= dim:
        temp_1 -= dim
        cube_1 += 1

    if temp_0 == dim - 1 and current_dir == 1:
        new_face, new_dir = move_face[((cube_0, cube_1), current_dir)]
        new_pos = adjust_pos(current_dir, new_dir, [temp_0, temp_1], dim - 1)
        new_pos[0] += dim * new_face[0]
        new_pos[1] += dim * new_face[1]
        return new_pos, new_dir
    if temp_0 == 0 and current_dir == 3:
        new_face, new_dir = move_face[((cube_0, cube_1), current_dir)]
        new_pos = adjust_pos(current_dir, new_dir, [temp_0, temp_1], dim - 1)
        new_pos[0] += dim * new_face[0]
        new_pos[1] += dim * new_face[1]
        return new_pos, new_dir
    if temp_1 == dim - 1 and current_dir == 0:
        new_face, new_dir = move_face[((cube_0, cube_1), current_dir)]
        new_pos = adjust_pos(current_dir, new_dir, [temp_0, temp_1], dim - 1)
        new_pos[0] += dim * new_face[0]
        new_pos[1] += dim * new_face[1]
        return new_pos, new_dir
    if temp_1 == 0 and current_dir == 2:
        new_face, new_dir = move_face[((cube_0, cube_1), current_dir)]
        new_pos = adjust_pos(current_dir, new_dir, [temp_0, temp_1], dim - 1)
        new_pos[0] += dim * new_face[0]
        new_pos[1] += dim * new_face[1]
        return new_pos, new_dir

    new_pos = [pos[0] + dirs[current_dir][0], pos[1] + dirs[current_dir][1]]
    return new_pos, current_dir


def process_lines_2(lines):
    map_matrix, path, start_point = parse_input(lines)

    pos = [0, start_point]

    current_dir = 0

    for action in path:
        if action == 'R':
            current_dir = (current_dir + 1) % 4
        elif action == 'L':
            current_dir = (current_dir - 1) % 4
        else:
            for _ in range(int(action)):
                new_pos, new_dir = get_new_pos(pos, current_dir)

                if map_matrix[new_pos[0]][new_pos[1]] == '.':
                    pos = new_pos
                    current_dir = new_dir
                elif map_matrix[new_pos[0]][new_pos[1]] == '#':
                    break
                elif map_matrix[new_pos[0]][new_pos[1]] == '@':
                    return 0

    print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + current_dir)



def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/22.txt"
    start = time.time()
    process_lines_1(readfile(file))
    process_lines_2(readfile(file))
    end = time.time()
    print(end - start)
