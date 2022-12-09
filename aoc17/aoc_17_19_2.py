from adventofcode_3 import Punt

REAL = "adventofcode_19.txt"
TEST = "adventofcode_19_test.txt"

alpha = [x for x in "abcdefghijklmnopqrstuvxyz".upper()]

def read_file(file):
    input_ = []
    with open(file, 'r') as f:
        for line in f:
            input_.append(line.replace("\n", ""))
    return input_

def get_nodes(file):
    maze = {}
    input_ = read_file(file)
    for row, line in enumerate(input_):
        if row == 0:
            maze[Punt(row, line.index("|"))] = "+"
            maze["START"] = Punt(row, line.index("|"))
        for col, char in enumerate(line):
            if char == "+" or char == "-" or char == "|" or char in alpha:
                maze[Punt(row, col)] = char
    return maze

def run_through(file, print_ = False):
    maze = get_nodes(file)
    start_point = maze["START"]
    cur_pos = start_point
    text = ""
    directions = [[0, 1], [-1, 0],
                  [0, -1], [1, 0]]
    cur_dir = [1, 0]
    steps = 1
    while True:
        if maze[cur_pos] in alpha:
            text += maze[cur_pos]
        if print_:
            print(cur_pos)
        new_pos = cur_pos + cur_dir
        if new_pos in maze.keys():
            cur_pos = new_pos
            steps += 1
        else:
            left = directions[(directions.index(cur_dir)+1)%4]
            right = directions[(directions.index(cur_dir)+3)%4]
            if cur_pos + left in maze.keys():
                cur_dir = directions[(directions.index(cur_dir)+1)%4]
            elif cur_pos + right in maze.keys():
                cur_dir = directions[(directions.index(cur_dir)+3)%4]
            else:
                if print_:
                    print("End")
                break
    print(text, steps)
run_through(REAL, False)
