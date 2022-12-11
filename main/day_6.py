def split(s):
    print(s)
    s1, s2, s3, s4, s5, s6 = s.split(" ")
    print(int(s2), int(s4), int(s6))
    return int(s2), int(s4), int(s6)


def compare(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return False
    return True

def process_lines(lines):
    lines = lines[0]
    start = lines[:13]
    print(start)

    for l in range(13, len(lines)):
        c = lines[l]
        start = start + c
        b = compare(start)
        if compare(start):
            print(start, c, l + 1)
            break
        start = start[1:]


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/6.txt"
    process_lines(readfile(file))
