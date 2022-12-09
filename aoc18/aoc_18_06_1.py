from collections import Counter
import sys

def print_grid(grid):
    global grid_min
    global grid_max

    for y in range(grid_min, grid_max+1):
        for x in range(grid_min, grid_max+1):
            print(grid[(x, y)], end="")
        print("")

def manhattan_distance(punt_1_x, punt_1_y, punt_2_x, punt_2_y):
    return manhattan_distance_points([punt_1_x, punt_2_x], [punt_1_y, punt_2_y])

def manhattan_distance_points(source_points, target_points):
    dist = 0
    for values in list(zip(source_points, target_points)):
        dist += abs(values[0]-values[1])
    return dist

def create_grid():
    grid = {(x, y): "." for x in range(grid_min, grid_max+1) for y in range(grid_min, grid_max+1)}
    for key, value in grid_starts.items():
        grid[key] = value[0]
    return grid

def fill_grid(grid):
    for key in grid.keys():
        if not grid[key] == ".":
            continue

        all_distances = [manhattan_distance_points(key, target) for target in grid_starts.keys()]
        min_dist = min(all_distances)

        if all_distances.count(min_dist) > 1:
            grid[key] = " "
            continue
        
        for idx, distance in enumerate(all_distances):
            if distance == min_dist:
                try:
                    grid[key] = [value[0] for value in grid_starts.values() if value[1] == idx][0]
                except IndexError:
                    continue
                else:
                    break

def grow_grid(grid, diff):
    global grid_min
    global grid_max
    
    # /-----------\
    # | A | B | C |
    # |---|---|---|
    # | D | E | F |
    # |---|---|---|
    # | G | H | I |
    # \-----------/

    cur_min = grid_min
    cur_max = grid_max
    new_min = cur_min - diff
    new_max = cur_max + diff

    for y in range(new_min, new_max+1):
        for x in range(new_min, new_max+1):
            if (x, y) in grid.keys():
                continue
            # if cur_min <= x <= cur_max and cur_min <= y <= cur_max:
            #     continue
            grid[(x, y)] = "."

    grid_min = new_min
    grid_max = new_max

def current_sizes(grid):
    print(sorted([(key, value) for key, value in Counter([value.lower() for value in grid.values() if not value == "." and not value == " "]).items()]))

grid_min = 0
grid_max = 400

# grid_starts = {(1, 1): ("A", 0), (1, 6): ("B", 1), (8, 3): ("C", 2), (3, 4): ("D", 3), (5, 5): ("E", 4), (8, 9): ("F", 5)}
grid_starts = {
    (300, 90): ("A", 0), 
    (300, 60): ("B", 1), 
    (176, 327): ("C", 2),
    (108, 204): ("D", 4), 
    (297, 303): ("E", 5), 
    (101, 236): ("F", 6), 
    (70, 102): ("G", 7), 
    (336, 153): ("H", 8), 
    (260, 265): ("I", 9), 
    (228, 221): ("J", 10), 
    (119, 267): ("K", 11), 
    (310, 302): ("L", 12), 
    (291, 164): ("M", 13), 
    (190, 202): ("N", 14), 
    (298, 228): ("O", 15), 
    (292, 262): ("P", 16), 
    (53, 251): ("Q", 17), 
    (176, 64): ("R", 18), 
    (170, 160): ("S", 19), 
    (71, 42): ("T", 20), 
    (314, 51): ("U", 21), 
    (71, 88): ("V", 22), 
    (319, 150): ("W", 23), 
    (192, 322): ("X", 24), 
    (270, 88): ("Y", 25), 
    (165, 203): ("Z", 26), 
    (262, 340): ("0", 27), 
    (301, 327): ("1", 28), 
    (135, 324): ("2", 29), 
    (97, 250): ("3", 30), 
    (161, 231): ("4", 31), 
    (305, 344): ("5", 32), 
    (295, 213): ("6", 33), 
    (320, 219): ("7", 34), 
    (172, 269): ("8", 35), 
    (151, 150): ("9", 36), 
    (215, 128): ("10", 37), 
    (167, 102): ("11", 38), 
    (158, 138): ("12", 39), 
    (307, 353): ("13", 40), 
    (358, 335): ("14", 41), 
    (163, 329): ("15", 42), 
    (234, 147): ("16", 43), 
    (58, 298): ("17", 44), 
    (228, 50): ("18", 45), 
    (151, 334): ("19", 46), 
    (108, 176): ("20", 47), 
    (335, 235): ("21", 48), 
    (296, 263): ("22", 49), 
    (80, 233): ("23", 50), 
}

grid = create_grid()
fill_grid(grid)
current_sizes(grid)

grow_grid(grid, 30)
fill_grid(grid)
current_sizes(grid)
