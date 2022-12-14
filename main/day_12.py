from collections import defaultdict, deque

def convert_to_matrix(lines):
    matrix = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for l in lines:
        matrix.append(list(l))
    #
    # for r in matrix:
    #     print(r)

    start = []
    end = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                start = (i, j)
                matrix[i][j] = 0
            elif matrix[i][j] == "E":
                end = (i, j)
                matrix[i][j] = 25
            else:
                matrix[i][j] = alphabet.index(matrix[i][j])
    return matrix, start, end

def find(matrix, s, e, deq):
    set_ = set()

    path_length = 0

    while deq:
        (i, j), l = deq.popleft()
        if (i, j) not in set_:
            if i == e[0] and j == e[1]:
                path_length = l
            set_.add((i, j))
            for change_i, change_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i = i + change_i
                new_j = j + change_j
                if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and matrix[new_i][new_j] <= (
                        matrix[i][j] + 1):
                    deq.append(((new_i, new_j), l + 1))

    return path_length


def process_lines_1(lines):
    matrix, s, e = convert_to_matrix(lines)

    deq = deque()

    deq.append(((s[0], s[1]), 0))

    print(find(matrix, s, e, deq))


def process_lines_2(lines):
    matrix, s, e = convert_to_matrix(lines)
    deq = deque()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                deq.append(((i, j), 0))

    print(find(matrix, s, e, deq))



def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/12.txt"
    process_lines_1(readfile(file))
    process_lines_2(readfile(file))
