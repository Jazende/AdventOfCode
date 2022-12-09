states = {'clean': '.', 'weak': 'W', 'infect': '#', 'flag': 'F'}
size = 20

grid = {(x, y): 'clean' for y in range(-1*size, size+1) for x in range(-1*size, size+1)}

directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]
cur_pos = [0, 0]
cur_dir = [0, 1]

### Test Grid ###
# grid[(1, 1)] = 'infect'
# grid[(-1, 0)] = 'infect'

### Actual Grid ###
with open(r'aoc_17_22.txt', 'r') as f:
    raw_input = f.read().strip()
lines = raw_input.split("\n")
for idx_line, line in enumerate(lines[::-1]):
    for idx_char, char in enumerate(line):
        if char == "#":
            grid[(idx_char - len(line)//2, idx_line - len(lines)//2)] = 'infect'

def print_grid(grid):
    keys = sorted(grid.keys(), key=lambda x: x[1]*100*-1 + x[0])
    start_y = keys[0][1]
    index = 0
    while True:
        if keys[index] == tuple(cur_pos):
            print('C', end="")
        elif keys[index][1] == start_y:
            print(states[grid[keys[index]]], end="")
        else:
            print("\n", states[grid[keys[index]]], sep="", end="")
            start_y = keys[index][1]
        index += 1
        if index == len(keys):
            break
    print("\n"*2)

print_grid(grid)

bursts = 0
infection_bursts = 0
while True:
    if bursts >= 10000000:
        break
    elif not tuple(cur_pos) in grid:
        grid[tuple(cur_pos)] = 'clean'
        continue
    elif grid[tuple(cur_pos)] == 'infect':
        cur_dir = directions[(directions.index(cur_dir)+3) % len(directions)]
        grid[tuple(cur_pos)] = 'flag'
    elif grid[tuple(cur_pos)] == 'flag':
        cur_dir = directions[(directions.index(cur_dir)+2) % len(directions)]
        grid[tuple(cur_pos)] = 'clean'
    elif grid[tuple(cur_pos)] == 'clean':
        cur_dir = directions[(directions.index(cur_dir)+1) % len(directions)]
        grid[tuple(cur_pos)] = 'weak'
    elif grid[tuple(cur_pos)] == 'weak':
        cur_dir = directions[(directions.index(cur_dir)+0) % len(directions)]
        grid[tuple(cur_pos)] = 'infect'
        infection_bursts += 1

    cur_pos = [cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]]
    bursts += 1

# print_grid(grid)
print(infection_bursts)