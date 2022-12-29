import cProfile
import re
from operator import attrgetter
from itertools import product, combinations, chain

with open(r'22_15.txt', 'r') as f:
    raw_lines = f.read().strip()

row_to_check = y = 2_000_000
min_x = 0
max_x = 4_000_000
min_y = 0
max_y = 4_000_000

re_sensors = re.compile('Sensor at x=([0-9\-]+), y=([0-9\-]+): closest beacon is at x=([0-9\-]+), y=([0-9\-]+)')

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

    # def inner_lines(self):
    #     print('-x {', self.x - self.range, '<= x <=', self.x, '} -', self.range, '+', self.x, '+', self.y)
    #     print('-x {', self.x, '<= x <=', self.x + self.range, '} +', self.range, '+', self.x, '+', self.y)
    #     print(' x {', self.x, '<= x <=', self.x + self.range, '} -', self.range, '-', self.x, '+', self.y)
    #     print(' x {', self.x - self.range, '<= x <=', self.x, '} +', self.range, '-', self.x, '+', self.y)

    # def outer_lines(self):
    #     print('-x {', self.x - (self.range + 1), '<= x <=', self.x, '} -', (self.range + 1), '+', self.x, '+', self.y)
    #     print('-x {', self.x, '<= x <=', self.x + (self.range + 1), '} +', (self.range + 1), '+', self.x, '+', self.y)
    #     print(' x {', self.x, '<= x <=', self.x + (self.range + 1), '} -', (self.range + 1), '-', self.x, '+', self.y)
    #     print(' x {', self.x - (self.range + 1), '<= x <=', self.x, '} +', (self.range + 1), '-', self.x, '+', self.y)

    def line_segments_up(self):
        return (
            {'offset': self.y - self.x - (self.range + 1), 'min': self.x, 'max': self.x + (self.range + 1)},
            {'offset': self.y - self.x + (self.range + 1), 'min': self.x - (self.range + 1), 'max': self.x},
        )

    def line_segments_down(self):
        return (
            {'offset': self.y + self.x - (self.range + 1), 'min': self.x - (self.range + 1), 'max': self.x},
            {'offset': self.y + self.x + (self.range + 1), 'min': self.x, 'max': self.x + (self.range + 1)}
        )

    def __repr__(self):
        return f'S@({self.x}, {self.y}):{self.range}'

sensors = [Sensor(*x) for x in re_sensors.findall(raw_lines)]
sensors.sort(key=attrgetter('x'))
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
print('Part 1:', len(invalid_locations))

##########################################################

def find_missing_beacon(sensors):
    points = set()
    for sensor_combination in combinations(sensors, 2):
        first_sensor, second_sensor = sensor_combination
        # Get a chain of first_up, second_down & second_up, first_down; this to always have first segment go up and second go down for calculations
        # Could be replaced by a double loop for clarity's sake
        for line_combo in chain(product(first_sensor.line_segments_up(), second_sensor.line_segments_down()), product(second_sensor.line_segments_up(), first_sensor.line_segments_down())):
            # offset_a = up, offset_b = down
            offset_a, offset_b = line_combo
            # x + a = -x + b -> x + x = b - a
            # 2x = b - a     -> x = (b - a) / 2

            double_point_of_contact = (offset_b['offset'] - offset_a['offset'])
            if not double_point_of_contact % 2 == 0:
                continue
            point_of_contact = double_point_of_contact / 2
            if not offset_a['min'] <= point_of_contact <= offset_a['max']:
                continue
            if not offset_b['min'] <= point_of_contact <= offset_b['max']:
                continue

            # x + slope_a = y                  || - x + slope_b = y
            # point_of_contact + slope_a = y   || - point_of_contact + slope_b = y
            height = point_of_contact + offset_a['offset']

            # check that both x and y are between 0 and max
            if not 0 <= point_of_contact <= max_x:
                continue
            if not 0 <= height <= max_y:
                continue
            points.add((int(point_of_contact), int(height)))

    for point in points:
        point_x, point_y = point
        if not any(manhattan_distance(point_x, point_y, sensor.x, sensor.y) <= sensor.range for sensor in sensors):
            return point_x * 4_000_000 + point_y

print('Part 2:', find_missing_beacon(sensors))
