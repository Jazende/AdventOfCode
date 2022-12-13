with open(r'22_08.txt', 'r') as f:
    raw_lines = f.read().strip()

locations = {
    # (column, row): [height, left_vis, top_vis, right_vis, down_vis, trees_visible]
    (idx_col, idx_row): [int(char), False, False, False, False]
    for idx_row, line in enumerate(raw_lines.split('\n'))
    for idx_col, char in enumerate(str(line))
}

# Height/Width as read from locations, which is 0 indexed, so needs +1
width = max(key[0] for key in locations.keys())+1
height = max(key[1] for key in locations.keys())+1

# Can be optimized for 1 outer loop if wanted
# Horizontal
for row in range(height):
    # From left to right
    max_height = -1
    for col in range(width):
        if max_height < locations[(col, row)][0]:
            locations[(col, row)][1] = True
            max_height = locations[(col, row)][0]

    # From right to left
    max_height = -1
    for col in list(range(width)[::-1]):
        if max_height < locations[(col, row)][0]:
            locations[(col, row)][3] = True
            max_height = locations[(col, row)][0]

# Vertical
for col in range(width):
    # From top to bottom
    max_height = -1
    for row in range(height):
        if max_height < locations[(col, row)][0]:
            locations[(col, row)][2] = True
            max_height = locations[(col, row)][0]

    # From right to left
    max_height = -1
    for row in list(range(height))[::-1]:
        if max_height < locations[(col, row)][0]:
            locations[(col, row)][4] = True
            max_height = locations[(col, row)][0]

print(sum(1 if any(v == True for v in values[1:5]) else 0 for values in locations.values()))

max_scenic_score = 0
for col in range(width):
    for row in range(height):
        tree = locations[(col, row)]

        trees_visible_top    = 0
        trees_visible_left   = 0
        trees_visible_right  = 0
        trees_visible_bottom = 0

        # go left, doesn't need +1 cause python stops at last value for list
        for c_col in list(range(0, col))[::-1]:
            trees_visible_left += 1
            if locations[(c_col, row)][0] >= tree[0]:
                break

        # go right, +1 else it counts itself
        for c_col in range(col+1, width):
            trees_visible_right += 1
            if locations[(c_col, row)][0] >= tree[0]:
                break

        # go up, doesn't need +1 cause python stops at last value for list
        for c_row in list(range(0, row))[::-1]:
            trees_visible_top += 1
            if locations[(col, c_row)][0] >= tree[0]:
                break

        # go down +1 else it counts itself
        for c_row in range(row+1, height):
            trees_visible_bottom += 1
            if locations[(col, c_row)][0] >= tree[0]:
                break

        # multiply and check highest
        max_scenic_score = max(max_scenic_score, trees_visible_top * trees_visible_left * trees_visible_right * trees_visible_bottom)

print(max_scenic_score)
