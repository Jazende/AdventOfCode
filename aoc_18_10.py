import re
import time

with open(r'aoc_18_10.txt', 'r') as f:
    raw_input = f.read()

class Beacon:
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def tick(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

    def __repr__(self):
        st = f"position=<{self.pos_x},{self.pos_y}> velocity=<{self.vel_x},{self.vel_y}>"
        return st

    @property
    def pos(self):
        return (self.pos_x, self.pos_y)

line = re.compile('position=\<([\-\s\d]+),([\-\s\d]+)> velocity=\<([\-\s\d]+),([\-\s\d]+)>')
inputs = [[int(x[0]), int(x[1]), int(x[2]), int(x[3])] for x in line.findall(raw_input.strip())]
beacons = [Beacon(*x) for x in inputs]

##cur_min_x = 1000
##cur_min_y = 1000
##count = 0
##while True:
##    min_x = min([b.pos_x for b in beacons])
##    min_y = min([b.pos_y for b in beacons])
##    max_x = max([b.pos_x for b in beacons])
##    max_y = max([b.pos_y for b in beacons])
##    dif_x = max_x - min_x
##    dif_y = max_y - min_y
##    if dif_x < cur_min_x:
##        cur_min_x = dif_x
##        print("x:", dif_x, count)
##    if dif_y < cur_min_y:
##        cur_min_y = dif_y
##        print("y:", dif_y, count)
##    for beacon in beacons:
##        beacon.tick()
##    count += 1
    
count = 0
while True:
    min_x = min([b.pos_x for b in beacons])
    min_y = min([b.pos_y for b in beacons])
    max_x = max([b.pos_x for b in beacons])
    max_y = max([b.pos_y for b in beacons])
    if max_y - min_y < 10 and max_x - min_x < 65:
        print(count)
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                pr = "."
                for beacon in beacons:
                    if beacon.pos == (x, y):
                        pr = "#"
                print(pr, end="")
            print("")
    for beacon in beacons:
        beacon.tick()
    count += 1
    
