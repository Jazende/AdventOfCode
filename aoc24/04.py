import os
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX'''

### Part 1 ###

x_positions = []
m_positions = []
a_positions = []
s_positions = []

max_col = 0
max_row = 0

for row, line in enumerate(raw_inputs.strip().split('\n')):
    max_row = row
    for col, letter in enumerate(line):
        if letter == 'X':
            x_positions.append([col, row])
        if letter == 'M':
            m_positions.append([col, row])
        if letter == 'A':
            a_positions.append([col, row])
        if letter == 'S':
            s_positions.append([col, row])
        if row == 0:
            max_col = col

patterns = [
    [[0, 0], [-1,  1], [-2,  2], [-3,  3]], 
    [[0, 0], [ 0,  1], [ 0,  2], [ 0,  3]], 
    [[0, 0], [ 1,  1], [ 2,  2], [ 3,  3]], 
    [[0, 0], [ 1,  0], [ 2,  0], [ 3,  0]], 
    [[0, 0], [ 1, -1], [ 2, -2], [ 3, -3]], 
    [[0, 0], [ 0, -1], [ 0, -2], [ 0, -3]], 
    [[0, 0], [-1, -1], [-2, -2], [-3, -3]], 
    [[0, 0], [-1,  0], [-2,  0], [-3,  0]], 
]

count = 0
for x_pos in x_positions:
    for pattern in patterns:
        m_pos = [x_pos[0] + pattern[1][0], x_pos[1] + pattern[1][1]]
        if not m_pos in m_positions:
            continue
        a_pos = [x_pos[0] + pattern[2][0], x_pos[1] + pattern[2][1]]
        if not a_pos in a_positions:
            continue
        s_pos = [x_pos[0] + pattern[3][0], x_pos[1] + pattern[3][1]]
        if not s_pos in s_positions:
            continue
        count += 1
print(count)

### Part 2 ###

## Patterns: RD, RU, DR, DL
## Verwijderen: LD, LU & UR, UL niet, anders telt alles dubbel mee.

patterns = [
    [[0, 0], [ 2,  0], [ 1,  1], [ 0,  2], [ 2,  2]], # RD
    [[0, 0], [ 2,  0], [ 1, -1], [ 0, -2], [ 2, -2]], # RU
    [[0, 0], [ 0,  2], [ 1,  1], [ 2,  0], [ 2,  2]], # DR
    [[0, 0], [ 0,  2], [-1,  1], [-2,  0], [-2,  2]], # DL
]

count = 0
for m_pos_one in m_positions:
    for pattern in patterns:
        m_pos_two = [m_pos_one[0] + pattern[1][0], m_pos_one[1] + pattern[1][1]]
        if not m_pos_two in m_positions:
            continue
        a_pos     = [m_pos_one[0] + pattern[2][0], m_pos_one[1] + pattern[2][1]]
        if not a_pos in a_positions:
            continue
        s_pos_one = [m_pos_one[0] + pattern[3][0], m_pos_one[1] + pattern[3][1]]
        if not s_pos_one in s_positions:
            continue
        s_pos_two = [m_pos_one[0] + pattern[4][0], m_pos_one[1] + pattern[4][1]]
        if not s_pos_two in s_positions:
            continue
        count += 1
print(count)
