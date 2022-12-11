
def point_use(c):
    if c == "X":
        return 1
    if c == "Y":
        return 2
    if c == "Z":
        return 3

def point_win(a, b):
    if a == "A": # Rock
        if b == "X": # Scissors/lose 3 + 0
            return 3
        if b == "Y": # Rocke/draw 1 + 3
            return 4
        if b == "Z": # paper/win 2 + 6
            return 8
    if a == "B": # paper
        if b == "X": # rock/lose 1 + 0
            return 1
        if b == "Y": # paper/draw 2 + 3
            return 5
        if b == "Z": # scissors/win 3 + 6
            return 9
    if a == "C": # scissors
        if b == "X": # paper/lose 2 + 0
            return 2
        if b == "Y": # scissors/draw 3 + 3
            return 6
        if b == "Z": # rock/win 1 + 6
            return 7

def split_lines(lines):
    print(len(lines))
    # elves = []
    sum_ = 0
    for l in range(0, len(lines)):
        data = lines[l].split(" ")
        print(data[0])
        print(data[1])
        # sum_ += point_use(data[1])
        sum_ += point_win(data[0], data[1])

    print(sum_)


    # s = sorted(elves, key=int, reverse=True)
    # print(s)
    # print(s[0] + s[1] + s[2])
    # print(max(elves))


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/2.txt"
    split_lines(readfile(file))
