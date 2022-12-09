from collections import Counter

starting_pattern = '.#.\n..#\n###'

example_book = {
    '../.#': '##./#../...',
    '##/.#': '###/#../.#.',
    '../##': '##./##./##.',
    '.#./..#/###': '#..#/..../..../#..#',}

with open(r'aoc_17_21.txt', 'r') as f:
    raw_inputs = f.read().strip().split('\n')

real_book = {inp.split(' => ')[0]: inp.split(' => ')[1] for inp in raw_inputs}

def insert_slashes(part):
    if len(part) == 4:
        return part[:2] + "/" + part[2:]
    elif len(part) == 9:
        return part[:3] + "/" + part[3:6] + "/" + part[6:]
    else:
        raise ValueError(f"Part {part} not len 4 or 9")

def rotate_and_flip(part):
    l = determine_length(part)
    if l == 2:
        sets = [   # Rotations and Flipped Rotations for size 2
            [0, 1, 2, 3],
            [2, 0, 3, 1], 
            [3, 2, 1, 0], 
            [1, 3, 0, 2], 
            [2, 3, 0, 1], 
            [0, 2, 1, 3], 
            [1, 0, 3, 2], 
            [3, 1, 2, 0]
        ]
    else:
        sets = [   # Rotations and Flipped Rotations for size 3
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [6, 3, 0, 7, 4, 1, 8, 5, 2],
            [8, 7, 6, 5, 4, 3, 2, 1, 0],
            [2, 5, 8, 1, 4, 7, 0, 3, 6],
            [2, 1, 0, 5, 4, 3, 8, 7, 6],
            [8, 5, 2, 7, 4, 1, 6, 3, 0],
            [6, 7, 8, 3, 4, 5, 0, 1, 2],
            [0, 3, 6, 1, 4, 7, 2, 5, 8]
        ]
    
    without = part.replace('/', '')
    for set in sets:
        rotated_part = "".join([without[nr] for nr in set])
        yield insert_slashes(rotated_part)

def determine_length(pattern):
    reduc = pattern.replace('\n', '')
    if int(len(reduc)**(1/2)) % 2 == 0:
        return 2
    else:
        return 3

def split_parts(input_pattern, split):
    pattern = input_pattern.replace('\n', '')

    number_of_lines = len(input_pattern.strip().split('\n'))
    number_of_columns = (len(pattern) // number_of_lines)

    horizontal_groups = number_of_lines // split
    vertical_groups = number_of_columns // split

    groups = []
    for h in range(horizontal_groups):
        for v in range(vertical_groups):
            group = []
            for x in range(split):
                group.append(pattern[((h*split)+x) * number_of_columns + v * split:((h*split)+x) * number_of_columns + (v+1) * split])
            groups.append("/".join(group))
    return groups

def pattern_from_parts(parts):
    if len(parts) == 1:
        return parts[0].replace('/', '\n')
    else:
        sides = int(len(parts)**(1/2))
        part_length = int(len(parts[0].replace('/', ''))**(1/2))

        pattern = ""

        for vertical in range(sides):
            for side_len in range(part_length):
                for horizontal in range(sides):
                    pattern += parts[(vertical * sides) + horizontal].split('/')[side_len]
                pattern += "\n"
        return pattern.strip()

def upgrade(pattern, book):
    parts = split_parts(pattern, determine_length(pattern))

    new_parts = []
    for part in parts:
        for transformed_part in rotate_and_flip(part):
            try:
                new_parts.append(book[transformed_part])
            except:
                continue
            else:
                break

    return pattern_from_parts(new_parts)

def count_pixels_on(pattern):
    c = Counter(pattern)
    return c['#']

def upgrade_x_times(x, pattern, book):
    for _ in range(x):
        print(_)
        pattern = upgrade(pattern, book=book)
    return pattern

print(count_pixels_on(upgrade_x_times(5, starting_pattern, real_book)))
print(count_pixels_on(upgrade_x_times(18, starting_pattern, real_book)))