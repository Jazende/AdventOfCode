import re

class Node:
    def __init__(self, x, y, size, used, avail, perc):
        self.x = int(x)
        self.y = int(y)
        self.size = int(size)
        self.used = int(used)
        self.avail = int(avail)
        self.perc = int(perc)
        self.goal = False

    def __repr__(self):
        return f'N{self.x}.{self.y} S:{self.size}T U:{self.used}T A:{self.avail}T'

    def __eq__(self, other):
        if not self.x == other.x:
            return False
        if not self.y == other.y:
            return False
        return True
    
    def _value(self):
        return self.x * 100 + self.y

    def __lt__(self, other):
        if self._value() < other._value():
            return True
        return False

with open(r'aoc_16_22.txt', 'r') as f:
    raw_input = f.read().strip()

# raw_input = """
# Filesystem            Size  Used  Avail  Use%
# /dev/grid/node-x0-y0   10T    8T     2T   80%
# /dev/grid/node-x0-y1   11T    6T     5T   54%
# /dev/grid/node-x0-y2   32T   28T     4T   87%
# /dev/grid/node-x1-y0    9T    7T     2T   77%
# /dev/grid/node-x1-y1    8T    0T     8T    0%
# /dev/grid/node-x1-y2   11T    7T     4T   63%
# /dev/grid/node-x2-y0   10T    6T     4T   60%
# /dev/grid/node-x2-y1    9T    8T     1T   88%
# /dev/grid/node-x2-y2    9T    6T     3T   66%
# """

re_node = re.compile('node\-x(\d+)\-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%')

node_info = [Node(*found_re) for found_re in re_node.findall(raw_input)]

### Day One
count_pairs = 0
for node in node_info:
    for other_node in node_info:
        if node == other_node:
            continue
        if node.used == 0:
            continue
        if node.used > other_node.avail:
            continue
        count_pairs += 1
# print(count_pairs)

### Day Two
def adjecant_nodes(grid, og_node):
    return [node for node in grid.values() if (abs(node.x - og_node.x) == 1 and node.y == og_node.y) or (abs(node.y - og_node.y) == 1 and node.x == og_node.x)]

def transfer_avail(node_a, node_b):
    if not isinstance(node_a, Node) or not isinstance(node_b, Node):
        return False
    if node_a.used == 0:
        return False
    if node_a == node_b:
        return False
    if node_a.used > node_b.avail:
        return False
    return True

def print_grid(grid, start_x=None, end_x=None, start_y=None, end_y=None):
    most_available = max(node_grid.items(), key=lambda x: x[1].avail)[1]

    start_x = 0 if not start_x else start_x
    start_y = 0 if not start_y else start_y
    end_y = max(node_grid.keys(), key=lambda n: n[1])[1] + 1 if not end_y else end_y
    end_x = max(node_grid.keys(), key=lambda n: n[0])[0] + 1 if not end_x else end_x

    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if node_grid[(x, y)].goal == True:
                print(" G ", end="")
            elif node_grid[(x, y)].used == 0:
                print("[_]", end="")
            elif node_grid[(x, y)].size >= (most_available.avail * 3):
                print(" # ", end="")
            else:
                print(" . ", end="")
        print("")

def transfer_data(node_a, node_b):
    data_to_transfer = node_a.used
    node_a.used = 0
    node_a.avail = node_a.size
    node_b.used += data_to_transfer
    node_b.avail -= data_to_transfer
    if node_a.goal == True:
        node_b.goal = True
        node_a.goal = False

def get_block_in_direction(grid, direction, source):
    nearby = adjecant_nodes(grid, source)
    for node in nearby:
        if direction == "up" and node.x == source.x and node.y == source.y - 1:
            return node
        if direction == "down" and node.x == source.x and node.y == source.y + 1:
            return node
        if direction == "left" and node.x == source.x - 1 and node.y == source.y:
            return node
        if direction == "right" and node.x == source.x + 1 and node.y == source.y:
            return node

def move_empty_block(grid, direction):
    current_empty = max(grid.items(), key=lambda x: x[1].avail)[1]
    next_block = get_block_in_direction(grid, direction, current_empty)
    transfer_data(next_block, current_empty)

node_grid = {(node.x, node.y): node for node in node_info}
node_grid[(max(node_grid.keys(), key=lambda n: n[0])[0], 0)].goal = True

count_moves = 0

for i in range(26):
    move_empty_block(node_grid, 'left')
    count_moves += 1

for i in range(26):
    move_empty_block(node_grid, 'up')
    count_moves += 1

for i in range(29):
    move_empty_block(node_grid, 'right')
    count_moves += 1

for i in range(36):
    move_empty_block(node_grid, 'down')
    move_empty_block(node_grid, 'left')
    move_empty_block(node_grid, 'left')
    move_empty_block(node_grid, 'up')
    move_empty_block(node_grid, 'right')
    count_moves += 5

print_grid(node_grid, end_y=2, end_x = 2)
print(count_moves)