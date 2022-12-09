from particle import Particle
from time import sleep
import re

PART2 = "adventofcode_20_test_2.txt"
TEST = "adventofcode_20_test.txt"
REAL = "adventofcode_20.txt"

RE_MATCH_VALUES = "^p=<\s?(?P<pos_x>-?\d{1,10}),(?P<pos_y>-?\d{1,10}),(?P<pos_z>-?\d{1,10})>, " + \
                  "v=<\s?(?P<vel_x>-?\d{1,10}),(?P<vel_y>-?\d{1,10}),(?P<vel_z>-?\d{1,10})>, " + \
                  "a=<\s?(?P<acc_x>-?\d{1,10}),(?P<acc_y>-?\d{1,10}),(?P<acc_z>-?\d{1,10})>$"

def load_file(file):
    res = []
    with open(file, "r") as f:
        for line in f:
            res.append(line.strip())
    return res

def parse_values(file):
    file_input = load_file(file)
    values = []
    for line in file_input:
        x = re.match(RE_MATCH_VALUES, line)
        values.append([x.group('pos_x'), x.group('pos_y'), x.group('pos_z'),
                       x.group('vel_x'), x.group('vel_y'), x.group('vel_z'),
                       x.group('acc_x'), x.group('acc_y'), x.group('acc_z')])
        
    return values

def calc_values(file):
    values = parse_values(file)
    closest = sorted(values, key=lambda x: int(x[6])**2+int(x[7])**2+int(x[8])**2)[0]
    return closest
    
def create_particles(file):
    values = parse_values(file)
    particles = []
    for x in values:
        particles.append(Particle(x[0], x[1], x[2], x[3], x[4],
                                  x[5], x[6], x[7], x[8]))
    return particles

def check_collisions(file):
    particles = create_particles(file)
    while len(particles)>1:
        for part in particles:
            part.tick()
        for part in particles:
            if part in particles:
                pass
        for part in particles[::-1]:
            if part.collided:
                particles.remove(part)
        print(len(particles), end="\t")
        
print(check_collisions(REAL))
