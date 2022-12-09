import re

with open(r'input_17.txt', 'r') as f:
    raw_inputs = f.read().strip()

# raw_inputs = 'target area: x=20..30, y=-10..-5'

re_input = re.compile('target area\: x\=([\-0-9]+)\.\.([\-0-9]+),\sy=([\-0-9]+)\.\.([\-0-9]+)')
inputs = re_input.findall(raw_inputs)
x_min, x_max, y_min, y_max = [int(x) for x in inputs[0]]
print(f'{x_min=}, {x_max=}, {y_min=}, {y_max=}')

# Day 1: 
# x_value is los van y_value, als som(0->x) binnen range valt is er altijd een X waarde die er voor valt
# in dat geval moet dus enkel y bekeken worden, wat hier het geval is (x_min <= 17+16+15+...+1+0 <= x_max)

# y value: valt in een parabool. bv y = 3 -> 0 (3) 3 (2) 5 (1) 6 (0) 6 (-1) 5 (-2) 3 (-3) 0 (-4) -4 (-5)
# ie: y  -> -1 * (y+1) in 2*y stappen
# => hoogst mogelijk begin y waar y_min <= -1 * (y+1) <= y_max
# => -89 <= -1 * (y+1) <= -148 (grootst mogelijke y)
# => -1 * (y+1) = -148 => y+1 = 148 => y = 147

x_start = 7
y_start = abs(y_min + 1) 

cur_x = 0
cur_y = 0

max_y = 0
while True:
    cur_x += x_start
    x_start = max(x_start - 1, 0)
    cur_y += y_start
    y_start -= 1
    max_y = max(max_y, cur_y)

    if x_min <= cur_x <= x_max and y_min <= cur_y <= y_max:
        # print(f'{cur_x=}, {cur_y=}')
        # print(f'{max_y=}')
        break
    if cur_y <= -200:
        break
print(f'Day 1: {max_y}')

# Day 2:
# Elke combinatie...
# x values en stappen into infinity
# y values en aantal stappen waar het er in valt
# match op stappen?

## y - range ##
y_highest = abs(y_min + 1)
y_lowest = y_min

## x - range ##
find_min_x = 0
count = 0
while True:
    find_min_x += count
    count += 1
    if find_min_x >= x_min:
        break

x_lowest = count - 1
x_highest = x_max

print(f'{x_lowest=} {x_highest=} {y_lowest=} {y_highest=}')

def is_valid(x, y):
    print(f'Checking {x} {y}')
    start_x = 0
    start_y = 0
    while True:
        # print(f'{start_x=} {x=} {start_y=} {y=}')
        start_x = start_x + x
        x = max(x - 1, 0)
        start_y = start_y + y
        y -= 1
        if x_min <= start_x <= x_max and y_min <= start_y <= y_max:
            return True
        if x == 0 and (start_x < x_min or start_x > x_max):
            return False
        if y <= 0 and start_y < y_min:
            return False
    return True

print((x_highest-x_lowest) * (y_highest-y_lowest))

amount = sum(1 for x_ in range(x_lowest, x_highest+1) for y_ in range(y_lowest, y_highest+1) if is_valid(x_, y_))

print(f'Day 2: {amount}')