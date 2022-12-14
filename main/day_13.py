class Stack:
    def __init__(self):
        self.stack = []

    def push(self, c):
        self.stack.append(c)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]


def build_stack(str):
    stack = Stack()
    for c in str.split(","):
        if c.isnumeric():
            c = int(c)
        if c == "]":
            items = []
            cur = stack.pop()
            while cur != "[":
                items.append(cur)
                cur = stack.pop()
            items.reverse()
            stack.push(items)

        else:
            stack.push(c)

    return stack.stack[0]


def compare_list_list(a, b):
    max_ = len(a) > len(b)
    same = len(a) == len(b)
    for i in range(min(len(a), len(b))):
        left = a[i]
        right = b[i]

        if left == '' and right != '':
            return 1
        if right == '' and left != '':
            return 0

        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return 1
            if left > right:
                return 0
        if isinstance(left, list) and isinstance(right, list):
            comp = compare_list_list(left, right)
            if comp >= 0:
                return comp

        if isinstance(left, list) and isinstance(right, int):
            comp = compare_list_list(left, [right])
            if comp >= 0:
                return comp

        if isinstance(left, int) and isinstance(right, list):
            comp = compare_list_list([left], right)
            if comp >= 0:
                return comp

    if same:
        return -1
    if not max_:
        return 1
    else:
        return 0


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if compare_list_list(arr[j], arr[j + 1]) == 0:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


def process_lines_1(lines):
    packet_str = []
    packet = []
    for i in range(len(lines)):
        # print(i, lines[i])
        if i % 3 == 0:
            packet.append(lines[i])
        if i % 3 == 1:
            packet.append(lines[i])
        if i % 3 == 2:
            packet_str.append(packet)
            packet = []

    count = 0

    for i in range(len(packet_str)):
        first = build_stack(packet_str[i][0])
        second = build_stack(packet_str[i][1])

        print(first)
        print(second)

        c = compare_list_list(first, second)
        print(c)
        if c == 1:
            count += i + 1

    print(count)


def process_lines_2(lines):
    packet = []

    packet.append(build_stack("[,[,2,],]"))
    packet.append(build_stack("[,[,6,],]"))

    for l in lines:
        if len(l) > 0:
            packet.append(build_stack(l))

    bubbleSort(packet)

    for p in packet:
        print(p)

    product = 1

    for i in range(len(packet)):
        if compare_list_list(packet[i], [[6]]) == -1 or compare_list_list(packet[i], [[2]]) == -1:
            print(i + 1)
            product *= (i + 1)

    print(product)


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/13.txt"

    process_lines_1(readfile(file))
    process_lines_2(readfile(file))
