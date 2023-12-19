import re
from itertools import cycle
from math import gcd

with open('input_08.txt', 'r') as f:
    raw_inputs = f.read()

re_connections = re.compile('(?P<node>[0-9A-Z]{3})\s=\s\((?P<left>[0-9A-Z]{3}), (?P<right>[0-9A-Z]{3})\)$')

# raw_inputs = '''RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)'''

# raw_inputs = '''LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)'''

raw_steps = raw_inputs.strip().split('\n')[0]
raw_lines = raw_inputs.strip().split('\n')[2:]

raw_connections = [re_connections.match(x).groups() for x in raw_lines]
connections = { x[0]: {'L': x[1], 'R': x[2]} for x in raw_connections}

########################## DAY 8 PART 1 ########################## 

position = 'AAA'
steps = 0
for instruction in cycle(raw_steps):
    position = connections[position][instruction]
    steps += 1
    if position == 'ZZZ':
        break
print(steps)

########################## DAY 8 PART 2 ########################## 

positions = [ node for node in connections.keys() if node.endswith('A') ]
steps = []

# voor elke start-positie check de cyclus tijd
# origineel had hier ook cyclus tijd na op "Z" uit te komen, maar kwam op zelfde neer als OG tijd
for node in positions:
    new_pos = node
    node_steps = 0
    cycle_steps = 0
    for instruction in cycle(raw_steps):
        new_pos = connections[new_pos][instruction]
        node_steps += 1
        if new_pos.endswith('Z'):
            break
    steps.append( node_steps )

# GGD van de steps
max_gcd = 0
for i in range(len(steps)-1):
    max_gcd = max(gcd(steps[i], steps[i+1]), max_gcd)
divided = [int(step / max_gcd) for step in steps]

# overschot na delen door GGD met elkaar vermenigvuldigen
result = 1
for div in divided:
    result *= div

# en terug * ggd om aan uitkomst te komen
result *= max_gcd
print(result)