def process_lines(lines):
    # lines = new_lines()


    x = 1

    cycle = [x]

    for l in lines:
        if "noop" in l:
            cycle.append(x)
        elif "addx" in l:
            op, v = l.split(" ")
            cycle.append(x)
            x += int(v)
            cycle.append(x)

    print(len(cycle))

    input = []
    cur = ""

    for i in range(0, len(cycle)):
        if i % 40 == 0:
            input.append(cur)
            cur = ""

        val = [cycle[i] - 1, cycle[i], cycle[i] + 1]
        cur_len = len(cur)
        if len(cur) in val:
            cur = cur + "#"
        else:
            cur = cur + "."

    for m in input:
        print(m)
    # print(cycle[19])
    # print(cycle[59])
    # print(cycle[99])
    # print(cycle[139])
    # print(cycle[179])
    # print(cycle[219])
    # print()
    # print(cycle[19] * 20 + cycle[59] * 60 + cycle[99] * 100 + cycle[139] * 140 + cycle[179] * 180 + cycle[219] * 220)



def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/10.txt"
    process_lines(readfile(file))


PCPBKAPJ