def new_lines():
    # lines = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
    lines = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]
    return lines


def case(d):
    if d == "U":
        return V(-1, 0)
    if d == "R":
        return V(0, 1)
    if d == "D":
        return V(1, 0)
    if d == "L":
        return V(0, -1)

class Seen:
    def __init__(self):
        self.seen = []

    def __contains__(self, item):
        for v in self.seen:
            if v.x == item.x and v.y == item.y:
                return True
        return False

    def add(self, v):
        if not self.__contains__(v):
            self.seen.append(v)

    def len(self):
        return len(self.seen)


class V:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        return V(self.x + vector.x, self.y + vector.y)

    def sub(self, vector):
        return V(self.x - vector.x, self.y - vector.y)


def move_tail(head, tail):
    # print("prev", head.x, head.y)
    # print("cur", tail.x, tail.y)
    new_diff = tail.sub(head)
    x_ = new_diff.x
    y_ = new_diff.y
    # print("new_diff", new_diff.x, new_diff.y)
    temp = V(x_, y_)
    if x_ == 2 and y_ == 2:
        temp = V(1, 1)
    elif x_ == 2 and y_ == -2:
        temp = V(1, -1)
    elif x_ == -2 and y_ == 2:
        temp = V(-1, 1)
    elif x_ == -2 and y_ == -2:
        temp = V(-1, -1)
    elif x_ == 2:
        temp = V(1, 0)
    elif x_ == -2:
        temp = V(-1, 0)
    elif y_ == 2:
        temp = V(0, 1)
    elif y_ == -2:
        temp = V(0, -1)

    # print("change", temp.x, temp.y)

    return head.add(temp)


def print_(rope):
    matrix = []
    for _ in range(25):
        t = ["."] * 30
        matrix.append(t)

    start = V(10, 16)

    for i in range(len(rope)):
        v = rope[i]
        pos = start.add(v)
        if matrix[pos.x][pos.y] == ".":
            if i == 0:
                matrix[pos.x][pos.y] = "H"
            else:
                matrix[pos.x][pos.y] = str(i)

    print()
    print()
    for l in matrix:
        print(''.join(l))


def process_lines(lines):


    # lines = new_lines()

    seen = Seen()
    rope = [V(0, 0), V(0, 0), V(0, 0), V(0, 0), V(0, 0), V(0, 0), V(0, 0), V(0, 0), V(0, 0), V(0, 0)]

    print_(rope)
    seen.add(rope[9])

    for l in lines:
        direction, times = l.split(" ")
        for _ in range(int(times)):
            rope[0] = rope[0].add(case(direction))
            prev = rope[0]
            for i in range(1, len(rope)):
                # print(i)
                rope[i] = move_tail(prev, rope[i])
                prev = rope[i]
            seen.add(rope[9])
        # print_(rope)



    print(seen.len())


# . . . .
# . . T .
# . . . .
# . H . .
# . . . .



def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/9.txt"
    process_lines(readfile(file))
