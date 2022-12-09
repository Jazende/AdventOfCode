from math import sqrt

##	0,5	0,5		1	1       ##	0	0,5	1	1,5
##N	0,5	1,5		1	2       ##2	x		x	
##NE	1	1		1,5	1,5     ##1,5		x		x
##SE	1	0		1,5	0,5     ##1	x		x	
##S	0,5	-0,5		1	0       ##0,5		x		x
##SW	0	0		0,5	0,5     ##0	x		x	
##NW	0	1		0,5	1,5     ##-0,5		x		x
##					
##N	0	1		0	1   
##NE	0,5	0,5		0,5	-0,5
##SE	0,5	-0,5		0,5	-0,5
##S	0	-1		0	-1
##SW	-0,5	-0,5		-0,5	-0,5
##NW	-0,5	0,5		-0,5	0,5

def test_values(x, y):
    if int(x // 0.5 % 2) == int(y // 0.5 % 2):
        return True
    else:
        return False

class HexaPunt:
    def __init__(self, x, y):
        if not test_values(x, y):
            raise ValueError("Not correct location for hexa. Grid starts at 0, 0")
        self.x = x
        self.y = y

    def __repr__(self):
        return "{} x {}".format(self.x, self.y)

    def n(self):
        return HexaPunt(self.x, self.y+1)

    def ne(self):
        return HexaPunt(self.x+0.5, self.y+0.5)

    def se(self):
        return HexaPunt(self.x+0.5, self.y-0.5)

    def s(self):
        return HexaPunt(self.x, self.y-1)

    def sw(self):
        return HexaPunt(self.x-0.5, self.y-0.5)

    def nw(self):
        return HexaPunt(self.x-0.5, self.y+0.5)

    def manhattan_distance(self, other):
        return abs(self.x-other.x) + abs(self.y-other.y)

    def euclidian_distance(self, other):
        max_x = max(self.x, other.x)
        min_x = min(self.x, other.x)
        max_y = max(self.y, other.y)
        min_y = min(self.y, other.y)
        return sqrt((max_x - min_x)**2 + (max_y - min_y)**2)

    def get_directions(self):
        directions = []
        directions.append(self.n())
        directions.append(self.ne())
        directions.append(self.nw())
        directions.append(self.s())
        directions.append(self.se())
        directions.append(self.sw())
        return directions

    def get_best_direction_to_point_manhattan(self, point):
        directions = self.get_directions()
        return min(directions, key=lambda x: x.manhattan_distance(point))

    def get_best_direction_to_point_euclidian(self, point):
        directions = self.get_directions()
        return min(directions, key=lambda x: x.euclidian_distance(point))

    def __eq__(self, other):
        if self.manhattan_distance(other) == 0:
            return True
        else:
            return False
def main():
    def calc_steps(point, target):
        steps = 0
        while True:
            if point == HexaPunt(0, 0):
                break
            point = point.get_best_direction_to_point_euclidian(HexaPunt(0, 0))
            steps += 1
        return steps
    
    curr = HexaPunt(0, 0)
    steps = []
    with open("adventofcode_input_11.txt", "r") as f:
        line = f.readline()
        for x in line.strip().split(","):
            if x == "ne":
                curr = curr.ne()
            elif x == "n":
                curr = curr.n()
            elif x == "nw":
                curr = curr.nw()
            elif x == "s":
                curr = curr.s()
            elif x == "se":
                curr = curr.se()
            elif x == "sw":
                curr = curr.sw()
            steps.append(curr)
    print(calc_steps(curr, HexaPunt(0, 0)))
    print(len(steps))
    dist_steps = sorted(steps, key=lambda x: x.euclidian_distance(HexaPunt(0, 0)), reverse= True)
    max_ = 0
    for x in dist_steps:
        test = calc_steps(x, HexaPunt(0, 0))
        if test > max_:
            max_ = test
            print(x, test)
main()
