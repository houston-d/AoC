def split(s):
    print(s)
    s1, s2, s3, s4, s5, s6 = s.split(" ")
    print(int(s2), int(s4), int(s6))
    return int(s2), int(s4), int(s6)


def compare(s1, s2, s3):
    common = []
    for c2 in s2:
        if c2 in s1:
            common.append(c2)
    for c3 in common:
        if c3 in s3:
            return c3


def build_stack():
    full = []
    full.append([])
    full.append(["T", "P", "Z", "C", "S", "L", "Q", "N"])
    full.append(["L", "P", "T", "V", "H", "C", "G"])
    full.append(["D", "C", "Z", "F"])
    full.append(["G", "W", "T", "D", "L", "M", "V", "C"])
    full.append(["P", "W", "C"])
    full.append(["P", "F", "J", "D", "C", "T", "S", "Z"])
    full.append(["V", "W", "G", "B", "D"])
    full.append(["N", "J", "S", "Q", "H", "W"])
    full.append(["R", "C", "Q", "F", "S", "L", "V"])
    # full.append(["Z", "N"])
    # full.append(["M", "C", "D"])
    # full.append(["P"])
    return full


def process_lines(lines):
    # input = ["move 1 from 2 to 1",
    #          "move 3 from 1 to 3",
    #          "move 2 from 2 to 1",
    #          "move 1 from 1 to 2"]
    stack = build_stack()

    for l in lines:
        a, b, c = split(l)

        temp = []

        for i in range(a):
            temp.append(stack[b].pop())

        for i in range(a):
            stack[c].append(temp.pop())

    print(stack)

    for i in range(1, len(stack)):
        print(stack[i].pop())

# CHQCCZDWV
# SVFDLGLWV
# DCVTCVPCL

def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/5.txt"
    process_lines(readfile(file))
