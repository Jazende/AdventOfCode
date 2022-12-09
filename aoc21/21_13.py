with open(r'input_13.txt', 'r') as f:
    raw_inputs = f.read().strip()

# raw_inputs = '''6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5'''

raw_inputs, raw_folds = raw_inputs.split('\n\n')
inputs = [[int(x) for x in part.split(',')] for part in raw_inputs.split('\n')]
folds = [part.split(' ')[-1].split('=')[0::1] for part in raw_folds.split('\n')]

for idx, fold in enumerate(folds):
    orientation, line = fold

    if orientation == 'x':
        nr_idx = 0
    if orientation == 'y':
        nr_idx = 1
    line_nr = int(line)
    
    for location in inputs:
        if location[nr_idx] > line_nr:
            location[nr_idx] = line_nr - (location[nr_idx] - line_nr)

    if idx == 0:
        print('Day 1:', len(set(tuple(loc) for loc in inputs)))

min_x = min(part[0] for part in inputs)
max_x = max(part[0] for part in inputs)
min_y = min(part[1] for part in inputs)
max_y = max(part[1] for part in inputs)

print('Day 2:')
for y in range(min_y, max_y + 1):
    print(f'{y:>2}', end=" ")
    for x in range(min_x, max_x + 1):
        if [x, y] in inputs:
            print('#', end='')
        else:
            print('.', end='')
    print('')
