import time


def print_cave(cave):
    for i in range(50, -1, -1):
        print("".join(cave[i]))


class Rock:
    def __init__(self):
        self.pieces = []
        self.width = 0
        self.height = 0

    def set_pieces(self, l):
        self.pieces = l
        self.height, self.width = self.get_size()

    def ret_size(self):
        return self.height, self.width

    def get_size(self):
        height = 0
        width = 0

        for p in self.pieces:
            if p[0] > height:
                height = p[0]
            if p[1] > width:
                width = p[1]

        return height + 1, width + 1

    def get_left(self, h):
        most_left = 99
        for p in self.pieces:
            if p[0] == h:
                if p[1] < most_left:
                    most_left = p[1]
        return most_left

    def get_right(self, h):
        most_right = -1
        for p in self.pieces:
            if p[0] == h:
                if p[1] > most_right:
                    most_right = p[1]
        return most_right

    def get_down(self, w):
        most_down = 99
        for p in self.pieces:
            if p[1] == w:
                if p[0] < most_down:
                    most_down = p[0]
        return most_down

    def get_edges(self, case):
        arr = []
        if case == "LEFT":
            for h in range(self.height):
                arr.append([h, self.get_left(h)])
        if case == "RIGHT":
            for h in range(self.height):
                arr.append([h, self.get_right(h)])
        if case == "DOWN":
            for w in range(self.width):
                arr.append([self.get_down(w), w])

        return arr


def get_rocks():
    rock_list = []
    r1 = Rock()
    r1.set_pieces([(0, 0), (0, 1), (0, 2), (0, 3)])
    rock_list.append(r1)
    r2 = Rock()
    r2.set_pieces([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)])
    rock_list.append(r2)
    r3 = Rock()
    r3.set_pieces([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])
    rock_list.append(r3)
    r4 = Rock()
    r4.set_pieces([(0, 0), (1, 0), (2, 0), (3, 0)])
    rock_list.append(r4)
    r5 = Rock()
    r5.set_pieces([(0, 0), (0, 1), (1, 0), (1, 1)])
    rock_list.append(r5)

    return rock_list


def process_lines_1(lines):
    input = lines[0]
    print(input)

    rocks = get_rocks()

    cave = []
    for i in range(5000):
        cave.append(["."] * 7)


    jet = 0
    mod = len(input)

    max_height = 0

    for r in range(2022):
        new_rock = rocks[r % len(rocks)]
        height, width = new_rock.ret_size()
        pos = [max_height + 3, 2]

        settle = False

        while not settle:
            move_jet = input[jet % mod]
            print(move_jet)
            if move_jet == "<":
                valid_left = True
                if pos[1] == 0:
                    valid_left = False
                else:
                    most_left = new_rock.get_edges("LEFT")
                    for piece in most_left:
                        if cave[pos[0] + piece[0]][pos[1] + piece[1] - 1] == "#":
                            valid_left = False

                if valid_left:
                    pos[1] += -1

            if move_jet == ">":
                valid_right = True
                if pos[1] + width == 7:
                    valid_right = False
                else:
                    most_right = new_rock.get_edges("RIGHT")
                    for piece in most_right:
                        if cave[pos[0] + piece[0]][pos[1] + piece[1] + 1] == "#":
                            valid_right = False

                if valid_right:
                    pos[1] += 1

            valid_down = True
            most_down = new_rock.get_edges("DOWN")
            if pos[0] == 0:
                valid_down = False
            else:
                for piece in most_down:
                    t_0 = pos[0] + piece[0] - 1
                    t_1 = pos[1] + piece[1]
                    if cave[pos[0] + piece[0] - 1][pos[1] + piece[1]] == "#":
                        valid_down = False
                        break

            if valid_down:
                pos[0] += -1
            else:
                settle = True
                for piece in new_rock.pieces:
                    cave[pos[0] + piece[0]][pos[1] + piece[1]] = "#"
                if pos[0] + height > max_height:
                    max_height = pos[0] + height
                print_cave(cave)
                print(max_height)
                print()
            jet += 1


def find_cycle(rocks: list):
    rock_set = set()
    first = None
    first_index = 0
    count = 0
    for i in range(len(rocks)):
        r = rocks[i]
        if r in rock_set:
            if first is None:
                first = r
                first_index = i
                count += 1
            elif r == first:
                print("CYCLE FOUND YAY", count, first_index)

                return count, first_index
            else:
                count += 1
        else:
            rock_set.add(r)
            first = None
            count = 0
            first_index = 0

    return 0, 0



def process_lines_2(lines):
    T = 1000000000000
    input = lines[0]
    print(input)
    print(len(input))
    set_rocks = []
    set_heights = []
    rocks = get_rocks()



    cave = []
    for i in range(1000000):
        cave.append(["."] * 7)

    jet = 0
    mod = len(input)

    max_height = 0

    for r in range(T):
        if r % 1000000 == 0:
            print(r)
        new_rock = rocks[r % len(rocks)]
        height, width = new_rock.ret_size()
        pos = [max_height + 3, 2]

        settle = False

        while not settle:
            move_jet = input[jet % mod]
            print(move_jet)
            if move_jet == "<":
                valid_left = True
                if pos[1] == 0:
                    valid_left = False
                else:
                    most_left = new_rock.get_edges("LEFT")
                    for piece in most_left:
                        if cave[pos[0] + piece[0]][pos[1] + piece[1] - 1] == "#":
                            valid_left = False

                if valid_left:
                    pos[1] += -1

            if move_jet == ">":
                valid_right = True
                if pos[1] + width == 7:
                    valid_right = False
                else:
                    most_right = new_rock.get_edges("RIGHT")
                    for piece in most_right:
                        if cave[pos[0] + piece[0]][pos[1] + piece[1] + 1] == "#":
                            valid_right = False

                if valid_right:
                    pos[1] += 1

            valid_down = True
            most_down = new_rock.get_edges("DOWN")
            if pos[0] == 0:
                valid_down = False
            else:
                for piece in most_down:
                    t_0 = pos[0] + piece[0] - 1
                    t_1 = pos[1] + piece[1]
                    if cave[pos[0] + piece[0] - 1][pos[1] + piece[1]] == "#":
                        valid_down = False
                        break

            if valid_down:
                pos[0] += -1
            else:
                settle = True
                for piece in new_rock.pieces:
                    cave[pos[0] + piece[0]][pos[1] + piece[1]] = "#"
                if pos[0] + height > max_height:
                    max_height = pos[0] + height

                if len(set_heights) == 0:
                    s = (max_height - pos[0], pos[1], r % len(rocks), jet % mod, max_height)
                else:
                    s = (max_height - pos[0], pos[1], r % len(rocks), jet % mod, max_height - set_heights[len(set_heights) - 1])
                set_rocks.append(s)
                set_heights.append(max_height)
                if r > 2022:
                    cycle, index = find_cycle(set_rocks)
                    if cycle != 0:
                        print(cycle, index, r)
                        n = 0
                        for m in range(index, index + cycle):
                            print(set_heights[m])
                            n += set_heights[m]
                        n = set_heights[index + cycle - 1]
                        m = set_heights[index]
                        change_per_cycle = (set_heights[index + cycle] - set_heights[index])
                        remaining_steps = T - index
                        cycles_to_add = remaining_steps // cycle

                        height_to_add = cycles_to_add * change_per_cycle
                        new_height = set_heights[index] + height_to_add

                        steps_left_over = remaining_steps - (cycles_to_add * cycle)

                        final_amount_to_add = set_heights[index + steps_left_over] - set_heights[index]

                        new_height += final_amount_to_add

                        print(new_height - 1)
                        return 0

            jet += 1


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/17.txt"
    start = time.time()

    process_lines_1(readfile(file))
    process_lines_2(readfile(file))
    end = time.time()
    print(end - start)
