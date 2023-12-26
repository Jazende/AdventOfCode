with open('input_16.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = r'''.|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|....'''

########################## DAY 16 PART 1 ########################## 

def lit_tiles(raw_inputs, starting_position_x, starting_position_y, starting_direction_x, starting_direction_y):
    positions = { 
        (col_idx, row_idx): { 
            'energized': False, 'char': char, 
            (0, -1): False, (0, 1): False, # Down, Up 
            (-1, 0): False, (1, 0): False, # Left, Right
        } 
        for row_idx, line in enumerate(raw_inputs.strip().split('\n')) 
        for col_idx, char in enumerate(line) 
    }

    rows = max(key[1] for key in positions.keys())
    cols = max(key[0] for key in positions.keys())

    beams = [(starting_position_x, starting_position_y, starting_direction_x, starting_direction_y)]
    beams_idx = 0

    while True:
        if beams_idx == len(beams):
            break

        current_beam = beams[beams_idx]

        old_position_col, old_position_row, adjustment_col, adjustment_row = current_beam
        new_position = (old_position_col + adjustment_col, old_position_row + adjustment_row)

        if new_position[0] < 0 or new_position[0] > cols:
            beams_idx += 1
            continue
        if new_position[1] < 0 or new_position[1] > rows:
            beams_idx += 1
            continue

        positions[(new_position)]['energized'] = True

        # If a beam already came up to this point from this direction: Stop
        if not positions[(new_position)][(adjustment_col, adjustment_row)]:
            positions[(new_position)][(adjustment_col, adjustment_row)] = True
        else:
            beams_idx += 1
            continue

        new_char = positions[(new_position)]['char']

        if new_char == '.':
            beams.append( (new_position[0], new_position[1], adjustment_col, adjustment_row) )
        elif new_char == '|':
            if abs(adjustment_col) == 1:
                beams.append( (new_position[0], new_position[1], 0, -1 ) )
                beams.append( (new_position[0], new_position[1], 0,  1) )
            else:
                beams.append( (new_position[0], new_position[1], adjustment_col, adjustment_row) )
        elif new_char == '-':
            if abs(adjustment_row) == 1:
                beams.append( (new_position[0], new_position[1], -1, 0) )
                beams.append( (new_position[0], new_position[1],  1, 0) )
            else:
                beams.append( (new_position[0], new_position[1], adjustment_col, adjustment_row) )
        elif new_char == '/': 
            if (adjustment_col, adjustment_row) == (0, 1):
                beams.append( (new_position[0], new_position[1], -1,  0) )
            elif (adjustment_col, adjustment_row) == (0, -1):
                beams.append( (new_position[0], new_position[1],  1,  0) )
            elif (adjustment_col, adjustment_row) == (1, 0):
                beams.append( (new_position[0], new_position[1],  0, -1) )
            elif (adjustment_col, adjustment_row) == (-1, 0):
                beams.append( (new_position[0], new_position[1],  0,  1) )
        elif new_char == '\\':
            if (adjustment_col, adjustment_row) == (0, 1):
                beams.append( (new_position[0], new_position[1],  1,  0) )
            if (adjustment_col, adjustment_row) == (0, -1):
                beams.append( (new_position[0], new_position[1], -1,  0) )
            if (adjustment_col, adjustment_row) == (1, 0):
                beams.append( (new_position[0], new_position[1],  0,  1) )
            if (adjustment_col, adjustment_row) == (-1, 0):
                beams.append( (new_position[0], new_position[1],  0, -1) )
        beams_idx += 1

    return sum(1 for key, value in positions.items() if value['energized'] == True)

print(lit_tiles(raw_inputs, -1, 0, 1, 0))

########################## DAY 16 PART 2 ########################## 

rows = len(raw_inputs.strip().split('\n'))
cols = len(raw_inputs.strip().split('\n')[0])

max_tiles = 0
for idx in range(rows):
    max_tiles = max(max_tiles, lit_tiles(raw_inputs, -1, idx, 1, 0))
    max_tiles = max(max_tiles, lit_tiles(raw_inputs, rows, idx, -1, 0))

for idx in range(cols):
    max_tiles = max(max_tiles, lit_tiles(raw_inputs, idx, -1, 0, 1))
    max_tiles = max(max_tiles, lit_tiles(raw_inputs, idx, cols, 0, -1))

print(max_tiles)
