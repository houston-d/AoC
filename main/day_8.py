def new_lines():

    lines = ["30373", "25512", "65332", "33549", "35390"]
    # lines = [
    #     [3, 0, 3, 7, 3],
    #     [2, 5, 5, 1, 2],
    #     [6, 5, 3, 3, 2],
    #     [3, 3, 5, 4, 9],
    #     [3, 5, 3, 9, 0]]
    return lines


def convert_to_matrix(lines):
    matrix = []
    for l in lines:
        matrix.append(list(l))
    return matrix


def visible_left(matrix, i, j):
    height = matrix[i][j]
    for k in range(j - 1, -1, -1):
        if matrix[i][k] >= height:
            return False
    return True


def visible_right(matrix, i, j):
    height = matrix[i][j]
    for k in range(j + 1, len(matrix[0])):
        if matrix[i][k] >= height:
            return False
    return True


def visible_up(matrix, i, j):
    height = matrix[i][j]
    for k in range(i - 1, -1, -1):
        if matrix[k][j] >= height:
            return False
    return True


def visible_down(matrix, i, j):
    height = matrix[i][j]
    for k in range(i + 1, len(matrix)):
        if matrix[k][j] >= height:
            return False
    return True


def count_up(matrix, i, j):
    count = 0
    height = matrix[i][j]
    for k in range(i - 1, -1, -1):
        count += 1
        if matrix[k][j] >= height:
            return count

    return count


def count_down(matrix, i, j):
    count = 0
    height = matrix[i][j]
    for k in range(i + 1, len(matrix)):
        count += 1
        if matrix[k][j] >= height:
            return count

    return count


def count_left(matrix, i, j):
    count = 0
    height = matrix[i][j]
    for k in range(j - 1, -1, -1):
        count += 1
        if matrix[i][k] >= height:
            return count

    return count


def count_right(matrix, i, j):
    count = 0
    height = matrix[i][j]
    for k in range(j + 1, len(matrix[0])):
        count += 1
        if matrix[i][k] >= height:
            return count

    return count


def process_lines(lines):
    # lines = new_lines()
    
    matrix = convert_to_matrix(lines)

    sum_ = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if visible_down(matrix, i, j) or visible_up(matrix, i, j) or visible_left(matrix, i, j) or visible_right(matrix, i, j):
                sum_ += 1

    sum_ += 2 * (len(matrix) - 1)
    sum_ += 2 * (len(matrix[0]) - 1)
    print(sum_)


    best = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            v = count_up(matrix, i, j) * count_down(matrix, i, j) * count_left(matrix, i, j) * count_right(matrix, i, j)
            # print(i, j, v)
            if v > best:
                best = v

    print(best)

def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/8.txt"
    process_lines(readfile(file))
