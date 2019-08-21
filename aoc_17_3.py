from itertools import cycle
import cProfile

class Punt:
    def __init__(self, x, y, value=None):
        self.x = x
        self.y = y
        self.value = value

    def manhattan_distance(self, other):
        return abs(self.x-other.x) + abs(self.y-other.y)

    def get_directions(self):
        directions = []
        if self.x > 0:
            directions.append(Punt(self.x-1, self.y))
        elif self.x < 0:
            directions.append(Punt(self.x+1, self.y))
        if self.y > 0:
            directions.append(Punt(self.x, self.y-1))
        elif self.y < 0:
            directions.append(Punt(self.x, self.y+1))
        return directions

    def get_best_direction(self):
        directions = self.get_directions()
        return max(directions, key=lambda x: self.manhattan_distance(x))

    def __repr__(self):
        if self.value:
            return "x: {}, y: {}, v: {}".format(self.x, self.y, self.value)
        else:
            return "x: {}, y: {}".format(self.x, self.y)

    def __eq__(self, other):
        if self.manhattan_distance(other) == 0:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        if type(other)==tuple or type(other)==list:
            if len(other)==2:
                return Punt(self.x + other[0], self.y+other[1])
                

def spiral(start_point):
    cur_point = start_point
    steps = 0
    while True:
        print(cur_point)
        if cur_point == Punt(0, 0):
            print(steps)
            break
        cur_point = cur_point.get_best_direction()
        steps += 1

def spiral_side(max_):
    cur_side = 1
    value = 1
    #print("{}x{}: {}".format(cur_side, cur_side, value))
    while value < max_:
        cur_side += 1
        value += cur_side*2 -1
        #print("{}x{}: {}".format(cur_side, cur_side, value))
    return cur_side, value

def name_unknown(value):
    side, val = spiral_side(value)
    diff = val-value
    if side % 2 == 0:
        x = ((side/2)-1)*-1
        y = side/2
        # print("even:", x, y, side, diff)
        if diff >= side:
            x += side -1
            y -=(diff-side)+1
        else:
            x += diff     
    else:
        x = (side-1)/2
        y = ((side-1)/2)*-1
        #print("oneven:", x, y, side, diff)
        if diff >= side:
            x -= side-1
            y += (diff-side)+1
        else:
            x -= diff
    # print(value, "punt:", x, y)
    return int(x), int(y), value

def main(profile=False):
    if profile:
        cProfile.run("name_unknown(312051)")
    else:
        x, y, value = name_unknown(312051)
        spiral(Punt(x, y, value))


def part_two(input_):
    directions = [[-1, -1], [-1, 0], [-1, 1],
                  [0, -1], [0, 0], [0, 1],
                  [1, -1], [1, 0], [1, 1]]
    punten = [Punt(0, 0, 1)]
    count = 2
    while True:
        x, y, _ = name_unknown(count)
        #print("test: ", x, y)
        result = 0
        for dir_ in directions:
            new_x = x+dir_[0]
            new_y = y+dir_[1]
            if Punt(new_x, new_y) in punten:
              #  print(punten[punten.index(Punt(new_x, new_y))].value)
                result += punten[punten.index(Punt(new_x, new_y))].value
        #print(result)
        punten.append(Punt(x, y, result))
        #print(punten)
        if result > input_:
            print(punten[len(punten)-1])
            break
        count += 1
