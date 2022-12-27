import re
from operator import attrgetter

with open(r'22_15.txt', 'r') as f:
    raw_lines = f.read().strip()
row_to_check = y = 2_000_000

re_sensors = re.compile('Sensor at x=([0-9\-]+), y=([0-9\-]+): closest beacon is at x=([0-9\-]+), y=([0-9\-]+)')

raw_lines = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''
row_to_check = y = 10

def manhattan_distance(first_x, first_y, second_x, second_y):
    return abs(first_x - second_x) + abs(first_y - second_y)

class Sensor:
    def __init__(self, x, y, beacon_x, beacon_y):
        self.x = int(x)
        self.y = int(y)
        self.beacon_x = int(beacon_x)
        self.beacon_y = int(beacon_y)
        self.range    = manhattan_distance(self.x, self.y, self.beacon_x, self.beacon_y)
    
    def range_on_height(self, height):
        vertical_distance   = abs(self.y - height)
        horizontal_distance = self.range - vertical_distance
        return range(self.x - horizontal_distance, self.x + horizontal_distance+1)

    def __repr__(self):
        return f'S@({self.x}, {self.y}):{self.range}'

sensors = [Sensor(*x) for x in re_sensors.findall(raw_lines)]
beacons = set((sensor.beacon_x, sensor.beacon_y) for sensor in sensors)

valid_locations = set()
for sensor in sensors:
    for valid_loc in sensor.range_on_height(y):
        if (valid_loc, y) in beacons:
            continue
        valid_locations.add(valid_loc)

print('Part 1: ', len(valid_locations))
