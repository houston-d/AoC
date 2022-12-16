import sys
import itertools
import time

def format(lines):
    sets = []

    for l in lines:
        first, second = l.split(";")
        pipe, rate = first.split(",")
        tunnels = second.split(",")
        sets.append((pipe, int(rate), tunnels))

    return sets


class Node:
    def __init__(self, label, flow):
        self.label = label
        self.flow = flow
        self.adjacent = {}

    def add_neighbour(self, n, weight=1):
        if n not in self.adjacent.keys():
            self.adjacent[n] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_weight(self, n):
        return self.adjacent[n]

    def remove_neighbour(self, n):
        del self.adjacent[n]


class Graph:
    def __init__(self):
        self.verts = {}
        self.num_vert = 0

    def __iter__(self):
        return iter(self.verts.values())

    def add_vertex(self, v, flow):
        if v in self.verts:
            return None
        new_v = Node(v, flow)
        self.verts[v] = new_v
        self.num_vert += 1
        return new_v

    def get_vertex(self, v):
        if v in self.verts:
            return self.verts[v]
        else:
            return None

    def add_edge(self, f, t, weight=1):
        self.verts[f].add_neighbour(self.verts[t], weight)
        self.verts[t].add_neighbour(self.verts[f], weight)

    def get_vertices(self):
        return self.verts.keys()

    def remove_vertex(self, n):
        del self.verts[n]


def create_labels(g: Graph):
    labels = {}
    for v_key in g.get_vertices():
        v = g.get_vertex(v_key)

        for n in v.get_connections():
            weight = v.get_weight(n)
            s = sorted([v_key, n.label])
            key = (s[0], s[1])
            labels[key] = weight
    return labels


def construct_graph(sets):
    G = Graph()

    for s in sets:
        G.add_vertex(s[0], s[1])

    for s in sets:
        for to in s[2]:
            G.add_edge(s[0], to, 1)

    return G


def permutations(g: Graph):
    non_zero = []
    for v_key in g.get_vertices():
        v = g.get_vertex(v_key)
        if v.flow != 0:
            non_zero.append(v_key)

    return non_zero


def shortest_path(g: Graph, f):
    unvisited = list(g.get_vertices())
    shortest_path_dict = {}
    previous = {}
    max_ = sys.maxsize
    for node in unvisited:
        shortest_path_dict[node] = max_

    shortest_path_dict[f] = 0

    while unvisited:
        current_min = None
        for n in unvisited:
            if current_min == None:
                current_min = n
            elif shortest_path_dict[n] < shortest_path_dict[current_min]:
                current_min = n

        neighbours = g.get_vertex(current_min).get_connections()
        for neighbour in neighbours:
            label = neighbour.label
            temp = shortest_path_dict[current_min] + 1
            if temp < shortest_path_dict[label]:
                shortest_path_dict[label] = temp
                previous[label] = current_min

        unvisited.remove(current_min)
    return shortest_path_dict


def calc_flow(G: Graph, p, dict, mins):
    flows = []
    for label in p:
        flows.append(G.get_vertex(label).flow)

    current_flow = 0
    total_flow = 0
    count = 0
    current = "AA"

    for i in range(len(p)):
        next_ = p[i]
        step = dict[current][next_]
        for _ in range(step):
            total_flow += current_flow
            count += 1
            if count >= mins:
                return total_flow, False
        count += 1
        total_flow += current_flow
        current_flow += flows[i]

        if count >= mins:
            return total_flow, False
        current = next_

    total_flow += (mins - count) * current_flow

    return total_flow, True


def process_lines_1(lines):
    sets = format(lines)

    G = construct_graph(sets)

    perms = permutations(G)

    t = ["AA"]
    for opt in perms:
        t.append(opt)

    dict = {}
    for label in t:
        dict[label] = shortest_path(G, label)

    best = 0

    for opt in list(itertools.permutations(perms, r=7)):
        temp = calc_flow(G, opt, dict, 30)
        if temp > best:
            best = temp

    print(best)


def process_lines_2(lines):
    sets = format(lines)

    G = construct_graph(sets)

    perms = permutations(G)

    t = ["AA"]
    for opt in perms:
        t.append(opt)

    dict = {}
    for label in t:
        dict[label] = shortest_path(G, label)

    best = 0

    opt_list = list(itertools.permutations(perms, r=7))
    values = []
    l = len(opt_list)
    print(l)
    count = 0
    for opt in opt_list:
        count += 1
        if count % 1000000 == 0:
            print(count)
        temp_1, spare_1 = calc_flow(G, opt, dict, 26)
        values.append(temp_1)

    opt_list = [x for _, x in sorted(zip(values, opt_list), reverse=True)]
    values.sort(reverse=True)
    count = 0
    for i in range(len(values)):
        count += 1
        if count % 1000000 == 0:
            print(count)
        if values[i] < best / 2:
            break
        for j in range(i + 1, len(values)):
            okay = True
            for a in opt_list[i]:
                if a in opt_list[j]:
                    okay = False
            if okay:
                s = values[i] + values[j]
                if s < best:
                    break

                if s > best:
                    best = s
                    print(s, values[i], values[j])

    print(best)


def readfile(s):
    f = open(s, "r")
    data = f.read()
    f.close()
    return data.split("\n")


if __name__ == "__main__":
    file = "../resources/16.txt"
    start = time.time()

    process_lines_1(readfile(file))
    # have not run to completion, but correct answer printed in ~8 mins
    process_lines_2(readfile(file))
    end = time.time()
    print(end - start)
