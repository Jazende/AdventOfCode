with open('aoc_16_2.txt', 'r') as file:
    input_ = file.read()

instructions = input_.split("\n")
#instructions = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']

nrs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pos = [1, 1]
dirs = {'U': [-1, 0],
        'D': [1, 0],
        'L': [0, -1],
        'R': [0, 1]}

def get_pos(*args):
    pos = args[0]
    return nrs[pos[0]][pos[1]]

def max_val(nr):
    return max(min(nr, 2), 0)

for instruction in instructions:
    for command in instruction:
        pos = [max_val(pos[0] + dirs[command][0]), max_val(pos[1] + dirs[command][1])]
        # print(command, end="")
    print("Output: nummer: ", get_pos(pos))


keypad_two = [[None, None, '1', None, None],
              [None, '2', '3', '4', None],
              ['5', '6', '7', '8', '9'],
              [None, 'A', 'B', 'C', None],
              [None, None, 'D', None, None]]

pos = [2, 0]
dirs = {'U': [-1, 0],
        'D': [1, 0],
        'L': [0, -1],
        'R': [0, 1]}

invalid_pos = [[0, 0],
               [0, 1],
               [0, 3],
               [0, 4],
               [1, 0],
               [1, 4],
               [3, 0],
               [3, 4],
               [4, 0],
               [4, 1],
               [4, 3],
               [4, 4]]
print("\n"*3)

def max_val(nr):
    return max(min(nr, 4), 0)

def get_pos(*args):
    pos = args[0]
    result = keypad_two[pos[0]][pos[1]]
    if not result:
        print(pos)
    return result

print(get_pos(pos))

for instruction in instructions:
    for command in instruction:
        new_pos = [max_val(pos[0] + dirs[command][0]), max_val(pos[1] + dirs[command][1])]
        if not new_pos in invalid_pos:
            pos = new_pos
    print("Output: nummer: ", get_pos(pos))
