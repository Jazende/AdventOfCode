with open('input_18.txt', 'r') as f:
    raw_inputs = f.read()

raw_inputs = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''

def print_walls(walls):
    min_x = min(key[0] for key in walls.keys())
    max_x = max(key[0] for key in walls.keys())
    min_y = min(key[1] for key in walls.keys())
    max_y = max(key[1] for key in walls.keys())

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in walls:
                print('#', end='')
            else:
                print('.', end='')
        print('')

########################## DAY 18 PART 1 ########################## 

walls = {}
position = (0, 0) # Col, Row

for instruction in raw_inputs.strip().split('\n'):
    direction, count, color = instruction.split(' ')
    for i in range(int(count)):
        if direction == 'R':
            position = (position[0] + 1, position[1])
        elif direction == 'D':
            position = (position[0], position[1] + 1)
        elif direction == 'L':
            position = (position[0] - 1, position[1])
        elif direction == 'U':
            position = (position[0], position[1] - 1)
        
        if position in walls:
            print(f'Position {position} in walls before | {instruction=}')
        walls[position] = '#'

# print_walls(walls)
# print('\n')

min_x = min(key[0] for key in walls.keys())
max_x = max(key[0] for key in walls.keys())
min_y = min(key[1] for key in walls.keys())
max_y = max(key[1] for key in walls.keys())
