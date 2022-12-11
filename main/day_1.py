
def split_lines(lines):
    print(len(lines))
    elves = []
    sum_ = 0
    for l in range(0, len(lines)):
        if lines[l] == "":
            elves.append(sum_)
            sum_ = 0
        else:
            sum_ = sum_ + int(lines[l])

    s = sorted(elves, key=int, reverse=True)
    print(s)
    print(s[0] + s[1] + s[2])
    print(max(elves))


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/1.txt"
    split_lines(readfile(file))
