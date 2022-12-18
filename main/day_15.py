import time
def parse_input(lines):
    pairs = set()
    beacons = set()
    max_distance = 0
    j_list = []

    for l in lines:
        sensor, beacon = l.split(":")
        s = list(map(int, sensor.split(",")))
        b = list(map(int, beacon.split(",")))
        d_i = abs(s[1] - b[1])
        d_j = abs(s[0] - b[0])
        d = d_i + d_j
        if d > max_distance:
            max_distance = d
        j_list.append(s[0])
        j_list.append(b[0])

        pairs.add((s[0], s[1], d))
        beacons.add((b[0], b[1]))

    min_j = min(j_list)
    max_j = max(j_list)

    return pairs, beacons, min_j, max_j, max_distance,


def process_lines_1(lines):

    # target = 10
    target = 2000000

    pairs, beacons, min_j, max_j, max_dis = parse_input(lines)

    for p in pairs:
        print(p)

    print(beacons)
    count = 0

    for j in range(min_j - max_dis, max_j + max_dis):

        not_possible = False
        for (s_j, s_i, d) in pairs:
            diff = abs(j - s_j) + abs(target - s_i)
            if diff <= d:
                not_possible = True

        if (j, target) in beacons:
            not_possible = False

        if not_possible:
            count += 1

    print(count)


def process_lines_2(lines):
    count = 0
    # max_v = 20
    max_v = 4000000
    pairs, beacons, min_j, max_j, max_dis = parse_input(lines)

    pairs = list(pairs)
    pairs.sort()

    for s_j, s_i, d in pairs:
        for j_change in range(-d, d):
            diff = d - abs(j_change)
            edge = [(s_j + j_change, s_i + diff), (s_j + j_change, s_i - diff)]

            test = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for e in edge:
                for t in test:
                    j = e[0] + t[0]
                    i = e[1] + t[1]

                    is_free = True
                    for new_s_j, new_s_i, new_d in pairs:
                        count += 1
                        if abs(new_s_j - j) + abs(new_s_i - i) <= new_d:

                            is_free = False
                    if is_free:
                        if 0 <= j <= max_v and 0 <= i <= max_v:
                            print(j, i)
                            print(j * 4000000 + i)
                            print(s_j, s_i)
                            return count


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/15.txt"
    start = time.time()
    # process_lines_1(readfile(file))
    count = process_lines_2(readfile(file))
    print(count)
    end = time.time()
    print(end - start)
