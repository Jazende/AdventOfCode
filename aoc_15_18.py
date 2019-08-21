def load_grid(day, test):
    if not test:
        with open('aoc_15_18.txt', 'r') as f:
            raw = f.read()
    else:
        if day == 1:
            raw = """.#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####.."""
        elif day == 2:
            raw = """##.#.#\n...##.\n#....#\n..#...\n#.#..#\n####.#"""

    grid = {}

    for l_idx, line in enumerate(raw.strip().split("\n")):
        for c_idx, char in enumerate(line):
            grid[(c_idx, l_idx)] = 1 if char == "#" else 0

    size, corners = get_size_and_corners(grid)

    if day == 2:
        for key in corners:
            grid[key] = 1

    return grid, corners, size

def get_size_and_corners(grid):
    max_x = 0
    max_y = 0
    for key in grid.keys():
        max_x = max(max_x, key[0])
        max_y = max(max_y, key[1])
    top_left = (0, 0)
    top_right = (max_x, 0)
    bot_left = (0, max_y)
    bot_right = (max_x, max_y)
    return (max_x, max_y), (top_left, top_right, bot_left, bot_right)

def get_value(grid, key):
    if key in grid:
        return grid[key]
    return 0

def count_lights(grid):
    sum_ = 0
    for key, value in grid.items():
        sum_ += value
    return sum_

def transform(old_g, corners, size, day):
    new_g = {}
    for key, value in old_g.items():
        sum_ = 0
        for pair in [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]:
            test = (key[0]+pair[0], key[1]+pair[1])
            sum_ += get_value(old_g, test)
            if sum_ > 3:
                break

        if value == 0:
            if sum_ == 3:
                new_g[key] = 1
            else:
                new_g[key] = 0
        elif value == 1:
            if sum_ == 2 or sum_ == 3:
                new_g[key] = 1
            else:
                new_g[key] = 0

        if day == 2 and key in corners:
            new_g[key] = 1
    return new_g

def challenge(day, nr_of_transforms, test=False):
    g, corners, size = load_grid(day, test)
    for _ in range(nr_of_transforms):
        g = transform(g, corners, size, day)
    return count_lights(g)

print(challenge(1, 4, True))
print(challenge(1, 100))
print(challenge(2, 5, True))
print(challenge(2, 100))
