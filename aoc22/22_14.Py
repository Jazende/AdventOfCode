with open(r'22_14.txt', 'r') as f:
    raw_lines = f.read().strip()

SOLID_ROCK  = '#'
EMPTY_SPACE = '.'
SAND        = 's'

def translate_inputs(raw_lines):
    partitions   = [line.split(' -> ') for line in raw_lines.split('\n')]
    # Each line segment of rocks
    raw_segments = [partition[idx:idx+2] for partition in partitions for idx in range(len(partition)-1)]
    segments = []

    for raw_segment in raw_segments:
        first, second = raw_segment
        first_x, first_y = first.split(',')
        second_x, second_y = second.split(',')

        start_x = min(int(first_x), int(second_x))
        end_x   = max(int(first_x), int(second_x))
        start_y = min(int(first_y), int(second_y))
        end_y   = max(int(first_y), int(second_y))

        segments.append([start_x, end_x, start_y, end_y])
    return segments

def make_rock_wall(segments):
    min_x, min_y = 10_000, 0
    max_x, max_y = 0, 0

    rock_wall = {}
    for segment in segments:
        start_x, end_x, start_y, end_y = segment
        if start_x == end_x:
            for y in range(start_y, end_y+1):
                rock_wall[(start_x, y)] = SOLID_ROCK
        elif start_y == end_y:
            for x in range(start_x, end_x+1):
                rock_wall[(x, end_y)] = SOLID_ROCK
        min_x = min(start_x, min_x)
        max_x = max(end_x, max_x)
        min_y = min(start_y, min_y)
        max_y = max(end_y, max_y)
    
    rock_wall['min_x'] = min_x
    rock_wall['min_y'] = min_y
    rock_wall['max_x'] = max_x
    rock_wall['max_y'] = max_y
    return rock_wall

def print_rock_wall(rock_wall):
    for x in range(rock_wall['min_x'], rock_wall['max_x']+1):
        if x % 3 == 2:
            print(str(x)[-1], end='')
        elif x == 499:
            print('[', end='')
        elif x == 501:
            print(']', end='')
        else:
            print(' ', end='')
    print(' ', x)

    for y in range(rock_wall['min_y'], rock_wall['max_y']+1):
        for x in range(rock_wall['min_x'], rock_wall['max_x']+1):
            if (x, y) in rock_wall:
                print(rock_wall[(x, y)], end='')
            else:
                print(EMPTY_SPACE, end='')
        print('')

def drop_sand(rock_wall, sand_origin):
    cur_loc = sand_origin
    while True:
        x, y = cur_loc
        # 1 down is empty, move cur_loc down and continue
        if rock_wall.get((x, y+1), EMPTY_SPACE) == EMPTY_SPACE:
            cur_loc = (x, y+1)

        # 1 down is rock, try left:
        elif rock_wall.get((x-1, y+1), EMPTY_SPACE) == EMPTY_SPACE:
            cur_loc = (x-1, y+1)

        # 1 down and left is rock, try right
        elif rock_wall.get((x+1, y+1), EMPTY_SPACE) == EMPTY_SPACE:
            cur_loc = (x+1, y+1)
        
        # All 3 are blocked, stop moving and return
        else:
            rock_wall[(x, y)] = 's'
            if (x, y) == sand_origin:
                return False
            break

        # If y keeps growing and goes beyond max_y: its freefalling into void
        if y >= rock_wall['max_y']:
            return False

    return True

def drop_all_sand(rock_wall, sand_origin):
    counter = 0
    while True:
        if drop_sand(rock_wall, sand_origin) == False:
            break
        counter += 1
    return counter

sand_origin = (500, 0)
segments = translate_inputs(raw_lines)

rock_wall = make_rock_wall(segments)
print('Part 1:', drop_all_sand(rock_wall, sand_origin))
# print_rock_wall(rock_wall)

### Part 2 ###
segments.append([335, 800, rock_wall['max_y']+2, rock_wall['max_y']+2])
rock_wall = make_rock_wall(segments)
print('Part 2:', drop_all_sand(rock_wall, sand_origin)+1)
# print_rock_wall(rock_wall)
