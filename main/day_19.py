import time
from collections import deque
import numpy as np


def parse_input(lines):
    numbers = []
    for l in lines:
        s = l.split(" ")
        ore_robot_cost = int(s[6])
        clay_robot_cost = int(s[12])
        obsidian_robot_cost = (int(s[18]), int(s[21]))
        geode_robot_cost = (int(s[27]), int(s[30]))

        numbers.append((ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost))

    return numbers


def add_resource(state):
    state[0] += state[1]
    state[2] += state[3]
    state[4] += state[5]
    state[6] += state[7]
    state[8] -= 1
    return state


def calc_max(blueprint, t):
    max_ = 0
    # 0: ore
    # 1: ore robot count
    # 2: clay
    # 3: clay robot count
    # 4: obsidian
    # 5: obsisian robot count
    # 6: geode
    # 7: geode robot count
    # 8: time left

    queue = deque()
    queue.append([0, 1, 0, 0, 0, 0, 0, 0, t])

    seen = set()
    count = 55
    # We don't need to produce more robots than the max required for a new robot
    # as only one robot can be made at one time
    max_ore_prod = max([blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0]])
    max_clay_prod = blueprint[2][1]
    max_obs_prod = blueprint[3][1]

    max_geode_robot = 0

    while len(queue) > 0:
        current = queue.popleft()
        check = tuple(current)
        if check in seen:
            continue
        else:
            seen.add(check)
        if current[6] > max_:
            max_ = current[6]
            print(max_)

        if current[8] == 0:
            continue

        # if len(seen) % 1000000 == 0:
        #     print(max_, len(seen))
        if max_ > current[7] * current[8] + current[6] and t < 5:
            continue
        # if current[7] > max_geode_robot:
        #     max_geode_robot = current[7]
        # elif current[7] < (max_geode_robot) // 2:
        #     continue

        # if current[8] < count:
        #     print(current[8], len(queue))
        #     count = current[8]
        # create new ore robot
        o = blueprint[0]
        if current[0] >= o and current[1] < max_ore_prod:
            new = add_resource(current.copy())
            new[0] -= o
            new[1] += 1
            queue.appendleft(new)
        # create new clay robot
        o = blueprint[1]
        if current[0] >= o and current[3] < max_clay_prod:
            new = add_resource(current.copy())
            new[0] -= o
            new[3] += 1
            queue.appendleft(new)
        # create new obsidian robot
        o, c = blueprint[2]
        if current[0] >= o and current[2] >= c and current[5] < max_obs_prod:
            new = add_resource(current.copy())
            new[0] -= o
            new[2] -= c
            new[5] += 1
            queue.appendleft(new)
        # create new geode robot
        o, o_ = blueprint[3]
        if current[0] >= o and current[4] >= o_:
            new = add_resource(current.copy())
            new[0] -= o
            new[4] -= o_
            new[7] += 1
            queue.appendleft(new)

        new = add_resource(current.copy())
        queue.append(new)

    return max_


def process_lines_1(lines):
    blueprints = parse_input(lines)

    bp_max = []
    for i in range(len(blueprints)):
        m = calc_max(blueprints[i], 24)
        print(m, i)
        bp_max.append(m)

    print(bp_max)

    sum_ = 0
    for m in range(len(bp_max)):
        prod = bp_max[m] * (m+1)
        sum_ += prod
    print(sum_)


def process_lines_2(lines):
    blueprints = parse_input(lines)

    bp_max = []
    # for i in range(3):
    for i in range(len(blueprints)):
        m = calc_max(blueprints[i], 32)
        print(m, i)
        bp_max.append(m)

    print(bp_max)

    print(np.prod(bp_max))


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/19_1.txt"
    start = time.time()

    process_lines_1(readfile(file))
    # process_lines_2(readfile(file))
    end = time.time()
    print(end - start)