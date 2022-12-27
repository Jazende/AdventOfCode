import re
from operator import attrgetter
import cProfile
from functools import partial

with open(r'22_15.txt', 'r') as f:
    raw_lines = f.read().strip()

row_to_check = y = 2_000_000
min_x = 0
max_x = 4_000_000
min_y = 0
max_y = 4_000_000

re_sensors = re.compile('Sensor at x=([0-9\-]+), y=([0-9\-]+): closest beacon is at x=([0-9\-]+), y=([0-9\-]+)')

# raw_lines = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3'''
# row_to_check = y = 10
# max_x = 20
# max_y = 20

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

    def bounds_on_height(self, height):
        vertical_distance   = abs(self.y - height)
        horizontal_distance = self.range - vertical_distance
        return (self.x - horizontal_distance), (self.x + horizontal_distance)

    def __repr__(self):
        return f'S@({self.x}, {self.y}):{self.range}'

sensors = [Sensor(*x) for x in re_sensors.findall(raw_lines)]
beacons = set((sensor.beacon_x, sensor.beacon_y) for sensor in sensors)

def calculate_invalid_locations(sensors, beacons, y):
    invalid_locations = set()
    for sensor in sensors:
        for invalid_loc in sensor.range_on_height(y):
            if (invalid_loc, y) in beacons:
                continue
            invalid_locations.add((invalid_loc, y))
    return invalid_locations

invalid_locations = calculate_invalid_locations(sensors, beacons, y)
print('Part 1: ', len(invalid_locations))

def find_valid_range(invalid_ranges):
    return invalid_ranges[0][1]+1

# def combine_two_ranges(range_one, range_two):
#     if range_one[0] <= range_two[0] <= range_one[1] and range_one[0] <= range_two[1] <= range_one[1]:
#         return (range_one[0], range_one[1])
#     elif range_two[0] <= range_one[1] + 1:
#         return (range_one[0], range_two[1])
#     return False

# def combine_ranges(ranges):
#     idx = 0
#     while True:
#         if len(ranges) < 2 or idx + 1 >= len(ranges):
#             break
#         if new_range := combine_two_ranges(*ranges[idx:idx+2]):
#             ranges.pop(idx+1)
#             ranges.pop(idx)
#             ranges.insert(idx, new_range)
#             idx = 0
#         else:
#             idx += 1
#     return ranges

def combine_ranges(ranges):
    idx = 0
    while True:
        if len(ranges) < 2 or idx + 1 >= len(ranges):
            break
        if ranges[idx][0] <= ranges[idx+1][0] <= ranges[idx][1] and ranges[idx][0] <= ranges[idx+1][1] <= ranges[0][1]:
            ranges.pop(idx+1)
            idx = 0
        elif ranges[idx+1][0] <= ranges[idx][1] + 1:
            ranges[idx] = (ranges[idx][0], ranges[idx+1][1])
            ranges.pop(idx+1)
            idx = 0
        else:
            idx += 1
    return ranges

def _bounded_range(range_, lower_bound, upper_bound):
    low, high = range_
    low = max(lower_bound, low)
    high = min(upper_bound, high)
    return (low, high)

bounded_range = partial(_bounded_range, lower_bound=min_x, upper_bound=max_x)

def invalid_locations_at_height(sensors, beacons, y):
    raw_ranges = []
    for sensor in sensors:
        left_bound, right_bound = sensor.bounds_on_height(y)
        if left_bound >= right_bound:
            continue
        raw_ranges.append((left_bound, right_bound))
    raw_ranges.sort()

    combined_ranges = combine_ranges(raw_ranges)
    bounded_ranges = list(map(bounded_range, combined_ranges))
    return bounded_ranges

def find_valid_solutions(sensors, beacons, min_y, max_y):
    invalid_range_check = [(min_x, max_x)]
    for height in range(min_y, max_y):
        invalid_ranges = invalid_locations_at_height(sensors, beacons, height)
        if invalid_ranges == invalid_range_check:
            continue
        valid_range = find_valid_range(invalid_ranges)
        break
    return valid_range * 4_000_000 + height

# cProfile.run('find_valid_solutions(sensors, beacons, min_y, max_y)')
solutions = find_valid_solutions(sensors, beacons, min_y, max_y)
print('Part 2: ', solutions)
