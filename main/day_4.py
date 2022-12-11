def split(s):
    s1, s2 = s.split(",")
    s1_1, s1_2 = s1.split("-")
    s2_1, s2_2 = s2.split("-")
    return s1_1, s1_2, s2_1, s2_2


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
    t = ["2-4,6-8",
         "2-3,4-5",
         "5-7,7-9",
         "2-8,3-7",
         "6-6,4-6",
         "2-6,4-8"]

    elves = []
    groups = []
    sum_ = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for l in range(0, len(lines)):
        s = lines[l]
        a, b, c, d = split(s)
        print(a, b, c, d)
        if int(c) <= int(a) <= int(d):
            sum_ += 1
            print("yes")
        elif int(c) <= int(b) <= int(d):
            sum_ += 1
        elif int(a) <= int(c) <= int(b):
            sum_ += 1
        elif int(a) <= int(d) <= int(b):
            sum_ += 1

        # print(split(s))
    print(sum_)


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/4.txt"
    process_lines(readfile(file))
