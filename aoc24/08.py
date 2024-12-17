import os
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............'''

### Part 1 ###

inputs = {}
max_col = 0
max_row = 0
for row, line in enumerate(raw_inputs.strip().split('\n')):
    for col, letter in enumerate(line):
        if not letter in inputs.keys():
            inputs[letter] = []
        inputs[letter].append((col, row))
        max_col = max(max_col, col)
    max_row = max(max_row, row)

antinodes = set()
for frequency, locations in inputs.items():
    if frequency == '.':
        continue
    for location_1 in locations:
        for location_2 in locations:
            if location_1 == location_2:
                continue

            delta_col = location_2[0] - location_1[0]
            delta_row = location_2[1] - location_1[1]

            possible_antinodes = [
                (location_1[0] -      delta_col,  location_1[1] -      delta_row),
                (location_2[0] +      delta_col,  location_2[1] +      delta_row),
            ]

            for node in possible_antinodes:
                if 0 <= node[0] <= max_col and 0 <= node[1] <= max_row:
                    antinodes.add(node)

print(len(antinodes))

### Part 2 ###

for frequency, locations in inputs.items():
    if frequency == '.':
        continue
    for location_1 in locations:
        antinodes.add(location_1)
        for location_2 in locations:
            if location_1 == location_2:
                continue
        
            delta_col = location_2[0] - location_1[0]
            delta_row = location_2[1] - location_1[1]

            ## Going 'left'
            left_position = location_1
            while True:
                left_position = (left_position[0] - delta_col, left_position[1] - delta_row)
                if 0 <= left_position[0] <= max_col and 0 <= left_position[1] <= max_row:
                    antinodes.add(left_position)
                else:
                    break
            
            ## Going 'right'
            right_position = location_2
            while True:
                right_position = (right_position[0] + delta_col, right_position[1] + delta_row)
                if 0 <= right_position[0] <= max_col and 0 <= right_position[1] <= max_row:
                    antinodes.add(right_position)
                else:
                    break

print(len(antinodes))