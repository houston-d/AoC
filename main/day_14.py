def find_ends(lines):
    left = 500
    right = 500
    max = 0

    for l in lines:
        d = l.split(" -> ")
        for pair in d:
            p = pair.split(',')
            if int(p[0]) < left:
                left = int(p[0])
            elif int(p[0]) > right:
                right = int(p[0])
            if int(p[1]) > max:
                max = int(p[1])

    return left - 1, right + 2, max + 1


def adjust(lines, left):
    adjusted = []
    for l in lines:
        pairs = []
        dir = l.split(" -> ")
        for d in dir:
            temp = d.split(',')
            temp.reverse()
            temp[1] = int(temp[1]) - left
            temp[0] = int(temp[0])
            pairs.append(temp)
        adjusted.append(pairs)

    return adjusted


def construct_walls(matrix, lines, left):
    adj = adjust(lines, left)
    for pairs in adj:
        prev = pairs[0]

        diff = 0
        cur = 0
        for k in range(1, len(pairs)):
            curr_pair = pairs[k]
            diff_i = curr_pair[0] - prev[0]
            diff_j = curr_pair[1] - prev[1]
            if diff_i != 0:
                diff = curr_pair[0] - prev[0]
                cur = 0
            elif diff_j != 0:
                diff = curr_pair[1] - prev[1]
                cur = 1

            matrix[prev[0]][prev[1]] = '#'
            while prev != curr_pair:
                if diff < 0:
                    prev[cur] -= 1
                else:
                    prev[cur] += 1

                matrix[prev[0]][prev[1]] = '#'

            prev = pairs[k]

    return matrix


def drop_sand(matrix, in_):
    set = False

    start = [0, in_]
    while not set:
        if start[0] == len(matrix) - 1:
            return matrix, False
        next_ = [start[0] + 1, start[1]]
        if matrix[next_[0]][next_[1]] == ".":
            start = next_
        elif matrix[next_[0]][next_[1] - 1] == ".":
            next_[1] = next_[1] - 1
            start = next_
        elif matrix[next_[0]][next_[1] + 1] == ".":
            next_[1] = next_[1] + 1
            start = next_
        else:
            matrix[start[0]][start[1]] = "O"
            set = True

    return matrix, set


def drop_sand_2(matrix, in_):
    set = False
    first = True
    s = [0, in_]
    start = [0, in_]
    while not set:
        # if not first and start == s:
        #     return matrix, False
        first = False
        next_ = [start[0] + 1, start[1]]
        if matrix[next_[0]][next_[1]] == ".":
            start = next_
        elif matrix[next_[0]][next_[1] - 1] == ".":
            next_[1] = next_[1] - 1
            start = next_
        elif matrix[next_[0]][next_[1] + 1] == ".":
            next_[1] = next_[1] + 1
            start = next_
        else:
            matrix[start[0]][start[1]] = "O"
            if start == s:
                return matrix, False
            set = True

    return matrix, set


def process_lines_1(lines):
    left, right, max = find_ends(lines)

    print(left, right, max)

    diff = right - left
    matrix = []

    for m in range(max + 1):
        matrix.append(['.'] * diff)

    matrix_ = construct_walls(matrix, lines, left)

    # for i in range(len(matrix_)):
    #     print("".join(matrix_[i]))

    continue_ = True
    count = 0
    while continue_:
        matrix_, continue_ = drop_sand(matrix_, 500 - left)
        count += 1

    # for i in range(len(matrix_)):
    #     print("".join(matrix_[i]))

    print(count - 1)


def process_lines_2(lines):
    left, right, max = find_ends(lines)

    print(left, right, max)

    left -= 150
    right += 90

    diff = right - left
    matrix = []

    for m in range(max + 2):
        matrix.append(['.'] * diff)

    matrix_ = construct_walls(matrix, lines, left)

    for i in range(len(matrix_[0])):
        matrix[len(matrix_) - 1][i] = '#'

    # for i in range(len(matrix_)):
    #     print("".join(matrix_[i]))

    continue_ = True
    count = 0
    while continue_:
        matrix_, continue_ = drop_sand_2(matrix_, 500 - left)
        count += 1

    # for i in range(len(matrix_)):
    #     print("".join(matrix_[i]))

    print(count)


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/14.txt"

    process_lines_1(readfile(file))
    process_lines_2(readfile(file))