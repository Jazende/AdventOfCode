import sys
sys.path.append(r'C:\Users\kridder\Desktop\Python\custom')
from jaz_funcs.points import Punt
from jaz_funcs.classes import UniqueObject

with open(r'aoc_18_18.txt', 'r') as f:
    raw_input = f.read()

##raw_input = """.#.#...|#.\n.....#|##|\n.|..|...#.
##..|#.....#\n#.#|||#|#|\n...#.||...\n.|....|...
##||...#|.#|\n|.||||..|.\n...#.|..|."""

inputs = [x for x in raw_input.strip().split("\n")]

class Acre(Punt, UniqueObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n = None
        self.ne = None
        self.e = None
        self.se = None
        self.s = None
        self.sw = None
        self.w = None
        self.nw = None
        self.new_value = None

    @property
    def neighbours(self):
        poss_n = [self.n, self.ne, self.e, self.se,
                  self.s, self.sw, self.w, self.nw]
        return [acre for acre in poss_n if acre]

    @property
    def adj_trees(self):
        return len([acre for acre in self.neighbours if acre.value == "|"])

    @property
    def adj_lumber(self):
        return len([acre for acre in self.neighbours if acre.value == "#"])

    @property
    def adj_open(self):
        return len([acre for acre in self.neighbours if acre.value == "."])
    
    def grow(self):
        # Open: "."
        # Tree: "|"
        # Lumber: "#"
        if self.value == ".":
            if self.adj_trees >= 3:
                self.new_value = "|"
            else:
                self.new_value = "."
                
        if self.value == "|":
            if self.adj_lumber >= 3:
                self.new_value = "#"
            else:
                self.new_value = "|"
                
        if self.value == "#":
            if self.adj_lumber >= 1 and self.adj_trees >= 1:
                self.new_value = "#"
            else:
                self.new_value = "."

    def tick(self):
        if self.new_value:
            self.value = self.new_value
            self.new_value = None

class Grounds:
    def __init__(self, inputs):
        self._grounds = {}
        self.x = len(inputs)
        for i, line in enumerate(inputs):
            self.y = len(line)
            for j, value in enumerate(line):
                self._grounds[(i, j)] = Acre(i, j, value=value)

        for piece_of_land in self._grounds:
            x, y = piece_of_land
            if (x-1, y) in self._grounds:
                self._grounds[(x, y)].n = self._grounds[(x-1, y)]
                
            if (x-1, y+1) in self._grounds:
                self._grounds[(x, y)].ne = self._grounds[(x-1, y+1)]
                
            if (x, y+1) in self._grounds:
                self._grounds[(x, y)].e = self._grounds[(x, y+1)]
                
            if (x+1, y+1) in self._grounds:
                self._grounds[(x, y)].se = self._grounds[(x+1, y+1)]
                
            if (x+1, y) in self._grounds:
                self._grounds[(x, y)].s = self._grounds[(x+1, y)]
                
            if (x+1, y-1) in self._grounds:
                self._grounds[(x, y)].sw = self._grounds[(x+1, y-1)]
                
            if (x, y-1) in self._grounds:
                self._grounds[(x, y)].w = self._grounds[(x, y-1)]
                
            if (x-1, y-1) in self._grounds:
                self._grounds[(x, y)].nw = self._grounds[(x-1, y-1)]

    def grow(self):
        for pos, acre in self._grounds.items():
            acre.grow()
        for pos, acre in self._grounds.items():
            acre.tick()

    @property
    def resource_value(self):
        wood = len([x for x in self._grounds if self._grounds[x].value == "|"])
        lumber = len([x for x in self._grounds if self._grounds[x].value == "#"])
        return wood * lumber

    def __repr__(self):
        re = ""
        for i in range(self.x):
            for j in range(self.y):
                re += str(self._grounds[(i, j)])
            re += "\n"
        return re[:-1]

    def __hash__(self):
        return hash(str(self).replace("\n", ""))

g = Grounds(inputs)
seen_l = [hash(g)]
seen_d = {0: g.resource_value}
for i in range(1, 1000):
    g.grow()
    h = hash(g)
    if h in seen_l:
        # repeat = current value - index first time repeat is seen
        repeat = i - seen_l.index(h)
        first = i
        break
    seen_l.append(hash(g))
    seen_d[i] = g.resource_value

base_r = 1000000000 - first
reduc = base_r % repeat
a = first + base_r
print(seen_d[len(seen_l)-repeat+reduc])
