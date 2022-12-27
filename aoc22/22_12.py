from operator import attrgetter

with open(r'22_12.txt', 'r') as f:
    raw_lines = f.read().strip()

# raw_lines = '''Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi'''

heights = "abcdefghijklmnopqrstuvwxyz"

def get_height(letter):
    match letter:
        case 'S':
            return 0
        case 'E':
            return 25
        case _:
            return heights.find(letter)

class Node:
    def __init__(self, x, y, char, height):
        self.x             = x
        self.y             = y
        self.char          = char
        self.height        = height
        self.connections   = []
        self.shortest_path = None

    def set_target(self, target):
        self.target = target
        self.distance    = self._distance(target)

    def _distance(self, other):
        return (abs(self.x - other.x)**2 + abs(self.y - other.y)**2) ** 0.5

    def __repr__(self):
        return f'<Node ({self.x}, {self.y}): {self.char}>'

    def __lt__(self, other):
        return self.distance > other.distance

height_map = {
    (idx_col, idx_row): Node(x=idx_col, y=idx_row, char=char, height=get_height(char))
    for idx_row, line in enumerate(raw_lines.split('\n'))
    for idx_col, char in enumerate(line)
}

width  = max(key[0] for key in height_map.keys())+1
height = max(key[1] for key in height_map.keys())+1

target_node = [node for node in height_map.values() if node.char == 'E'][0]
target_node.set_target(target_node)
starting_node = [node for node in height_map.values() if node.char == 'S'][0]
starting_node.set_target(target_node)

for row in range(height):
    for col in range(width):
        node = height_map[(col, row)]
        node.set_target(target_node)
        directions = [(col, row+1), (col, row-1), (col-1, row), (col+1, row)]
        for direction in directions:
            if not direction in height_map.keys():
                continue
            if 0 <= height_map[direction].height <= node.height + 1:
                node.connections.append(height_map[direction])

def clear_paths(height_map):
    for value in height_map.values():
        value.shortest_path = None

def calculate_path(starting_node, target_node, height_map):
    clear_paths(height_map)

    starting_node.shortest_path = [starting_node]
    to_test = [starting_node, ]

    while True:
        if len(to_test) == 0:
            break

        next_test = to_test.pop(0)

        for connection in next_test.connections:
            path = [node for node in next_test.shortest_path] + [connection]

            if connection.shortest_path is None:
                connection.shortest_path = path
                to_test.append(connection)
            
            if len(path) < len(connection.shortest_path):
                connection.shortest_path = path
                to_test.append(connection)

    return len(target_node.shortest_path)-1

print(f'Part 1: Length of path: {calculate_path(starting_node, target_node, height_map)}')

def most_scenic_path(target, height_map):
    starting_nodes = [node for node in height_map.values() if node.height == 0 and any(n.char == 'b' for n in node.connections)]

    best_path = None

    for starting_node in starting_nodes:
        path = calculate_path(starting_node, target_node, height_map)

        if best_path is None:
            best_path = path
        else:
            best_path = min(best_path, path)
    
    return best_path

print(f'Part 2: Most Scenic Path: {most_scenic_path(target_node, height_map)}')