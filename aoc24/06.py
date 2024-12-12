import os
import copy
import itertools
import time

with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...'''

def print_map(guard_map, special_positions=None):
    if not special_positions:
        special_positions = set()
    for row in itertools.count():
        for col in itertools.count():
            if not (col, row) in guard_map.keys():
                break
            if (col, row) in special_positions:
                print('!', end='')
            else:
                print(guard_map[(col, row)], end='')
        if not (0, row) in guard_map.keys():
            break
        print('')

guard_map = {
    (col, row): letter
    for row, line in enumerate(raw_inputs.strip().split('\n'))
    for col, letter in enumerate(line)
}

start_pos = [location for location, letter in guard_map.items() if letter in '^><v'][0]
guard_map[start_pos] = '.'

directions = [
    ( 0, -1), # ^ | UP
    ( 1,  0), # > | RIGHT
    ( 0,  1), # v | DOWN
    (-1,  0), # < | LEFT
]

### Part 1 ###

def walk_through(guard_map):
    direction_count = 0
    visited = set()

    guard_pos = tuple(start_pos)
    while True:
        ## Mark Guard Position as visited
        visited.add(guard_pos)
        ## Create Next Location
        next_pos = ( guard_pos[0] + directions[direction_count][0] , guard_pos[1] + directions[direction_count][1] )
        ## Check if next position is on the map, if not, stop:
        if not next_pos in guard_map.keys():
            break
        ## Check if next position is an obstacle, if it is, turn right and continue
        if guard_map[next_pos] == '#':
            direction_count = ( direction_count + 1 ) % 4
            continue
        ## Otherwise move Guard according to direction (guard letter)
        guard_pos = next_pos
    print(len(visited))
    return visited

visited_locations = walk_through(guard_map)

## Part 2 ##

def redirects_for_position(guard_map, position, direction_count):
    # For direction_count, 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT (see above)
    # Coming from = opposite of direction, next direction = -1 from coming from
    current_position = (
        position[0] + directions[(direction_count + 2) % 4][0], 
        position[1] + directions[(direction_count + 2) % 4][1]
    )

    while True:
        current_position = (
            current_position[0] + directions[(direction_count + 1) % 4][0], 
            current_position[1] + directions[(direction_count + 1) % 4][1]
        )
        if not current_position in guard_map.keys():
            return None
        if guard_map[current_position] == '#':
            return current_position

def find_obstacles(guard_map, position):
    return {
        '^': redirects_for_position(guard_map, position, 0),
        '>': redirects_for_position(guard_map, position, 1),
        'v': redirects_for_position(guard_map, position, 2),
        '<': redirects_for_position(guard_map, position, 3),
    }

obstacles = {
    position: find_obstacles(guard_map, position)
    for position, letter in guard_map.items()
    if letter == '#'
}

start_time = int(time.time() * 1_000)

count = 0
d = { 0: '^', 1: '>', 2: 'v', 3: '<' }

for visited in visited_locations:
    new_map = copy.copy(guard_map)
    new_map[visited] = '#'

    obstacles_copy = copy.copy(obstacles)

    obstacles_copy[visited] = find_obstacles(new_map, visited)
    for obstacle in obstacles_copy:
        if (visited[0] - 1 <= obstacle[0] <= visited[0] + 1) or \
            (visited[1] - 1 <= obstacle[1] <= visited[1] + 1):
            obstacles_copy[obstacle] = find_obstacles(new_map, obstacle)

    # Find First Position
    direction = 0
    position = start_pos
    while True:
        if position in obstacles_copy:
            break
        position = (position[0], position[1] - 1)

    cur_vis = set()
    cur_vis.add((position, direction))
    while True:
        position = obstacles_copy[position][d[direction]]
        direction = (direction + 1) % 4
        if position is None:
            break
        if (position, direction) in cur_vis:
            count += 1
            break
        cur_vis.add((position, direction))

print(count)
end_time = int(time.time() * 1_000)

print(f'{(end_time - start_time)/1000=}')
