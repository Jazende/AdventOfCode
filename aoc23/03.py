with open('input_03.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..'''

########################## DAY 3 PART 1 ########################## 

lines = raw_inputs.strip().split('\n')
numbers = '0123456789'
adjecents = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
max_x = len(lines[0].strip())
max_y = len(lines)


symbols = { char for char in raw_inputs if not char in '.0123456789\n' }
symbol_locations = {}

for line_nr, line in enumerate(lines):
    for idx, char in enumerate(line.strip()):
        if char in symbols:
            # symbol_locations.append((idx, line_nr))
            symbol_locations[(idx, line_nr)] = set()

for symbol_location in symbol_locations.keys():
    for adjecent in adjecents:
        check_spot = (symbol_location[0] + adjecent[0], symbol_location[1] + adjecent[1])
        if lines[check_spot[1]][check_spot[0]] in numbers:
            # find nr start
            start_x = check_spot[0]
            while True:
                if lines[check_spot[1]][start_x-1] in numbers:
                    start_x -= 1
                else:
                    break
            # find nr end
            end_x = check_spot[0]
            while True:
                if (end_x + 1) >= max_x:
                    break
                if lines[check_spot[1]][end_x+1] in numbers:
                    end_x += 1
                else:
                    break
            # add to symbol nrs
            symbol_locations[symbol_location].add(int(lines[check_spot[1]][start_x:end_x+1]))

print(sum(sum(value) for key, value in symbol_locations.items()))

########################## DAY 3 PART 2 ########################## 

part_number = 0
for key, value in symbol_locations.items():
    # enkel ratios zijn nodig -> symbol = '*' en len(2)
    if lines[key[1]][key[0]] == '*' and len(value) == 2:
        list_ = list(value)
        part_number += list_[0] * list_[1]

print(sum(list(value)[0] * list(value)[1] for key, value in symbol_locations.items() if lines[key[1]][key[0]] == '*' and len(value) == 2))
