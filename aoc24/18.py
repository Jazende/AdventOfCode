import os
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

width, height, sim_bytes = 71, 71, 1024

# raw_inputs, width, height, sim_bytes = '''5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0''', 7, 7, 12

starting_position = (0, 0)
ending_position = (width-1, height-1)

### Part 1 ###

def print_map(map):
    for row in range(height):
        for col in range(width):
            if (col, row) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print('')

positions = { (int(x.split(',')[0]), int(x.split(',')[1])) for x in raw_inputs.strip().split('\n')[:sim_bytes] }

def path_finding(map_):
    # Path = (Current Position, Current Count)
    paths = [(starting_position, 0), ]

    min_paths = { 
        (col, row): (width * height) ** 2
        for row in range(height)
        for col in range(width)
    }

    count = 0
    while True:
        count += 1
        if len(paths) == 0:
            break

        position, cost = paths.pop(0)
        # print(position, cost, paths[:5])

        if min_paths[position] > cost:
            min_paths[position] = cost
        else:
            continue

        if position == ending_position:
            continue

        new_pos_right = (position[0] + 1, position[1])
        if not new_pos_right in map_ and new_pos_right in min_paths:
            new_path_right = (new_pos_right, cost + 1)
            paths.append(new_path_right)

        new_pos_left = (position[0] - 1, position[1])
        if not new_pos_left in map_ and new_pos_left in min_paths:
            new_path_left = (new_pos_left, cost + 1)
            paths.append(new_path_left)

        new_pos_down = (position[0], position[1] + 1)
        if not new_pos_down in map_ and new_pos_down in min_paths:
            new_path_down = (new_pos_down, cost + 1)
            paths.append(new_path_down)

        new_pos_up = (position[0], position[1] - 1)
        if not new_pos_up in map_ and new_pos_up in min_paths:
            new_path_up = (new_pos_up, cost + 1)
            paths.append(new_path_up)

        paths.sort(key=lambda x: 140 - x[0][0] - x[0][1] + x[1])
    return min_paths[ending_position]

shortest_path = path_finding(positions)

print(shortest_path)


### Part 2 ###

full_count = len(raw_inputs.strip().split('\n'))

check = 1024
check_increase = 1024
max_value = (width * height) ** 2
while True:
    positions = { (int(x.split(',')[0]), int(x.split(',')[1])) for x in raw_inputs.strip().split('\n')[:check] }
    result = path_finding(positions)

    if result < max_value:
        check += check_increase
    else:
        if check_increase == 1:
            print(raw_inputs.strip().split('\n')[:check][-1])
            break
        check -= check_increase
        check_increase //= 2
        check += check_increase
    