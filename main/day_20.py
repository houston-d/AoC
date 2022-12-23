import time
import uuid


class Node:
    def __init__(self, value, prev=None, nxt=None):
        self.v = value
        self.prev = prev
        self.nxt = nxt
        self.id = uuid.uuid4()

    def __eq__(self, other):
        return self.id == other.id

    def insert_after(self, n):
        n.nxt = self.nxt
        self.nxt.prev = n
        self.nxt = n
        n.prev = self

    def insert_before(self, n):
        n.prev = self.prev
        self.prev.nxt = n
        self.prev = n
        n.nxt = self

    def remove(self):
        self.nxt.prev = self.prev
        self.prev.nxt = self.nxt
        self.nxt = None
        self.prev = None


def parse_input_1(lines):
    new_list = []
    for l in lines:
        new_list.append(int(l))

    head_node = Node(new_list[0])
    current_node = head_node
    for i in range(1, len(new_list)):
        temp_node = Node(new_list[i], prev=current_node)
        current_node.nxt = temp_node
        current_node = temp_node

    current_node.nxt = head_node
    head_node.prev = current_node
    return new_list, head_node


def parse_input_2(lines):
    new_list = []
    for l in lines:
        new_list.append(int(l))

    key = 811589153
    new_list = [line * key for line in new_list]

    head_node = Node(new_list[0])
    current_node = head_node
    for i in range(1, len(new_list)):
        temp_node = Node(new_list[i], prev=current_node)
        current_node.nxt = temp_node
        current_node = temp_node

    current_node.nxt = head_node
    head_node.prev = current_node
    return new_list, head_node


def print_list(node: Node):
    new_list = [node.v]

    n = node.nxt

    while n.id != node.id:
        new_list.append(n.v)
        n = n.nxt

    print(new_list)


def get_index(head: Node, i):

    n = head
    while n.v != 0:
        n = n.nxt
    for _ in range(i):
        n = n.nxt
    return n

def create_new(n:Node):
    new_node = Node(n.v)
    new_node.prev = n.prev
    new_node.nxt = n.nxt
    return new_node


def process_lines_1(lines):
    lines, head_node = parse_input_1(lines)

    print(len(lines))

    seen = []
    current_node = head_node
    print_list(head_node)

    count = 0
    while len(seen) < len(lines):
        count += 1
        if count % 100 == 0:
            print(count, len(seen))
        # print_list(head_node)

        if current_node.id in seen:
            current_node = current_node.nxt
            continue
        seen.append(current_node.id)
        if current_node.v == 0:
            # if current_node == head_node:
            #     head_node = current_node.nxt
            current_node = current_node.nxt

        elif current_node.v > 0:
            temp_node = create_new(current_node)
            next_node = current_node.nxt
            # if current_node == head_node:
            #     head_node = next_node
            current_node.remove()
            for _ in range(current_node.v):
                temp_node = temp_node.nxt

            temp_node.insert_after(current_node)
            current_node = next_node
        elif current_node.v < 0:
            temp_node = create_new(current_node)
            prev_node = current_node.nxt
            # if current_node == head_node:
            #     head_node = prev_node
            current_node.remove()
            for _ in range(abs(current_node.v)):
                temp_node = temp_node.prev

            temp_node.insert_before(current_node)
            current_node = prev_node
        # print_list(head_node)
    print_list(head_node)

    print(sum([get_index(head_node, 1000).v, get_index(head_node, 2000).v, get_index(head_node, 3000).v]))
    return head_node


def process_lines_2(lines):
    lines, head_node = parse_input_2(lines)
    print(len(lines))
    for i in range(10):
        seen = []
        current_node = head_node
        # print_list(head_node)

        count = 0
        while len(seen) < len(lines):
            count += 1
            if count % 100 == 0:
                print(count, len(seen))
            # print_list(head_node)

            if current_node.id in seen:
                current_node = current_node.nxt
                continue
            seen.append(current_node.id)
            if current_node.v == 0:
                if current_node == head_node:
                    head_node = current_node.nxt
                current_node = current_node.nxt

            elif current_node.v > 0:
                temp_node = create_new(current_node)
                next_node = current_node.nxt
                if current_node == head_node:
                    head_node = next_node
                current_node.remove()
                for _ in range(current_node.v):
                    temp_node = temp_node.nxt

                temp_node.insert_after(current_node)
                current_node = next_node
            elif current_node.v < 0:
                temp_node = create_new(current_node)
                prev_node = current_node.nxt
                if current_node == head_node:
                    head_node = prev_node
                current_node.remove()
                for _ in range(abs(current_node.v)):
                    temp_node = temp_node.prev

                temp_node.insert_before(current_node)
                current_node = prev_node
            print_list(head_node)
        print_list(head_node)

    print(sum([get_index(head_node, 1000).v, get_index(head_node, 2000).v, get_index(head_node, 3000).v]))
    return head_node


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/20_1.txt"
    start = time.time()
    # process_lines_1(readfile(file))
    process_lines_2(readfile(file))
    end = time.time()
    print(end - start)
