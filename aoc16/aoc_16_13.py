import heapq
import sys
import cProfile

test = {
    'designer_number': 10,
    'target_x': 7, 'target_y': 4,
    'size_x': 10, 'size_y': 10,
    'distance': 5,
}

real = {
    'designer_number': 1364,
    'target_x': 31, 'target_y': 39,
    'size_x': 51, 'size_y': 51,
    'distance': 50,
}

def geography(x, y, designer_number):
    calc = x*x + 3*x + 2*x*y + y + y*y + designer_number
    binary_string = str(bin(calc))[2:]
    count_ones = len(binary_string.replace('0', ''))
    location = "." if count_ones % 2 == 0 else "#"
    return location

def get_grid(size_x, size_y, designer_number):
    return {(x, y): geography(x, y, designer_number) for x in range(0, size_x+1) for y in range(0, size_y+1)}

def solutions(target_x, target_y, size_x, size_y, designer_number, distance):
    grid = {key: None for key, value in get_grid(size_x, size_y, designer_number).items() if value == "."}
    grid[(1, 1)] = 0
    while True:
        changed = 0

        for key, value in grid.items():
            if isinstance(value, int):
                continue

            x, y = key
            for adjecant in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if adjecant in grid.keys() and isinstance(grid[adjecant], int):
                    changed += 1
                    if grid[key] is None:
                        grid[key] = grid[adjecant] + 1
                    else:
                        grid[key] = min(grid[adjecant] + 1, grid[key])

        if changed == 0:
            break

    print("Day 1:", grid[(31, 39)])
    print("Day 2:", len([key for key, value in grid.items() if isinstance(value, int) and value <= distance]))

solutions(**real)
cProfile.run('solutions(**real)')