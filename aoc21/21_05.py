import re

re_input = re.compile('(\d+),(\d+) \-\> (\d+),(\d+)')

with open(r'input_05.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2'''

inputs = [[int(x) for x in line] for line in re_input.findall(raw_inputs)]

locations = {}

def add_locations(locations, spot):
    if not spot in locations:
        locations[spot] = 0
    locations[spot] += 1

for inp in inputs:
    delta_x = inp[2] - inp[0]
    delta_y = inp[3] - inp[1]

    sign_x = int(delta_x / abs(delta_x)) if not delta_x == 0 else 0
    sign_y = int(delta_y / abs(delta_y)) if not delta_y == 0 else 0

    count = max(abs(delta_x), abs(delta_y))

    loc = [inp[0], inp[1]]

    while True:
        add_locations(locations, tuple(loc))
        loc[0] += sign_x
        loc[1] += sign_y
        if count == 0:
            break
        count -= 1

# print(locations)
print(sum([1 for loc, count in locations.items() if count > 1]))
