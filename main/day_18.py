import time
import heapq


def parse_input(lines):
    cubes = []

    for l in lines:
        x, y, z = l.split(",")
        cubes.append((int(x), int(y), int(z)))

    return cubes


def process_lines_1(lines):
    cubes = parse_input(lines)

    added = set()

    faces = 0

    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    for cube in cubes:
        extra = 6

        for d in dirs:
            adj = (cube[0] + d[0], cube[1] + d[1], cube[2] + d[2])
            if adj in added:
                extra -= 2
        faces += extra
        added.add(cube)

    print(faces)


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    # defining less than for purposes of heap queue
    def __lt__(self, other):
        return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
        return self.f > other.f


def astar(added, start):
    end = (0, 0, 0)

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    outer_iterations = 0
    max_iterations = 75

    dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

    while len(open_list) > 0:
        outer_iterations += 1

        if outer_iterations > max_iterations:
            # By this point, it will not contain the destination
            return 0

        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        if current_node == end_node:
            return 1

        children = []

        for new_position in dirs:
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1],
                             current_node.position[2] + new_position[2])

            if node_position in added:
                continue

            if node_position[0] > 23 or \
                    node_position[0] < 0 or \
                    node_position[1] > 23 or \
                    node_position[1] < 0 or \
                    node_position[2] > 23 or \
                    node_position[2] < 0:
                # If it can reach the edge then we have success
                return 1

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            child.g = current_node.g + (((child.position[0] - child.parent.position[0]) ** 2) + (
                        (child.position[1] - child.parent.position[1]) ** 2) + (
                        (child.position[2] - child.parent.position[2]) ** 2))
            child.h = (((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2) + (
                        (child.position[2] - end_node.position[2]) ** 2))
            child.f = child.g + child.h

            if child in open_list:
                idx = open_list.index(child)
                if child.g < open_list[idx].g:
                    open_list[idx].g = child.g
                    open_list[idx].f = child.f
                    open_list[idx].h = child.h
            else:
                heapq.heappush(open_list, child)

    # no path found
    return 0


def process_lines_2(lines):
    cubes = parse_input(lines)

    added = set()
    edges = set()

    faces = 0

    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    for cube in cubes:
        extra = 6

        for d in dirs:
            adj = (cube[0] + d[0], cube[1] + d[1], cube[2] + d[2])
            if adj in added:
                extra -= 2
            edges.add(adj)
        faces += extra
        added.add(cube)

    for cub in added:
        if cub in edges:
            edges.remove(cub)

    faces_to_remove = 0

    for c in edges:
        count = 0
        for d in dirs:
            adj = (c[0] + d[0], c[1] + d[1], c[2] + d[2])
            if adj in added:
                count += 1

        if astar(added, c) == 0:
            faces_to_remove += count

    print(faces - faces_to_remove)


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/18.txt"
    start = time.time()

    process_lines_1(readfile(file))
    process_lines_2(readfile(file))
    end = time.time()
    print(end - start)
