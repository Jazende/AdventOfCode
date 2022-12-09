import re

with open(r'aoc_18_03.txt', 'r') as f:
    raw_input = f.read()

class Claim:
    def __init__(self, id_, loc_x, loc_y, size_x, size_y):
        self.id_ = id_
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.size_x = size_x
        self.size_y = size_y
        self.os_x = loc_x+size_x
        self.os_y = loc_y+size_y
            
    def overlap(self, other, once=False):
        if (other.loc_x <= self.loc_x <= other.os_x) and (other.loc_y <= self.loc_y <= other.os_y):
            return True
        elif (other.loc_x <= self.os_x <= other.os_x) and (other.loc_y <= self.loc_y <= other.os_y):
            return True
        elif (other.loc_x <= self.loc_x <= other.os_x) and (other.loc_y <= self.os_y <= other.os_y):
            return True
        elif (other.loc_x <= self.os_x <= other.os_x) and (other.loc_y <= self.os_y <= other.os_y):
            return True
        elif not once:
            return other.overlap(self, once=True)
        else:
            return False

    def __eq__(self, other):
        if self.id_ == other.id_:
            return True
        return False

    def __repr__(self):
        return f"<#{self.id_} @{self.loc_x}x{self.loc_y}->{self.os_x}x{self.os_y}>"

inputs = raw_input.strip().split("\n")
field = {}
formatted_inputs = []
claims = []

for line in inputs:
    id_, at, loc, size = line.split(" ")
    id_ = id_[1:]
    loc_x, loc_y = loc.split(",")
    loc_y = loc_y[:-1]
    size_x, size_y = size.split("x")
    id_ = int(id_)
    loc_x = int(loc_x)
    loc_y = int(loc_y)
    size_x = int(size_x)
    size_y = int(size_y)
    formatted_inputs.append([id_, loc_x, loc_y, size_x, size_y])
    claims.append(Claim(id_, loc_x, loc_y, size_x, size_y))
    
def day_1():
    for input_ in formatted_inputs:
        id_, loc_x, loc_y, size_x, size_y = input_
        for x in range(loc_x, loc_x+size_x):
            for y in range(loc_y, loc_y+size_y):
                if not (x, y) in field:
                    field[(x, y)] = 0
                field[(x, y)] += 1

    count = 0
    for key, value in field.items():
        if value >= 2:
            count += 1
    
    return count

def day_2():
    for claim in claims:
        list_ = [x for x in claims if not x == claim]
        res = not any([claim.overlap(x) for x in list_])
        if res:
            return claim

print(day_1())
print(day_2())
