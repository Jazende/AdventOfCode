from collections import Counter
import time

with open(r'input_12.txt', 'r') as f:
    raw_inputs = f.read().strip()

# raw_inputs = '''start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end'''

# raw_inputs = '''dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc'''

# raw_inputs = '''fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW'''

inputs = [line.split('-') for line in raw_inputs.split('\n')]

connections = {}
for conn in inputs:
    left, right = conn
    if not left in connections:
        connections[left] = []
    if not right in connections:
        connections[right] = []
    connections[left].append(right)
    connections[right].append(left)

def is_lower(string):
    if string.lower() == string:
        return True
    return False

paths = [['start']]
idx = 0
while True:
    if idx == len(paths):
        break
    if paths[idx][-1] == 'end':
        idx += 1
        continue
    cur_path = paths.pop(idx)
    for connected in connections[cur_path[-1]]:
        if connected in ['start', 'end']:
            if connected == 'start':
                continue
        elif is_lower(connected) and connected in cur_path:
            continue
        paths.append(cur_path + [connected])

def double_small_used(path):
    small_ones = [part for part in path if is_lower(part) and not part in ['start', 'end']]
    for key, value in Counter(small_ones).items():
        if value == 2:
            return True
    return False

print('Day 1:', len(paths))

paths = [['start']]
idx = 0
while True:
    if idx == len(paths):
        break
    if paths[idx][-1] == 'end':
        idx += 1
        continue
    cur_path = paths.pop(idx)
    for connected in connections[cur_path[-1]]:
        if connected == 'start':
            continue
        elif connected == 'end':
            paths.append(cur_path + [connected])
        elif not is_lower(connected):
            paths.append(cur_path + [connected])
        elif is_lower(connected):
            if not connected in cur_path:
                paths.append(cur_path + [connected])
            else:
                if not double_small_used(cur_path):
                    paths.append(cur_path + [connected])
                else:
                    continue

print('Day 2:', len(paths))