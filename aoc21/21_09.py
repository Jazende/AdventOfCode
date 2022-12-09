with open(r'input_09.txt', 'r') as f:
    raw_inputs = f.read().strip()

# raw_inputs =  '''
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678'''

inputs = {}
for y, line in enumerate(raw_inputs.strip().split('\n')):
    for x, row in enumerate(line):
        inputs[(x, y)] = int(row)

lows = []
for location, height in inputs.items():
    x, y = location
    lowest = True
    for check in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if not check in inputs:
            continue
        if inputs[check] <= height:
            lowest = False
            break
    if lowest:
        lows.append(height)

print(sum(lows)+len(lows))

sizes = []
for location, height in inputs.items():
    if height == 9:
        continue
    count = 0
    x, y = location
    additionals = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    cur_idx = -1
    while True:
        cur_idx += 1
        if cur_idx == len(additionals):
            break
        if not additionals[cur_idx] in inputs:
            continue
        if inputs[additionals[cur_idx]] < 9:
            count += 1
            inputs[additionals[cur_idx]] = 9
            new_x = additionals[cur_idx][0]
            new_y = additionals[cur_idx][1]
            for check in [(new_x-1, new_y), (new_x+1, new_y), (new_x, new_y-1), (new_x, new_y+1)]:
                if not check in additionals:
                    additionals.append(check)

    sizes.append(count)
sizes.sort(reverse=True)

print(sizes)
print(sizes[:3], sizes[0] * sizes[1] * sizes[2])