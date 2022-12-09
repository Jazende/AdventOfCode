import cProfile

def fuel_cell_level(x, y, grid_serial):
    power_level = ((((((x + 10) * y) + grid_serial) * (x + 10)) % 1000) // 100) - 5 
    return power_level

def check_max(max_sum, max_loc, sum_, x, y, size):
    if sum_ > max_sum:
        max_sum = sum_
        max_loc = (x, y, size)
    return max_sum, max_loc

def solutions(grid_serial, day=1):
    #               Naive: 82359030040
    # adjust_sum_per line:  2034022550 => 2.4%
    #  start_sum per line:  1367849353 => 1.6% ( => 67.0%)
    grid = {(x, y): fuel_cell_level(x, y, grid_serial) for y in range(1, 301) for x in range(1, 301)}

    max_sum = 0
    max_loc = None

    if day == 1:
        min_size = 3
        max_size = 3
    else:
        min_size = 14
        max_size = 18

    for size in range(min_size, max_size+1):
        size_sum = 0
        for size_y in range(size):
            for size_x in range(size):
                size_sum += grid[(1 + size_x, 1 + size_y)]

        max_sum, max_loc = check_max(max_sum, max_loc, size_sum, 1, 1, size)

        for y in range(2, 302 - size):
            for x in range(size):
                size_sum -= grid[(x+1, y-1)]
                size_sum += grid[(x+1, y+size-1)]

            max_sum, max_loc = check_max(max_sum, max_loc, size_sum, 1, y, size)

            new_sum = size_sum + 0
            for x in range(2, 302 - size):
                for size_y in range(size):
                    new_sum -= grid[(x-1, y+size_y)]
                    new_sum += grid[(x+size-1, y+size_y)]
            
                max_sum, max_loc = check_max(max_sum, max_loc, new_sum, x, y, size)

    return (max_loc, max_sum)

print(solutions(3031, day=1))
print(solutions(3031, day=2))