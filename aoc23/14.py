with open('input_14.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....'''

########################## DAY 14 PART 1 ########################## 

def print_blocks(blocks):
    max_cols = max(key[0] for key in blocks.keys())
    max_rows = max(key[1] for key in blocks.keys())

    for row in range(max_rows+1):
        for col in range(max_cols+1):
            if (col, row) in blocks:
                print(blocks[(col, row)], end='')
            else:
                print('.', end='')
        print('')

def count_score(blocks, max_lines):
    # max_lines - key[1] (hoogte) voor elke rij waar value O is
    return sum(max_lines - key[1] for key, value in blocks.items() if value == 'O')

max_lines = len(raw_inputs.strip().split('\n'))
blocks = { 
    (char_idx, line_idx): '#' 
    for line_idx, line in enumerate(raw_inputs.strip().split('\n'))
    for char_idx, char in enumerate(line)
    if char == '#'
}

for line_idx, line in enumerate(raw_inputs.strip().split('\n')):
    for char_idx, char in enumerate(line):
        if char == 'O':
            # get keys on same line, lower line nr than current line_idx, and then take max, then add one
            possible_keys_line_values = [key[1] for key in blocks.keys() if key[0] == char_idx and key[1] <= line_idx]
            if len(possible_keys_line_values) > 0:
                blocks[(char_idx, max(possible_keys_line_values)+1)] = 'O'
            else:
                blocks[(char_idx, 0)] = 'O'

print(count_score(blocks, max_lines))

########################## DAY 14 PART 2 ########################## 

def count_boulder_score(boulders, max_lines):
    return sum(max_lines - boulder[1] for boulder in boulders)

def print_blocks_boulders(blocks, boulders):
    max_cols = max( max(key[0] for key in blocks.keys()), max(key[0] for key in boulders) ) + 1
    max_rows = max( max(key[1] for key in blocks.keys()), max(key[1] for key in boulders) ) + 1

    for row in range(max_rows):
        for col in range(max_cols):
            if (col, row) in blocks:
                print(blocks[(col, row)], end='')
            elif (col, row) in boulders:
                print('O', end='')
            else:
                print('.', end='')
        print('')

rows = len(raw_inputs.strip().split('\n'))
cols = len(raw_inputs.strip().split('\n')[0])

all_blocks = { 
    (char_idx, line_idx): char 
    for line_idx, line in enumerate(raw_inputs.strip().split('\n'))
    for char_idx, char in enumerate(line)
    if char == '#' or char == 'O'
}

blocks = { key: value for key, value in all_blocks.items() if value == '#'}
boulders =  [key for key, value in all_blocks.items() if value == 'O']

def roll_north(blocks, boulders, rows, cols):
    # x[1] / row zo klein mogelijk
    boulders.sort(key=lambda x: x[1])
    new_boulders = []
    for boulder in boulders:
        col, row = boulder
        while True:
            if (col, row-1) in blocks or (col, row-1) in new_boulders or row == 0:
                new_boulders.append( (col, row) )
                break
            row -= 1
    return new_boulders

def roll_west(blocks, boulders, rows, cols):
    # x[0] / col zo klein mogelijk
    boulders.sort(key=lambda x: x[0])
    new_boulders = []
    for boulder in boulders:
        col, row = boulder
        while True:
            if (col-1, row) in blocks or (col-1, row) in new_boulders or col == 0:
                new_boulders.append( (col, row) )
                break
            col -= 1
    return new_boulders

def roll_south(blocks, boulders, rows, cols):
    # x[1] / row zo groot mogelijk
    boulders.sort(key=lambda x: x[1], reverse=True)
    new_boulders = []
    for boulder in boulders:
        col, row = boulder
        while True:
            if (col, row+1) in blocks or (col, row+1) in new_boulders or row == rows-1:
                new_boulders.append( (col, row) )
                break
            row += 1
    return new_boulders

def roll_east(blocks, boulders, rows, cols):
    # x[0] / col zo groot mogelijk
    boulders.sort(key=lambda x: x[0], reverse=True)
    new_boulders = []
    for boulder in boulders:
        col, row = boulder
        while True:
            if (col+1, row) in blocks or (col+1, row) in new_boulders or col == cols-1:
                new_boulders.append( (col, row) )
                break
            col += 1
    return new_boulders

boulder_hashes = [set(boulders)]

target = 1_000_000_000
cycle_start = None
cycle_end = None
while True:
    boulders = roll_north(blocks, boulders, rows, cols)
    boulders = roll_west(blocks, boulders, rows, cols)
    boulders = roll_south(blocks, boulders, rows, cols)
    boulders = roll_east(blocks, boulders, rows, cols)

    new_hash = set(boulders)
    if new_hash in boulder_hashes:
        cycle_start = boulder_hashes.index(new_hash)
        cycle_end = len(boulder_hashes)
        print(f'Copy found of hash {cycle_start} at {cycle_end=}.')
        print(f'Cycle lenght: {cycle_end - cycle_start}')
        break
    boulder_hashes.append(new_hash)

# Boulders cycle from {cycle_start} to {cycle_end}
# print(f'{target=} -= {cycle_start=}')
target -= cycle_start
# print(f'{target=} %= {(cycle_end - cycle_start)=}')
target %= (cycle_end - cycle_start)
# print(target)

print(count_boulder_score(boulder_hashes[cycle_start + target], max_lines))
