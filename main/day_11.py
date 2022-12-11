class Monkey:
    def __init__(self, num, start, test, true, false):
        self.num = num
        self.current = start
        self.test = test
        self.true = true
        self.false = false
        self.count = 0
        self.test_modulo = 23 * 19 * 13 * 17
        self.modulo = 13 * 19 * 5 * 2 * 17 * 11 * 7 * 3

    def throw(self):
        monkeys = []
        for i in self.current:
            level = self.op(i) % self.modulo
            if level % self.test == 0:
                monkeys.append((level, self.true))
            else:
                monkeys.append((level, self.false))

        self.count += len(self.current)
        return monkeys

    def add(self, val):
        self.current.append(val)

    def clear(self):
        self.current = []

    def test_op(self, old):
        if self.num == 0:
            return old * 19
        if self.num == 1:
            return old + 6
        if self.num == 2:
            return old * old
        if self.num == 3:
            return old + 3

    def op(self, old):
        if self.num == 0:
            return old * 7
        if self.num == 1:
            return old + 7
        if self.num == 2:
            return old * 3
        if self.num == 3:
            return old + 3
        if self.num == 4:
            return old * old
        if self.num == 5:
            return old + 8
        if self.num == 6:
            return old + 2
        if self.num == 7:
            return old + 4

def process_lines(lines):
    print(lines)
    monkeys = []
    split = []
    curr = []
    for i in range(len(lines)):
        l = lines[i]
        if i % 5 == 0:
            curr.append(l.split(","))
        elif i % 5 != 4:
            curr.append(int(l.split(":")[1]))
        elif i % 5 == 4:

            m = Monkey(len(monkeys), list(map(int, curr[0])), curr[1], curr[2], curr[3])
            monkeys.append(m)
            print(curr)
            curr = []

    # for m in monkeys:
    #     print(m.num, m.op(5))

    rounds = [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

    for j in range(10000):
        if j in rounds:
            print("round", j)
            for m in monkeys:
                print(m.num, m.count)

        for m in monkeys:
            to_throw = m.throw()

            for val, monkey in to_throw:
                monkeys[monkey].add(val)
            m.clear()

    thrown = []
    for m in monkeys:
        thrown.append(m.count)

    thrown = sorted(thrown, reverse=True)
    print(thrown)

    print(thrown[0] * thrown[1])

def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/11.txt"
    process_lines(readfile(file))
