import os
import time
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

### Part 1 ###

map_, inputs = raw_inputs.strip().split('\n\n')

full_map = {
    (col, row): letter
    for row, line in enumerate(map_.strip().split('\n'))
    for col, letter in enumerate(line)
}

def print_map():
    from itertools import count
    for row in count():
        for col in count():
            if (col, row) in full_map:
                print(full_map[(col, row)], end='')
            else:
                break
        if (row, 0) in full_map:
            print('')
        else:
            break

def move_block(cur_location, direction_x, direction_y):
    cur_icon = full_map[cur_location]
    new_location = (cur_location[0] + direction_x, cur_location[1] + direction_y)
    # print(f'Pushing from {cur_location} in direction: {direction_x} {direction_y}')
    if full_map[new_location] == '#':
        # print(f'Pushing against #, continue on next')
        return False
    elif full_map[new_location] == '.':
        # print(f'Pushing against ., swap locations')
        full_map[new_location] = cur_icon
        full_map[cur_location] = '.'
        return True
    elif full_map[new_location] == 'O':
        # print(f'Pushing against O, trying to push further')
        if move_block(new_location, direction_x, direction_y):
            # print(f'Succesfully pushed 0, moving further')
            full_map[new_location] = cur_icon
            full_map[cur_location] = '.'
            return True
        else:
            # print(f'Unsuccesfully pushed, not moving')
            return False

idx = -1
while True:
    idx += 1
    if idx == len(inputs):
        break
    # print(inputs[idx])
    cur_location = [key for key, value in full_map.items() if value == '@'][0]
    if inputs[idx] == '^':
        move_block(cur_location, 0, -1)
    elif inputs[idx] == '>':
        move_block(cur_location, 1, 0)
    elif inputs[idx] == 'v':
        move_block(cur_location, 0, 1)
    elif inputs[idx] == '<':
        move_block(cur_location, -1, 0)

print(sum(location[0] + location[1] * 100 for location, value in full_map.items() if value == 'O'))

### Part 2 ###

def duplicate(letter):
    if letter == '#':
        return '##'
    if letter == 'O':
        return '[]'
    if letter == '.':
        return '..'
    if letter == '@':
        return '@.'
    return letter

raw_inputs = ''.join(duplicate(letter) for letter in raw_inputs)

map_, inputs = raw_inputs.strip().split('\n\n')

full_map = {
    (col, row): letter
    for row, line in enumerate(map_.strip().split('\n'))
    for col, letter in enumerate(line)
}

def print_map():
    from itertools import count
    for row in count():
        for col in count():
            if (col, row) in full_map:
                print(full_map[(col, row)], end='')
            else:
                break
        if (0, row) in full_map:
            print('')
        else:
            break

def can_move_block(cur_location, direction_x, direction_y):
    cur_icon = full_map[cur_location]
    new_location = (cur_location[0] + direction_x, cur_location[1] + direction_y)
    if full_map[new_location] == '#':
        return False
    elif full_map[new_location] == '.':
        return True
    elif direction_y == 0 and (full_map[new_location] == '[' or full_map[new_location] == ']'):
        if can_move_block(new_location, direction_x, direction_y):
            return True
        else:
            return False
    elif not direction_y == 0 and full_map[new_location] == '[':
        new_location_right = (new_location[0]+1, new_location[1])
        if can_move_block(new_location, direction_x, direction_y) and can_move_block(new_location_right, direction_x, direction_y):
            return True
        else:
            return False
    elif not direction_y == 0 and full_map[new_location] == ']':
        new_location_left = (new_location[0]-1, new_location[1])
        if can_move_block(new_location, direction_x, direction_y) and can_move_block(new_location_left, direction_x, direction_y):
            return True
        else:
            return False

def move_block(cur_location, direction_x, direction_y):
    cur_icon = full_map[cur_location]
    new_location = (cur_location[0] + direction_x, cur_location[1] + direction_y)
    if full_map[new_location] == '#':
        return False
    elif full_map[new_location] == '.':
        full_map[new_location] = cur_icon
        full_map[cur_location] = '.'
        return True
    elif direction_y == 0 and (full_map[new_location] == '[' or full_map[new_location] == ']'):
        if move_block(new_location, direction_x, direction_y):
            full_map[new_location] = cur_icon
            full_map[cur_location] = '.'
            return True
        else:
            return False
    elif not direction_y == 0 and full_map[new_location] == '[':
        new_location_right = (new_location[0]+1, new_location[1])
        if can_move_block(new_location, direction_x, direction_y) and can_move_block(new_location_right, direction_x, direction_y):
            move_block(new_location, direction_x, direction_y)
            move_block(new_location_right, direction_x, direction_y)
            full_map[new_location] = cur_icon
            full_map[cur_location] = '.'
            return True
        else:
            return False
    elif not direction_y == 0 and full_map[new_location] == ']':
        new_location_left = (new_location[0]-1, new_location[1])
        if can_move_block(new_location, direction_x, direction_y) and can_move_block(new_location_left, direction_x, direction_y):
            move_block(new_location, direction_x, direction_y)
            move_block(new_location_left, direction_x, direction_y)
            full_map[new_location] = cur_icon
            full_map[cur_location] = '.'
            return True
        else:
            return False

idx = -1
while True:
    idx += 1
    if idx == len(inputs):
        break
    # print(inputs[idx])
    cur_location = [key for key, value in full_map.items() if value == '@'][0]
    if inputs[idx] == '^':
        move_block(cur_location, 0, -1)
    elif inputs[idx] == '>':
        move_block(cur_location, 1, 0)
    elif inputs[idx] == 'v':
        move_block(cur_location, 0, 1)
    elif inputs[idx] == '<':
        move_block(cur_location, -1, 0)

print(sum(location[0] + location[1] * 100 for location, value in full_map.items() if value == '['))
