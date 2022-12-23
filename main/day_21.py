import time
from copy import deepcopy


def parse_input(lines):
    monkeys = {}
    monkeys_ = []

    for l in lines:
        monk, task = l.split(":")
        ops = task.split(" ")
        if len(ops) == 2:
            monkeys[monk] = int(ops[1])
        else:
            monkeys_.append((monk, ops[1:]))

    return monkeys, monkeys_



def process_lines_1(lines):
    monkeys, monkeys_ = parse_input(lines)

    while len(monkeys) < len(lines):
        for m in monkeys_:
            if m[1][0] in monkeys and m[1][2] in monkeys:
                if m[1][1] == "+":
                    val = monkeys[m[1][0]] + monkeys[m[1][2]]
                elif m[1][1] == "-":
                    val = monkeys[m[1][0]] - monkeys[m[1][2]]
                elif m[1][1] == "*":
                    val = monkeys[m[1][0]] * monkeys[m[1][2]]
                elif m[1][1] == "/":
                    val = monkeys[m[1][0]] // monkeys[m[1][2]]

                monkeys[m[0]] = val
                monkeys_.remove(m)

    print(monkeys["root"])


def part_2(monkeys, monkeys_, length):
    while len(monkeys) < length:
        for m in monkeys_:
            if m[1][0] in monkeys and m[1][2] in monkeys:
                if m[0] == "root":
                    return monkeys[m[1][0]], monkeys[m[1][2]]
                if m[1][1] == "+":
                    val = monkeys[m[1][0]] + monkeys[m[1][2]]
                elif m[1][1] == "-":
                    val = monkeys[m[1][0]] - monkeys[m[1][2]]
                elif m[1][1] == "*":
                    val = monkeys[m[1][0]] * monkeys[m[1][2]]
                elif m[1][1] == "/":
                    val = monkeys[m[1][0]] // monkeys[m[1][2]]

                monkeys[m[0]] = val
                monkeys_.remove(m)

    return monkeys["root"], 1


def process_lines_2(lines):
    monkeys, monkeys_ = parse_input(lines)
    # Due to nature of inputs, this will not work for the test case
    test = 1000000000000
    lower = 1000000000000
    upper = 10000000000000

    while True:
        monkeys["humn"] = test
        f, s = part_2(deepcopy(monkeys), deepcopy(monkeys_), len(lines))

        if f == s:
            monkeys["humn"] = test - 1
            f, s = part_2(deepcopy(monkeys), deepcopy(monkeys_), len(lines))
            if f == s:
                print(test - 1)
            else:
                print(test)
            break
        elif f > s:
            lower = test
            test = (lower + upper) // 2
        elif f < s:
            upper = test
            test = (lower + upper) // 2


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/21.txt"
    start = time.time()
    process_lines_1(readfile(file))
    process_lines_2(readfile(file))
    end = time.time()
    print(end - start)
