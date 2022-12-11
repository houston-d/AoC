
def compare(s1, s2, s3):
    common = []
    for c2 in s2:
        if c2 in s1:
            common.append(c2)
    for c3 in common:
        if c3 in s3:
            return c3



def process_lines(lines):
    print(len(lines))
    elves = []
    groups = []
    sum_ = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for l in range(0, len(lines)):
        s = lines[l]
        elves.append(s)
        if l % 3 == 2:
            groups.append(elves)
            elves = []

    for g in groups:
        c = compare(g[0], g[1], g[2])
        print(c)
        sum_ += alphabet.index(c) + 1

    print(groups)
    print(sum_)

def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/3.txt"
    process_lines(readfile(file))
