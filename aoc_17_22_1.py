clean = "."
size = 200

grid = {(x, y): False for y in range(-1*size, size+1) for x in range(-1*size, size+1)}

directions = [
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 0],
]
cur_pos = [0, 0]
cur_dir = [0, 1]

### Test Grid ###
# grid[(1, 1)] = True
# grid[(-1, 0)] = True

### Actual Grid ###
with open(r'aoc_17_22.txt', 'r') as f:
    raw_input = f.read().strip()
lines = raw_input.split("\n")
for idx_line, line in enumerate(lines[::-1]):
    for idx_char, char in enumerate(line):
        if char == "#":
            grid[(idx_char - len(line)//2, idx_line - len(lines)//2)] = True

def print_grid(grid):
    keys = sorted(grid.keys(), key=lambda x: x[1]*100*-1 + x[0])
    start_y = keys[0][1]
    index = 0
    while True:
        if True == False:
            pass
        # if keys[index] == (0, 0):
        #     print('0', end="")
        if keys[index] == tuple(cur_pos):
            print('C', end="")
        elif keys[index][1] == start_y:
            print([clean, 1][grid[keys[index]]], end="")
        else:
            print("\n", [clean, 1][grid[keys[index]]], sep="", end="")
            start_y = keys[index][1]
        index += 1
        if index == len(keys):
            break
    print("\n"*2)

bursts = 0
infection_bursts = 0
while True:
    if bursts >= 10000:
        break
    elif not tuple(cur_pos) in grid:
        print(cur_pos, "not in grid. Increase size.")
    elif grid[tuple(cur_pos)] == True:
        cur_dir = directions[(directions.index(cur_dir)-1) % len(directions)]
        grid[tuple(cur_pos)] = False
        cur_pos = [cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]]
    elif grid[tuple(cur_pos)] == False:
        cur_dir = directions[(directions.index(cur_dir)+1) % len(directions)]
        grid[tuple(cur_pos)] = True
        infection_bursts += 1
        cur_pos = [cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]]
    bursts += 1

print(infection_bursts)