from collections import Counter

with open(r'aoc_17_24.txt', 'r') as f:
    raw_bridges = f.read().strip().split('\n')
str_bridges = [part.split('/') for part in raw_bridges]
real_bridges = [(int(part[0]), int(part[1])) for part in str_bridges]

example_bridges = [(0, 2), (2, 2), (2, 3), (3, 4), (3, 5), (0, 1), (10, 1), (9, 10)]

bridges = real_bridges

class Bridge:
    def __init__(self):
        self.parts = [(0, 0)]
        self._open_port()

    def _open_port(self):
        connections = []
        for part in self.parts:
            connections.append(part[0])
            connections.append(part[1])
        
        counter = Counter(connections)
        counter[0] -= 1
        self.open_port = [key for key, value in counter.items() if value % 2 == 1][0]

    def add_connection(self, part):
        if self.is_connectable(part):
            self.parts.append(part)
            self._open_port()

    def is_connectable(self, part):
        if part[0] == self.open_port or part[1] == self.open_port:
            return True
        return False

    def strength(self):
        return sum([sum(part) for part in self.parts])

    def __repr__(self):
        return " -- ".join([str(part) for part in self.parts])

    def __eq__(self, other):
        if set(self.parts) == set(other.parts):
            return True
        if set(self.parts) in set(other.parts):
            return True
        return False

    def __hash__(self):
        return hash(tuple(sorted(self.parts, key=lambda x: x[0] + x[1]*10)))

connections = [Bridge()]

idx = -1
while True:
    idx += 1
    try:
        cur_bridge = connections[idx]
    except IndexError:
        break

    poss_connections = [part for part in bridges if not part in cur_bridge.parts and cur_bridge.is_connectable(part)]
    for new_conn in poss_connections:
        new_bridge = Bridge()
        for part in cur_bridge.parts[1:]:
            new_bridge.add_connection(part)
        new_bridge.add_connection(new_conn)
        connections.append(new_bridge)

print(max(connections, key=lambda x: x.strength()), max(connections, key=lambda x: x.strength()).strength())

length_longest_bridges = len(max(connections, key=lambda x: len(x.parts)).parts)
longest_bridges = [connection for connection in connections if len(connection.parts) == length_longest_bridges]

print(max(longest_bridges, key=lambda x: x.strength()))

print(max([bridge for bridge in connections if len(bridge) == max(connections, key=lambda x: len(x.parts))]))