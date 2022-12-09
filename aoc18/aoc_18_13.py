import time
from itertools import permutations
from collections import Counter

day_one_test = """
/->-\        
|   |  /----\\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/  
"""

day_two_test = """
/>-<\  
|   |  
| /<+-\\
| | | v
\>+</ |
  |   ^
  \<->/
"""

with open(r'aoc_18_13.txt', 'r') as f:
    raw_input = f.read()

class Directions(dict):
    @property
    def reversed(self):
        return {value: key for key, value in self.items()}

    def __setitem__(self, *args, **kwargs):
        super().__setitem__(*args, **kwargs)
        self.order = list(self.keys())

    def next_directions(self, current):
        if not current in self.keys():
            raise ValueError()
        cur_idx = self.order.index(current)
        left = self.order[(cur_idx - 1) % len(self.order)]
        right = self.order[(cur_idx + 1) % len(self.order)]
        return left, current, right

directions = Directions()
directions[(0, 1)] = '^'
directions[(1, 0)] = '>'
directions[(0, -1)] = 'v'
directions[(-1, 0)] = '<'

class TopGrid(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.carts = []
        self.intersections = []
        self.collission = False

    def _max_x(self):
        return max([x[0] for x in self.keys()])

    def _max_y(self):
        return max([x[1] for x in self.keys()])

    def __repr__(self):
        string_parts = []
        for y in range(self._max_y()+1):
            for x in range(self._max_x()+1):
                if (x, y) in self.carts:
                    string_parts.append(directions[self.carts[self.carts.index((x, y))].direction])
                elif (x, y) in self.keys():
                    string_parts.append(self[(x, y)])
                else:
                    string_parts.append(" ")
            string_parts.append("\n")
        return "".join(string_parts)

    def check_collisions(self):
        if len(set(self.carts)) < len(self.carts):
            return True
        return False

    @classmethod
    def from_string(cls, raw_input):
        new_cls = cls()
        for line_idx, line in enumerate(raw_input.strip().split('\n')):
            for row_idx, char in enumerate(line):
                if not char == " ":
                    if char in ["v", "^"]:
                        new_cls[(row_idx, line_idx)] = "|" # added to show grid easier
                    elif char in ["<", ">"]:
                        new_cls[(row_idx, line_idx)] = "-" # added to show grid easier
                    else:
                        new_cls[(row_idx, line_idx)] = char
                if char == "+":
                    new_cls.intersections.append((row_idx, line_idx))
                if char in "^>v<":
                    new_cls.carts.append(Cart(row_idx, line_idx, directions.reversed[char], new_cls)) # rev_directions translates char (^ > v <) to cartesian directions
        return new_cls

    def day_one_tick(self):
        for cart in self.carts:
            cart.tick()
            if self.check_collisions():
                c = Counter(self.carts)
                self.collission = [key for key, value in c.items() if value == 2][0]
                return

    def day_two_tick(self):
        list_of_cars_to_move = sorted([cart for cart in self.carts], key=lambda c: c.x*10000 + c.y)
        for cart in list_of_cars_to_move:
            cart.tick()
            if self.check_collisions():
                for key, value in Counter(self.carts).items():
                    if value == 2:
                        self.carts = [c for c in self.carts if not (key.x == c.x and key.y == c.y)]

class Cart:
    def __init__(self, x, y, direction, grid_ref):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid_ref = grid_ref
        self.cross_roads_direction = 0

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, tuple):
            if self.x == other[0] and self.y == other[1]:
                return True
        if isinstance(other, Cart):
            if self.x == other.x and self.y == other.y:
                return True

    def tick(self):
        left_d, ahead_d, right_d = directions.next_directions(self.direction)
        left = (self.x + left_d[0], self.y - left_d[1])
        ahead = (self.x + ahead_d[0], self.y - ahead_d[1])
        right = (self.x + right_d[0], self.y - right_d[1])

        current_char = self.grid_ref[(self.x, self.y)]

        if current_char == "+":
            if self.cross_roads_direction == 0:
                self.x, self.y = left
                self.direction = left_d
                self.cross_roads_direction = 1
            elif self.cross_roads_direction == 1:
                self.x, self.y = ahead
                self.direction = ahead_d
                self.cross_roads_direction = 2
            elif self.cross_roads_direction == 2:
                self.x, self.y = right
                self.direction = right_d
                self.cross_roads_direction = 0

        elif self.direction == (0, -1) or self.direction == (0, 1): # ^ or v
            if ord(current_char) == 92: # \
                self.x, self.y = left
                self.direction = left_d
            elif ord(current_char) == 47: # /
                self.x, self.y = right
                self.direction = right_d
            else:
                self.x, self.y = ahead
                self.direction = ahead_d

        elif self.direction == (1, 0) or self.direction == (-1, 0):    # < or >
            if ord(current_char) == 92: # \
                self.x, self.y = right
                self.direction = right_d
            elif ord(current_char) == 47: # /
                self.x, self.y = left
                self.direction = left_d
            else:
                self.x, self.y = ahead
                self.direction = ahead_d

    def __hash__(self):
        return hash((self.x, self.y))

def day_one(raw_input):
    grid = TopGrid.from_string(raw_input)
    while True:
        grid.day_one_tick()
        if grid.collission:
            print(grid.collission)
            break

def day_two(raw_input):
    grid = TopGrid.from_string(raw_input)
    while True:
        grid.day_two_tick()
        if len(grid.carts) == 1:
            print(grid.carts[0])
            break

day_one(day_one_test)
day_one(raw_input)
day_two(day_two_test)
day_two(raw_input)