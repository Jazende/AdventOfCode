with open('input_10.txt', 'r') as f:
    raw_inputs = f.read()


raw_inputs = '''
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
'''

# raw_inputs = '''
# ...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ...........
# '''

# raw_inputs = '''7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ'''

# raw_inputs = '''-L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF'''

########################## DAY 10 PREP 0 ########################## 
def connections(char):
    #        0, -1
    #  -1, 0   X   1, 0
    #        0,  1
    if char == '┘':
        return ( (-1,  0), ( 0, -1) )
    if char == '┌':
        return ( ( 1,  0), ( 0,  1) )
    if char == '└':
        return ( ( 1,  0), ( 0, -1) )
    if char == '┐':
        return ( (-1,  0), ( 0,  1) )
    if char == '│':
        return ( ( 0, -1), ( 0,  1) )
    if char == '─':
        return ( (-1,  0), ( 1,  0) )
    if char == 'S':
        return ( ( 0, -1), ( 0,  1), (-1,  0), ( 1,  0) )
    if char == '.':
        return ( )

def add_locations(first, second):
    return (first[0] + second[0], first[1] + second[1])

def reverse_location(loc):
    return (loc[0] * -1, loc[1] * -1)

inputs = [line.replace('J', '┘').replace('F', '┌').replace('7', '┐').replace('L', '└').replace('-', '─').replace('|', '│') for line in raw_inputs.strip().split('\n')]
pipes = { (col, row): {'char': char, 'raw_connections': connections(char), 'connections': []} for row, line in enumerate(inputs) for col, char in enumerate(line) }

for pipe in pipes:
    conns = pipes[pipe]['raw_connections']
    for conn in conns:
        adj_location = add_locations(pipe, conn)
        opposite = reverse_location(conn)

        if adj_location in pipes and opposite in pipes[adj_location]['raw_connections']:
            pipes[pipe]['connections'].append(adj_location)

start = [pipe for pipe in pipes if pipes[pipe]['char'] == 'S'][0]

########################## DAY 10 PART 1 ########################## 
circle = [start, ]
current_position = start
while True:
    try:
        next_position = [position for position in pipes[current_position]['connections'] if not position in circle][0]
    except IndexError:
        circle.append(circle[0])
        break
    circle.append(next_position)

    current_position = next_position

print('Part 1:', int(len(circle)/2))

########################## DAY 10 PART 2 ########################## 

min_col = min(pipe[0] for pipe in pipes.keys())
max_col = max(pipe[0] for pipe in pipes.keys())
min_row = min(pipe[1] for pipe in pipes.keys())
max_row = max(pipe[1] for pipe in pipes.keys())

# ┌┐│─
# └┘

print(*inputs, sep='\n')