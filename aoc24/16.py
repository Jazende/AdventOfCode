import os
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''
# ###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############'''

# raw_inputs = '''
# #################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################'''

mapping = {
    (col, row): letter
    for row, line in enumerate(raw_inputs.strip().split('\n'))
    for col, letter in enumerate(line)
}

directions = [(1, 0), (0, -1), (-1, 0), (0, 1), ]

### Part 1 ###

starting_position = [key for key, value in mapping.items() if value == 'S'][0]
ending_position = [key for key, value in mapping.items() if value == 'E'][0]

# Path = (Current Position, Current Direction, Path, Current Cost)
paths = [(starting_position, 0, '', 0), ]

count = 0
min_cost = None
best_paths = set()
min_paths = { (key, direction): None for key, value in mapping.items() for direction in range(4) if not value == '#' }
while True:
    if len(paths) == 0:
        break

    next_path = paths.pop(0)

    if min_paths[(next_path[0], next_path[1])] is None:
        min_paths[(next_path[0], next_path[1])] = next_path[3]

        test_left = (next_path[0], (next_path[1] + 1) % 4)
        if min_paths[test_left] is None or min_paths[test_left] > (next_path[3] + 1000):
            min_paths[test_left] = next_path[3] + 1000
        
        test_right = (next_path[0], (next_path[1] - 1) % 4)
        if min_paths[test_right] is None or min_paths[test_right] > (next_path[3] + 1000):
            min_paths[test_right] = next_path[3] + 1000

        test_turned_around = (next_path[0], (next_path[1] + 2) % 4)
        if min_paths[test_turned_around] is None or min_paths[test_turned_around] > (next_path[3] + 2000):
            min_paths[test_turned_around] = next_path[3] + 2000
    else:
        if min_paths[(next_path[0], next_path[1])] < next_path[3]:
            continue 

    if next_path[0] == ending_position:
        if min_cost is None or next_path[3] < min_cost:
            min_cost = next_path[3] if min_cost is None else min(min_cost, next_path[3])
            best_paths = set()
        if next_path[3] == min_cost:
            best_paths.add(next_path[2])
        continue
    if not min_cost is None and next_path[3] > min_cost:
        continue

    new_path_turn_left = (next_path[0], (next_path[1]+1) % 4, next_path[2] + 'L', next_path[3] + 1000)
    paths.append(new_path_turn_left)

    new_path_turn_right = (next_path[0], (next_path[1]-1) % 4, next_path[2] + 'R', next_path[3] + 1000)
    paths.append(new_path_turn_right)

    position_forward = (next_path[0][0] + directions[next_path[1]][0], next_path[0][1] + directions[next_path[1]][1])
    if position_forward in mapping and not mapping[position_forward] == "#":
        new_path_move_forward = (position_forward, next_path[1], next_path[2] + 'F', next_path[3] + 1)
        paths.append(new_path_move_forward)

    count += 1
    if count % 50 == 0:
        paths = [
            path 
            for path in paths 
            if not ( not min_paths[(path[0], path[1])] is None and min_paths[(path[0], path[1])] < path[3] )
        ]
        paths.sort(key=lambda x: x[3])

print(count, min_cost)

unique_locations = set()
unique_locations.add(starting_position)
for path in best_paths:
    location = starting_position
    direction = 0

    for input_ in path:
        if input_ == 'L':
            direction = (direction + 1) % 4
        if input_ == 'R':
            direction = (direction - 1) % 4
        if input_ == 'F':
            location = (location[0] + directions[direction][0], location[1] + directions[direction][1])
            unique_locations.add(location)
print(len(unique_locations))